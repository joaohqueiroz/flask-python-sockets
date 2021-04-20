from socket import socket
from threading import Thread
import sys
import json

port = 3000


def process(connection):
    data = json.loads(connection.recv(1000))
    numbers = data["numbers"]
    print(numbers)
    num = data["num"]

    if num in numbers:
        index = numbers.index(num)
    else:
        index = -1

    connection.send(b"%d" % index)

    connection.close()


def listen():
    print("Iniciando Servidor...")
    socket_bind_info = ('127.0.0.1', port)
    sck = socket()
    sck.bind(socket_bind_info)
    sck.listen()
    print("Servidor Iniciado!")

    while True:
        try:
            connection, origin = sck.accept()
            print("Nova conexão estabelecida...")
            thread = Thread(target=process, args=(connection, ))
            thread.start()
            print(f"Thread iniciada - {thread}")

        except KeyboardInterrupt:
            sck.close()
            print("Programa Encerrado!")


if __name__ == '__main__':
    port = int(sys.argv[1])
    listen()
