from setuptools import setup, find_packages

setup(
    name="text_rank",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "nltk>=3.7",
        "networkx>=3.0",
        "numpy",
        "scipy"
    ],
    package_dir={'text_rank': 'text_rank'},
)
