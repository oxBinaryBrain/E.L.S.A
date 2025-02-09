import os
import base64
import json

DATA_FOLDER = "data/"

def load_data():
## Load and decode all base64-encoded JSON files from the data/ folder
    knowledge_base = []
    
    if not os.path.exists(DATA_FOLDER):
        print(f"Folder '{DATA_FOLDER}' not found. Creating it...")
        os.makedirs(DATA_FOLDER)
        return knowledge_base
    
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".b64"):
            filepath = os.path.join(DATA_FOLDER, filename)
            with open(filepath, "r") as file:
                try:
                    decoded_data = base64.b64decode(file.read()).decode("utf-8")
                    json_data = json.loads(decoded_data)
                    knowledge_base.append(json_data)
                except Exception as e:
                    print(f"Error decoding {filename}: {e}")

    return knowledge_base
