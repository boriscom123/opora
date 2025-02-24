import os
import json
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def find_files(path_fragment):
    results = []
    for root, dirs, files in os.walk("/"):  # Поиск по всей файловой системе
        for file in files:
            if path_fragment in os.path.join(root, file):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                creation_time = os.path.getctime(file_path)
                creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
                results.append({
                    "file_name": file,
                    "file_path": file_path,
                    "file_size": file_size,
                    "creation_date": creation_date
                })
    return results

@app.route('/search', methods=['GET'])
def search_files():
    path_fragment = request.args.get('path')
    if not path_fragment:
        return jsonify({"error": "Path fragment is required"}), 400

    files = find_files(path_fragment)
    return jsonify(files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
