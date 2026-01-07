import socket
import argparse

parser = argparse.ArgumentParser(description="Professional TCP PORT scanner")

parser.add_argument("-t", "--target", required=True, help="Target IP address (e.g 127.0.0.1)")
parser.add_argument("-p", "--ports", default="1-1204", help="Port Range (1-1024)")

args = parser.parse_args()
address = args.target
port_range = args.ports
split_range = port_range.split('-')
start = int(split_range[0])
end = int(split_range[1])

# simple port scanner to check for open ports on the local host
print("=" * 30)
print("PORT SCANNER")


for port in range(start,end + 1):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.01)
    result = sock.connect_ex((address,port))
    if result == 0:
        print(f"SCANNER: Port {port} is open")
    sock.close()
