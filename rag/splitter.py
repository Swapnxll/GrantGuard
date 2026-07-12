from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=100,
    separators=[
        "\n# ",
        "\n## ",
        "\n### ",
        "\n\n",
        "\n",
        ". ",
        " ",
        "",
    ],
)


def split_documents(documents: list[Document]) -> list[Document]:
    """
    Split policy documents into semantic chunks.
    """

    print("\n" + "=" * 60)
    print("Splitting documents...")
    print("=" * 60)
    print(f"Input documents: {len(documents)}")

    if not documents:
        print("No documents received!")
        return []

    chunks = text_splitter.split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    if chunks:
        print("\nFirst chunk metadata:")
        print(chunks[0].metadata)

        print("\nFirst chunk preview:")
        print("-" * 50)
        print(chunks[0].page_content[:300])
        print("-" * 50)
    else:
        print("No chunks were created!")

    print("=" * 60)

    return chunks