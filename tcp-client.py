import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)
try:
    client_socket.connect(("127.0.0.1", 4466))
    client_socket.send(b"teste\n")
    print(client_socket.recv(1024).decode())
except:
    print("Ocorreu algum erro!")