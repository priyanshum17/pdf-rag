# AI-Powered Document Query System

This project implements an AI-powered document query system that allows users to perform similarity searches and generate responses based on document contents. It leverages the `Chroma` vector store, `OpenAIEmbeddings`, and `ChatOpenAI` models.

## Features

- **Document Loading**: Load documents from a specified directory.
- **Text Splitting**: Split loaded documents into smaller, manageable chunks.
- **Vector Store Creation**: Store document chunks in a Chroma vector store.
- **Similarity Search**: Perform similarity searches on the document chunks.
- **Response Generation**: Generate AI-based responses using the `ChatOpenAI` model.

## Prerequisites

- Python 3.7+
- Install required Python packages using `requirements.txt`:
  ```sh
  pip install -r requirements.txt
