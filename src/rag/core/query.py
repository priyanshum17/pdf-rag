from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from src.rag.core.configuration import config

CHROMA_PATH = config.file_paths.database_directory

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def query(query_text):
    """
    Main function to perform a similarity search and generate a response using an AI model.

    Args:
        query_text (str): The input query text for which the response is to be generated.
    """
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_relevance_scores(query_text, k=20)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOpenAI(model="gpt-4o-mini")
    response_text = model.invoke(prompt)

    formatted_response = f"Response: {response_text.content}"
    print(formatted_response)
