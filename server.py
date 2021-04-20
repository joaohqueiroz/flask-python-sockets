from socket import socket
from threading import Thread
import sys
import json

porta = 3000


def processar(conexao):
    data = json.loads(conexao.recv(1000))
    numbers = data["numbers"]
    print(numbers)
    num = data["num"]

    if num in numbers:
        index = numbers.index(num)
    else:
        index = -1

    conexao.send(b"%d" % index)

    conexao.close()


def escutar():
    print("Iniciando Servidor...")
    socket_bind_info = ('127.0.0.1', porta)
    sck = socket()
    sck.bind(socket_bind_info)
    sck.listen()
    print("Servidor Iniciado!")

    while True:
        try:
            conexao, origem = sck.accept()
            print("Nova conexão estabelecida...")
            thread = Thread(target=processar, args=(conexao, ))
            thread.start()
            print(f"Thread iniciada - {thread}")

        except KeyboardInterrupt:
            sck.close()
            print("Programa Encerrado!")


if __name__ == '__main__':
    porta = int(sys.argv[1])
    escutar()
