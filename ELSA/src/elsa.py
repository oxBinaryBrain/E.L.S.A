from loader import load_data
from search import search_data

def main():
    print("E.L.S.A - Offline Knowledge Retrieval System")
    knowledge_base = load_data()

    if not knowledge_base:
        print("No data found. Please add base64-encoded files to the 'data/' folder.")
        return

    while True:
        query = input("\nEnter a search term (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break

        results = search_data(knowledge_base, query)

        if results:
            print("\nResults:")
            for res in results:
                for key, value in res.items():
                    print(f"- {key}: {value}")
        else:
            print("No matching results found.")

if __name__ == "__main__":
    main()
