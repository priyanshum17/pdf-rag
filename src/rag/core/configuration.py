import json
from pathlib import Path

from pydantic import BaseModel

CONFIG_PATH = Path("src/rag/sysconfig/appSettings.json")


class FilePaths(BaseModel):
    document_directory: str


class Configuration(BaseModel):
    file_paths: FilePaths


settings = json.load(open(CONFIG_PATH, "r"))
config = Configuration(**settings)
