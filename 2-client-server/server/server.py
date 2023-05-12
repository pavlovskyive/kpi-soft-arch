import socket

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', 8080))
        server_socket.listen(1)
        print("Server started. Listening on port 8080...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            # Handle client request
            request = client_socket.recv(1024).decode('utf-8')
            response = generate_response(request)

            # Send response to client
            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()


def generate_response(request):
    # Handle the request from the client and generate a response
    if request == 'hello':
        return 'Hello, client!'
    else:
        return 'Invalid request'


if __name__ == '__main__':
    start_server()
