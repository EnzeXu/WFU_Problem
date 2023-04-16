import socket
import json
from datetime import datetime

from backend_utils import *

from const import HOST, PORT


def myprint(string):
    with open("logs/wfu_problem.log", "a") as f:
        f.write(str(string) + "\n")
    print(string)


def get_now_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def handle_request(request):
    try:
        myprint("{} [Backend Server] received original request {}".format(get_now_string(), request))
        method, full_query, version = request.split('\r\n')[0].split(' ')
        params = {}
        myprint("{} [Backend Server] received request {}".format(get_now_string(), full_query))
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
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
            else:
                response_data = {'error': 'Missing parameter'}
                response = json.dumps(response_data)
                response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
        elif path == '/checklogin':
            email = params.get('email')
            password = params.get('password')
            if email and password:
                response_dic = check_login(email=email, password=password)
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
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
            else:
                response_data = {'error': 'Missing parameter'}
                response = json.dumps(response_data)
                response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
        elif path == '/getgroup':
            groupid = params.get('groupid')
            if groupid:
                response_dic = get_group(groupid=groupid)
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
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
            else:
                response_data = {'error': 'Missing parameter'}
                response = json.dumps(response_data)
                response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
        elif path == '/joingroup':
            userid = params.get('userid')
            groupid = params.get('groupid')
            if userid and groupid:
                response_dic = join_group(userid=userid, groupid=groupid)
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
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
            else:
                response_data = {'error': 'Missing parameter'}
                response = json.dumps(response_data)
                response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
        elif path == '/leavegroup':
            userid = params.get('userid')
            groupid = params.get('groupid')
            if userid and groupid:
                response_dic = leave_group(userid=userid, groupid=groupid)
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
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
            else:
                response_data = {'error': 'Missing parameter'}
                response = json.dumps(response_data)
                response_headers = "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n"
                response_headers += "Access-Control-Allow-Origin: *\r\n"
                response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
                response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
        else:
            response_data = {'error': 'Function {} not support'.format(path)}
            response = json.dumps(response_data)
            response_headers = "HTTP/1.1 404 Not Found\r\nContent-Type: application/json\r\n"
            response_headers += "Access-Control-Allow-Origin: *\r\n"
            response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
            response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
    except Exception as e:
        myprint("{} [Backend Server] Error detected: {}".format(get_now_string(), str(e)))
        response_data = {'error': 'Invaild request'}
        response = json.dumps(response_data)
        response_headers = "HTTP/1.1 404 Not Found\r\nContent-Type: application/json\r\n"
        response_headers += "Access-Control-Allow-Origin: *\r\n"
        response_headers += "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
        response_headers += "Access-Control-Allow-Headers: Content-Type, Authorization\r\n"
    myprint("{} [Backend Server] sent {}".format(get_now_string(), str(response)))
    return response_headers + "\r\n" + response


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    myprint("\n{} [Backend Server] Listening on port {} ...".format(get_now_string(), PORT))

    while True:
        try:
            client_connection, client_address = server_socket.accept()
            client_ip = client_address[0]
            myprint("{} [Backend Server] Incoming connection from {}".format(get_now_string(), client_ip))
            request = client_connection.recv(1024).decode()
            response = handle_request(request)
            client_connection.sendall(response.encode())
            client_connection.close()
        except Exception as e:
            myprint("{} [Backend Server] Bad error occurs".format(get_now_string()))
            myprint("{} [Backend Server] Error detected: {}".format(get_now_string(), str(e)))


if __name__ == '__main__':
    run_server()
    # http://127.0.0.1:8888/checklogin?userid=0001&password=mb123456
    # http://127.0.0.1:8888/getuser?userid=0002
