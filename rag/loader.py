from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document


POLICY_DIR = Path(__file__).resolve().parent.parent / "policies"


def load_policy_documents() -> list[Document]:
    """
    Load all policy markdown files.

    Returns:
        List[Document]
    """

    print("=" * 60)
    print("Loading policy documents...")
    print(f"Looking in: {POLICY_DIR.resolve()}")
    print("=" * 60)

    documents = []

    files = list(POLICY_DIR.glob("*.md"))

    print(f"Found {len(files)} policy files.")

    for file_path in files:
        print(f"\nLoading: {file_path.name}")

        loader = TextLoader(str(file_path), encoding="utf-8")
        docs = loader.load()

        print(f"Loaded {len(docs)} document(s).")

        for doc in docs:
            doc.metadata.update(
                {
                    "source": file_path.name,
                    "policy": file_path.stem,
                }
            )

        documents.extend(docs)

    print("\n" + "=" * 60)
    print(f"Total documents loaded: {len(documents)}")
    print("=" * 60)

    return documents