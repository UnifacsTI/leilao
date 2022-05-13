#CLIENTE VENDEDOR
import socket
# FORMATO = "utf-8"
tipoCliente=1

# def start():
#     pass

host = socket.gethostname()  #ip do servidor
port = 55551
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


nomeArtigo = input("Digite o nome do Artigo: ")
descArtigo = input("Digite a descrição: ")
valorArtigo = input("Digite o valor: ")

artigo = "nomeArtigo:" + nomeArtigo + "," + "descArtigo:" + descArtigo + "," + "valor:"+ valorArtigo

#print(artigo)


cliente.connect((host, port))
cliente.send(artigo.encode())



# start()