from vectorstore import build_vectorstore

def main():
    db = build_vectorstore()

    print(f"Indexed {db._collection.count()} chunks")

# if __name__ == "__main__":
#     main()