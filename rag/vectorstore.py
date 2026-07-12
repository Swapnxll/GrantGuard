from pathlib import Path

from langchain_chroma import Chroma

from embeddings import embedding_model
from loader import load_policy_documents
from splitter import split_documents


VECTOR_DB_DIR = Path(__file__).parent / "vector_db"


def build_vectorstore() -> Chroma:
    """
    Build a new vector database from policy documents.
    """

    documents = load_policy_documents()
    chunks = split_documents(documents)

    print(f"Documents: {len(documents)}")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(VECTOR_DB_DIR),
    )

    return db


def load_vectorstore() -> Chroma:
    """
    Load an existing vector database.
    """

    return Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embedding_model,
    )