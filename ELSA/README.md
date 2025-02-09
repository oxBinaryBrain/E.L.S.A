# E.L.S.A - Offline Knowledge Retrieval System

E.L.S.A (Enhanced Local Search Algorithm) allows users to retrieve knowledge from base64-encoded JSON datasets stored locally.

## How It Works
1. Place base64-encoded JSON files inside the `data/` folder (files must have a `.b64` extension).
2. Run `elsa.py` for CLI or `ui.py` for GUI.

## Example Base64 File
Convert a JSON file to Base64:
```sh
cat datasets/sample.json | base64 > data/sample.b64
```

Run the project:
```sh
cd src
python3 elsa.py
```

Run GUI:
```sh
python3 ui.py
```

## Dependencies
Install required dependencies:
```sh
pip install -r requirements.txt
```
