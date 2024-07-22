# Query Script Explanation

The `query.py` script is responsible for performing a similarity search on document chunks stored in a vector database and generating a response based on the most relevant chunks using an AI model. Below is a detailed explanation of the script:

## Imports

```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from src.rag.core.configuration import config
