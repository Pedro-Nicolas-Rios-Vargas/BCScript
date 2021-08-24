import socket
import codecs

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    conn, addr = server.accept()
    with conn:
        print('Connected by', addr)
        while conn:
            data = conn.recv(4096)
            if data:
                conn.send(b'1')
            if not data: break
            print(codecs.decode(data))
            pass
        pass
    pass
