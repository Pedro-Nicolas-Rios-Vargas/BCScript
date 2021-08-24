class Client:
    def __init__(self, message):
        self.HOST = 'localhost'
        self.PORT = 8080
        self.message = message
        pass

    def createClient(self):
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.HOST, self.PORT))
            client.send(self.message.encode('UTF-8'))
            data = client.recv(1024)
            if data == b'1':
                print('Mensaje enviado')
                pass
            pass
        pass

