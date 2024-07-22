import os
from dotenv import load_dotenv

import openai
from langchain_openai import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

from src.rag.core.configuration import config

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

DOCS_PATH = config.file_paths.document_directory


def get_csv_files(directory_path):
    """
    Returns a list of all CSV files in the given directory.

    Parameters:
    - directory_path (str): The path to the directory where CSV files are located.

    Returns:
    - list: A list of paths to CSV files found in the directory.
    """
    csv_files = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            csv_files.append(os.path.join(directory_path, filename))
    return csv_files


class CSVReader:
    def __init__(self, file_path):
        """
        Initializes the CSVReader with a file path and sets up the agent for querying.

        Parameters:
        - file_path (str): The path to the CSV file to be read.
        """
        self.file_path = file_path
        self.agent = create_csv_agent(
            OpenAI(temperature=0), file_path, verbose=True, allow_dangerous_code=True
        )

    def query(self, question: str):
        """
        Queries the CSV file using the agent and returns the result.

        Parameters:
        - question (str): The question to be asked about the CSV data.

        Returns:
        - str: The result of the query.
        """
        return self.agent.run(question)


def query_csv(query: str):
    """
    Queries the first CSV file found in the specified directory and prints the result.

    Parameters:
    - query (str): The question to be asked about the CSV data.
    """
    directory_path = DOCS_PATH

    csv_files = get_csv_files(directory_path)

    if csv_files:
        csv_file_path = csv_files[0]
        csv_reader = CSVReader(csv_file_path)

        result = csv_reader.query(query)
        print(result)
    else:
        print("No CSV files found in the directory.")
