import socket

# simple port scanner to check for open ports on the local host

address = "127.0.0.1"


for port in range(1,1025):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.01)
    result = sock.connect_ex((address,port))
    if result == 0:
        print(f"SCANNER: Port {port} is open")
    sock.close()
