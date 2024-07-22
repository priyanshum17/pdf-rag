from src.rag.core.rag import create_vector_db
from src.rag.core.query import query

create_vector_db()
query("Give me a detailed summary of this?")
