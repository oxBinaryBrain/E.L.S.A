import tkinter as tk
from loader import load_data
from search import search_data

class ELSAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E.L.S.A - Offline Knowledge Search")

        self.label = tk.Label(root, text="Enter search query:")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.perform_search)
        self.search_button.pack()

        self.result_text = tk.Text(root, height=15, width=60)
        self.result_text.pack()

        self.knowledge_base = load_data()

    def perform_search(self):
        query = self.entry.get().strip()
        self.result_text.delete("1.0", tk.END)
        
        if not query:
            self.result_text.insert(tk.END, "Please enter a search term.\n")
            return
        
        results = search_data(self.knowledge_base, query)

        if results:
            for res in results:
                for key, value in res.items():
                    self.result_text.insert(tk.END, f"{key}: {value}\n\n")
        else:
            self.result_text.insert(tk.END, "No matching results found.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ELSAApp(root)
    root.mainloop()
