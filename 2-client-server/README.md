# Client-Server Pattern in Python

This repository demonstrates a basic implementation of the Client-Server pattern in Python. The pattern involves two main components: the server-side code and the client-side code. Together, they enable communication and data exchange between clients and a central server.

## Server-Side Implementation

The server-side implementation consists of a server script (`server.py`) that listens for incoming connections from clients. Upon connection, the server receives client requests, processes them, and sends back responses.

To start the server, run the following command:

```bash
python3 server.py
```

The server listens on `localhost` at port 8080. When a client connects, the server accepts the connection, handles the client's request using the handle_request() function, and sends back a response.

## Client-Side Implementation

The client-side implementation consists of a client script (`client.py`) that connects to the server and sends requests. It prompts the user to enter a request, sends it to the server, and displays the server's response.

To start the client, run the following command:

```bash
python3 client.py
```

The client connects to the server running on `localhost` at port 8080. It sends the user's request to the server, receives the response, and displays it on the console.

## Usage

1. Start the server by running server.py.
2. In a separate terminal, start the client by running client.py.
3. Enter a request in the client terminal and observe the server's response.
4. Try different requests to see how the client and server interact (***implemented example: `hello`***)
5. Press Ctrl+C in both terminals to stop the client and server.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```

## Conclusion

This implementation provides a basic demonstration of the Client-Server pattern in Python. The server and client components are separate entities that communicate over a network connection. The code can be extended and customized to meet specific requirements.