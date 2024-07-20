import os
from pathlib import Path

import streamlit as st

from src.rag.core.configuration import config


class Interface:
    """
    This class represents a Streamlit app that processes PDF files.

    Methods:
        info: Displays the title and introductory information for the app.
        save_uploaded_file: Saves the uploaded file to the specified directory.
        list_uploaded_files: Lists all uploaded PDF files in the specified directory.
        run: Runs the Streamlit app.
    """

    def info(self) -> None:
        st.title("PDF-RAG")

    def save_uploaded_file(self, uploaded_file) -> None:
        save_path = Path(config.file_paths.document_directory)
        save_path.mkdir(parents=True, exist_ok=True)

        with open(save_path / uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"PDF file '{uploaded_file.name}' uploaded successfully!")

    def list_uploaded_files(self) -> list:
        save_path = Path(config.file_paths.document_directory)
        files = [f.name for f in save_path.glob("*.pdf")] if save_path.exists() else []
        return files

    def run(self):
        self.info()

        # Upload file in the sidebar with a unique key
        with st.sidebar:
            uploaded_file = st.file_uploader(
                "Choose a PDF file", type="pdf", key="pdf_uploader"
            )

            if uploaded_file is not None:
                self.save_uploaded_file(uploaded_file)

            st.sidebar.write("Uploaded Files:")
            files = self.list_uploaded_files()
            if files:
                for file in files:
                    st.sidebar.write(file)
            else:
                st.sidebar.write("No files uploaded yet.")
