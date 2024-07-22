import json
from pathlib import Path
from pydantic import BaseModel

CONFIG_PATH = Path("src/rag/sysconfig/appSettings.json")


class FilePaths(BaseModel):
    """
    A Pydantic model to represent file paths configuration.

    Attributes:
        document_directory (str): The directory path where documents are stored.
        data_directory (str): The directory path where data files are stored.
        database_directory (str): The directory path where the database files are stored.
    """

    document_directory: str
    data_directory: str
    database_directory: str


class Configuration(BaseModel):
    """
    A Pydantic model to represent the overall configuration.

    Attributes:
        file_paths (FilePaths): An instance of FilePaths model containing paths configuration.
    """

    file_paths: FilePaths


settings = json.load(open(CONFIG_PATH, "r"))

config = Configuration(**settings)
