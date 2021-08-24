import sys
from cliente.client import Client

if __name__ == '__main__':
    bar_code = sys.argv[1]
    client = Client(bar_code)
    client.createClient()
    pass
