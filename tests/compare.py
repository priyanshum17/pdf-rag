"""
Main script to demonstrate the usage of OpenAI embeddings and evaluation.

This script loads OpenAI API key from environment variables, initializes an embedding function,
and performs a comparison of embeddings using a pre-defined evaluator.

Requirements:
    - langchain_openai: OpenAIEmbeddings class for embedding retrieval.
    - langchain.evaluation: load_evaluator function for loading evaluators.
    - dotenv: load_dotenv function for loading environment variables.
    - openai: OpenAI API for accessing language models.
    - os: Operating system module for accessing environment variables.

Environment Variables:
    - OPENAI_API_KEY: Must be set in the environment to access OpenAI API.

Functions:
    main(): Main function that demonstrates the usage of OpenAI embeddings and evaluation.
        - Initializes OpenAI API with the provided API key.
        - Retrieves embedding vector for the word 'apple' and prints it.
        - Compares embedding vectors of two words ('apple' and 'iphone') using a pairwise evaluator.

Usage:
    $ python script_name.py

Example Output:
    Vector for 'apple': [0.12, 0.34, ..., 0.56]
    Vector length: 768
    Comparing (apple, iphone): 0.85
"""

from langchain_openai import OpenAIEmbeddings
from langchain.evaluation import load_evaluator
from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


def main():
    embedding_function = OpenAIEmbeddings()
    vector = embedding_function.embed_query("apple")
    print(f"Vector for 'apple': {vector}")
    print(f"Vector length: {len(vector)}")

    evaluator = load_evaluator("pairwise_embedding_distance")
    words = ("apple", "iphone")
    x = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    print(f"Comparing ({words[0]}, {words[1]}): {x}")


if __name__ == "__main__":
    main()
