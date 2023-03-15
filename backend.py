import socket
import json

HOST, PORT = '18.117.181.47', 9999


def handle_request(request):
    """Handle HTTP request"""
    # Extract the request method, path, and HTTP version
    method, path, version = request.split('\r\n')[0].split(' ')

    # Extract the query parameters from the request path
    params = {}
    print("[Backend Server] received request {}".format(path))
    if '?' in path:
        path, query = path.split('?')
        query_params = query.split('&')
        for param in query_params:
            key, value = param.split('=')
            params[key] = value

    # Generate a response based on the requested path and parameters
    if path == '/getuser':
        userid = params.get('userid')
        if userid:
            response_data = {'request_type': '/getuser', 'userid': userid}
            response = json.dumps(response_data)
            response_headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
        else:
            response_data = {'error': 'Missing "userid" parameter'}
            response = json.dumps(response_data)
            response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
    elif path == '/checklogin':
        userid = params.get('userid')
        password = params.get('password')
        if userid and password:
            response_data = {'request_type': '/checklogin', 'userid': userid, 'password': password}
            response = json.dumps(response_data)
            response_headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
        else:
            response_data = {'error': 'Missing "userid" parameter'}
            response = json.dumps(response_data)
            response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
    # elif path == '/getcourse':
    #     courseid = params.get('courseid')
    #     semester = params.get('semester')
    #     if courseid and semester:
    #         response_data = {'courseid': courseid, 'semester': semester}
    #         response = json.dumps(response_data)
    #         response_headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
    #     else:
    #         response_data = {'error': 'Missing "courseid" or "semester" parameter'}
    #         response = json.dumps(response_data)
    #         response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
    else:
        response_data = {'error': 'Page not found'}
        response = json.dumps(response_data)
        response_headers = "HTTP/1.1 404 Not Found\r\nContent-Type: application/json\r\n"

    return response_headers + "\r\n" + response


def run_server():
    """Run HTTP server"""
    # Create a TCP socket and bind it to a specific host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Listening on port {PORT}...")

    while True:
        # Wait for a client to connect
        client_connection, client_address = server_socket.accept()

        # Receive the client's request
        request = client_connection.recv(1024).decode()

        # Handle the request and generate a response
        response = handle_request(request)

        # Send the response back to the client
        client_connection.sendall(response.encode())

        # Close the connection with the client
        client_connection.close()


if __name__ == '__main__':
    run_server()
