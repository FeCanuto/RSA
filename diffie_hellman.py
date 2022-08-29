# echo-client.py
import random
import primo
import socket

# números primos conhecido pelo server e client, chaves públicass
p = 97
q = 67
HOST = "127.0.0.1"  # Endereço de interface de loopback padrão (localhost)
PORT = 65432  # Porta usada pelo server


def dh_client():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))
        while True:
            a = random.randrange(1, 100)  # chave privada
            x = pow(q, a) % p  # x = q^a mod p

            # enviando x ao servidor para ser estabelecido segredo
            s.sendall(str(x).encode('utf8'))

            data = s.recv(1024)
            strings = data.decode('utf8')

            # computando chave
            y = int(strings)
            ka = pow(y, a) % p

            if primo.verificar_primo(ka) == True:
                break
        return ka


def dh_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # O método .bind() é usado para associar o soquete a uma interface de rede e número de porta específicos
        s.bind((HOST, PORT))
        s.listen()  # .listen() permite que um servidor aceite conexões
        # .accept usada por um servidor para aceitar uma solicitação de conexão de um cliente.
        conn, addr = s.accept()
        with conn:

            print(f"Connected by {addr}")

            while True:
                b = random.randrange(1, 100)
                y = pow(q, b) % p  # y = q^b mod p

                data = conn.recv(1024)  # dados recebidos do client
                strings = data.decode('utf8')  # decodificando utf-8

                if not data:
                    break

                # enviando dados encodados (utf-8) para client
                conn.sendall(str(y).encode('utf-8'))

                # computando chave
                x = int(strings)
                kb = pow(x, b) % p

                if primo.verificar_primo(kb) == True:
                    print(f"Chave privada {kb}")
                    break

            return kb
        