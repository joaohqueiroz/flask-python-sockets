from server import socket, json, Thread
import random


def create_list():
    print("Escreva a quantidade de digitos: ")
    len = int(input())

    print("Escreva o número que deseja encontrar: ")
    num = int(input())

    count = 0
    numbers = []
    while count < len:
        numbers.append(random.randint(0, 9))
        count += 1

    numbers = [numbers[i::2] for i in range(2)]

    thread = Thread(target=request, args=(numbers[0], num, 3001))
    thread.start()

    thread = Thread(target=request, args=(numbers[1], num, 3002))
    thread.start()


def request(numbers, num, port):
    sck = socket()

    server_info = ('127.0.0.1', port)
    sck.connect(server_info)
    print(f"Conexao com o servidor na porta {port} foi aceita!")

    data = {"numbers": numbers, "num": num}

    sck.send(bytes(json.dumps(data), "utf-8"))
    index = int(sck.recv(1000))
    if index != -1:
        print(f"Valor encontrado no índice {index}\n")
    else:
        print("Valor não encontrado!\n")
    sck.close()


if __name__ == '__main__':
    create_list()
