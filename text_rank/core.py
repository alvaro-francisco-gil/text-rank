import nltk
import networkx as nx
from nltk.tokenize import TreebankWordTokenizer
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from collections import defaultdict

class TextRankKeywordExtractor:
    def __init__(self, window_size=5, pos_tags=('NN', 'NNS', 'JJ', 'JJR', 'JJS')):
        self.window_size = window_size
        self.pos_tags = pos_tags
        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = TreebankWordTokenizer()
        
    def _filter_words(self, text):
        """Extract nouns and adjectives using POS tagging"""
        tokens = self.tokenizer.tokenize(text)
        # Use default English tagger
        pos_tagged = pos_tag(tokens, lang='eng')
        return [
            word.lower() for word, tag in pos_tagged
            if tag in self.pos_tags and word.isalnum() and word.lower() not in self.stop_words
        ]

    def build_cooccurrence_graph(self, text):
        """Construct weighted co-occurrence graph"""
        words = self._filter_words(text)
        graph = nx.Graph()
        
        # Create nodes for all candidate words
        for word in set(words):
            graph.add_node(word)
            
        # Build edges with weights based on co-occurrence
        cooccurrence = defaultdict(int)
        for i in range(len(words)):
            for j in range(i+1, min(i+self.window_size, len(words))):
                pair = tuple(sorted([words[i], words[j]]))
                cooccurrence[pair] += 1
                
        for (w1, w2), count in cooccurrence.items():
            graph.add_edge(w1, w2, weight=count)
            
        return graph

    def extract_keywords(self, text, top_n=None):
        """
        Extract keywords using weighted PageRank
        
        Args:
            text (str): The input text to analyze
            top_n (int, optional): Number of top keywords to return. If None, returns all keywords.
            
        Returns:
            List of tuples containing (word, score) pairs, sorted by score in descending order
        """
        graph = self.build_cooccurrence_graph(text)
        scores = nx.pagerank(graph, weight='weight')
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        if top_n is None:
            return sorted_scores
        else:
            return sorted_scores[:top_n]

    def export_pajek(self, graph, filename):
        """Export graph to Pajek format"""
        with open(filename, 'w') as f:
            # Write vertices
            f.write(f"*Vertices {len(graph.nodes())}\n")
            for i, node in enumerate(graph.nodes(), 1):
                f.write(f'{i} "{node}"\n')
            
            # Write edges
            f.write("*Edges\n")
            for u, v, data in graph.edges(data=True):
                f.write(f"{list(graph.nodes()).index(u)+1} {list(graph.nodes()).index(v)+1} {data['weight']}\n")
