import socket
import json

from backend_utils import *

from const import HOST, PORT


def handle_request(request):
    try:
        method, full_query, version = request.split('\r\n')[0].split(' ')
        params = {}
        print("[Backend Server] received request {}".format(full_query))
        if '?' in full_query:
            path, query = full_query.split('?')
            query_params = query.split('&')
            for param in query_params:
                key, value = param.split('=')
                params[key] = value
        else:
            path = full_query

        if path == '/getuser':
            userid = params.get('userid')
            if userid:
                response_dic = get_user(userid=userid)
                response_data = {
                    'info': {
                        'request': full_query,
                        'request_type': path,
                    },
                    'request': params,
                    'response': response_dic,
                }
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
                response_dic = check_login(userid=userid, password=password)
                response_data = {
                    'info': {
                        'request': full_query,
                        'request_type': path,
                    },
                    'request': params,
                    'response': response_dic,
                }
                response = json.dumps(response_data)
                response_headers = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
            else:
                response_data = {'error': 'Missing "userid" parameter'}
                response = json.dumps(response_data)
                response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
        else:
            response_data = {'error': 'Page not found'}
            response = json.dumps(response_data)
            response_headers = "HTTP/1.1 404 Not Found\r\nContent-Type: application/json\r\n"
    except Exception as e:
        print(e)
        response_data = {'error': 'Invaild request'}
        response = json.dumps(response_data)
        response_headers = "HTTP/1.1 404 Not Found\r\nContent-Type: application/json\r\n"

    return response_headers + "\r\n" + response


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("[Backend Server] Listening on port {} ...".format(PORT))

    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        response = handle_request(request)
        client_connection.sendall(response.encode())
        client_connection.close()


if __name__ == '__main__':
    run_server()
    # http://127.0.0.1:8888/checklogin?userid=0001&password=mb123456
    # http://127.0.0.1:8888/getuser?userid=0002
