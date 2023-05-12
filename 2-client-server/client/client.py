import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    print("Connected to the server.")

    # Send request to the server
    request = input("Enter a request: ")
    client_socket.sendall(request.encode('utf-8'))

    # Receive and print the server's response
    response = client_socket.recv(1024).decode('utf-8')
    print("Server response:", response)

    client_socket.close()


if __name__ == '__main__':
    start_client()