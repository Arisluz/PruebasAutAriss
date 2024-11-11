from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = '0.0.0.0'
port = 8080

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')  # Especifica el charset como utf-8
        self.end_headers()
        self.wfile.write('¡Hola Mundo!\n'.encode('utf-8'))  # Codifica el texto como bytes usando UTF-8

def run():
    server_address = (hostname, port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Servidor corriendo en http://{hostname}:{port}/')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
