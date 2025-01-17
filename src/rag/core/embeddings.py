import os
import shutil
from dotenv import load_dotenv

import openai
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from src.rag.core.configuration import config

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

CHROMA_PATH = config.file_paths.database_directory
DATA_PATH = config.file_paths.data_directory


def create_vector_db():
    """
    Main function to generate the data store.
    """
    generate_data_store()


def generate_data_store():
    """
    Function to generate the data store by loading documents, splitting text,
    and saving to the Chroma vector store.
    """
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    """
    Load markdown documents from the specified data directory.

    Returns:
        list[Document]: A list of loaded documents.
    """
    loader = DirectoryLoader(DATA_PATH, glob="*.pdf")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    """
    Split the loaded documents into smaller chunks using a recursive character text splitter.

    Args:
        documents (list[Document]): A list of documents to be split.

    Returns:
        list[Document]: A list of document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    return chunks


def save_to_chroma(chunks: list[Document]):
    """
    Save the document chunks to the Chroma vector store.

    Args:
        chunks (list[Document]): A list of document chunks to be saved.
    """
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(
        chunks,
        OpenAIEmbeddings(model="text-embedding-3-large"),
        persist_directory=CHROMA_PATH,
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")
