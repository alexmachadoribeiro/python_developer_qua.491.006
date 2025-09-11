import os
import platform
import psutil
import socket

print(f"Sistema Operacional: {platform.system()} {platform.release()}.")
print(f"Nome do usuário: {os.environ.get("USERNAME")}.")
print(f"IPv4: {socket.gethostbyname(socket.gethostname())}.")

# coleta informações sobre as portas TCP e UDP
print("Portas abertas:\n")
connectall = psutil.net_connections(kind="inet")
only_udp = [conn for conn in psutil.net_connections(kind="inet") if conn.type == socket.SOCK_DGRAM]

# separar as informações sobre as portas
only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.status == psutil.CONN_LISTEN] # tpc
only_udp_listening_ports = [conn.laddr.port for conn in only_udp] # udp

# remover as portas repetidas da lista
only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_udp_listening_ports))

# organizar as portas
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

# mostra as portas TCP
print("Portas TCP:\n")
for port in only_tcp_listening_ports:
    print(f"Porta TCP: {port} aberta.")

# mostra as portas UDP
print("Portas UDP:\n")
for port in only_udp_listening_ports:
    print(f"Porta UDP: {port} aberta.")