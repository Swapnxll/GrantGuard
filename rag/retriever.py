from langchain_core.documents import Document

from .vectorstore import load_vectorstore


class PolicyRetriever:
    """
    Retrieves relevant policy chunks from the vector database.
    """

    def __init__(self):
        print("Loading policy vector database...")
        self.vectorstore = load_vectorstore()
        print("Policy vector database loaded.")

    def retrieve(
        self,
        query: str,
        k: int = 4,
    ) -> list[Document]:
        """
        Retrieve the top-k most relevant policy chunks.

        Args:
            query: Search query.
            k: Number of chunks to retrieve.

        Returns:
            List of retrieved LangChain Documents.
        """

        print("\n" + "=" * 60)
        print("Policy Retrieval")
        print("=" * 60)
        print(f"Query:\n{query}\n")

        documents = self.vectorstore.similarity_search(
            query=query,
            k=k,
        )

        print(f"Retrieved {len(documents)} chunks.\n")

        for i, doc in enumerate(documents, start=1):
            print(f"[{i}] {doc.metadata.get('source', 'Unknown')}")
            print(doc.page_content[:150].replace("\n", " "))
            print("-" * 60)

        return documents

    def retrieve_context(
        self,
        query: str,
        k: int = 4,
    ) -> str:
        """
        Retrieve policy chunks and format them into a single
        context string for the LLM.
        """

        documents = self.retrieve(query, k)

        context = []

        for i, doc in enumerate(documents, start=1):
            source = doc.metadata.get("source", "Unknown")

            context.append(
                f"""
Policy {i}
Source: {source}

{doc.page_content}
"""
            )

        return "\n\n".join(context)


# Singleton instance used throughout the application
retriever = PolicyRetriever()