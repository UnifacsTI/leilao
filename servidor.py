from asyncio.windows_events import NULL
import socket

host = socket.gethostname()
port = 55551

print(f'HOST: {host} , PORT{port}')

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)

while True:
    print ('aguardando conexao' )
    con, adr = serv.accept() 
    msg = con.recv(1024)
    print(msg.decode())
    print ('conectado' )



# while True:
#     con, adr = serv.accept()
#     while True:
#         msg = con.recv(1024)
#         if(msg):
#             msg = msg.decode()
#             print(msg)
#             msg = NULL