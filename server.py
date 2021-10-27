import socket
import codecs


class ServerSocket:

    def __init__(self):
        self.runServer = True

    def initServer(self):
        HOST = 'localhost'
        PORT = 8080
        barcode = ''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            result = ''
            # 60 segs of utility, after that the socket died.
            server.settimeout(60)
            # If another socket are bound to the same address that this socket
            # gonna use, the old socket just go to BLOCKING MODE and let this
            # socket use the address. 👍
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((HOST, PORT))
            server.listen(1)
            conn, addr = server.accept()
            with conn:
                print('Connected by', addr)
                while conn:
                    data = conn.recv(4096)
                    print(data)
                    if data:
                        conn.send(b'1')
                    if not data:
                        print('Socket server apagado.')
                        break
                    result = codecs.decode(data)
                    barcode = result
                    print(result)
#            server.close()
        return barcode

    def disconnectServer(self):
        self.runServer = False
