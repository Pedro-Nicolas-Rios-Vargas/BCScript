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
            print('\nIniciando el servidor socket..')
            result = ''
            # 60 segs of utility, after that the socket died.
            server.settimeout(10)
            # If another socket are bound to the same address that this socket
            # gonna use, the old socket just go to BLOCKING MODE and let this
            # socket use the address. 👍
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            server.bind((HOST, PORT))
            print(f'\nconectado al host: { HOST }')
            print(f'conectado al puerto: { PORT }\n')
            server.listen(1)
            try:
                conn, addr = server.accept()
                with conn:
                    print('Conectado con: ', addr)
                    while conn:
                        data = conn.recv(4096)
                        if data:
                            conn.send(b'1')
                        if not data:
                            break
                        result = codecs.decode(data)
                        barcode = result
                        print(f'Barcode: {result}')

            except socket.timeout:
                print('Socket server timeout')

            print('Servidor socket apagado.\n')
            server.close()
        return barcode

    def disconnectServer(self):
        self.runServer = False
