import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class MCPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Извлекаем фрагмент пути из запроса
        path_fragment = self.path.lstrip('/')

        # Ищем файлы по фрагменту пути
        results = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                if path_fragment in os.path.join(root, file):
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                    results.append({
                        'name': file,
                        'path': file_path,
                        'size': file_size,
                        'creation_time': creation_time
                    })

        # Отправляем ответ в формате JSON
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(results).encode())

def run(server_class=HTTPServer, handler_class=MCPServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting MCP server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
