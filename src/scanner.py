import socket
import argparse

def run_scanner(target,strt,final) -> None:
    # simple port scanner to check for open ports on the local host
    print("=" * 30)
    print("PORT SCANNER")


    for port in range(strt,final + 1):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.01)
        try:
            result = sock.connect_ex((target,port))
            if result == 0:
                print(f"SCANNER: Port {port} is open")
            sock.close()
        except socket.error as e:
            logging.error(f"could not connect to {address}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Professional TCP PORT scanner")

    parser.add_argument("-t", "--target", required=True, help="Target IP address (e.g 127.0.0.1)")
    parser.add_argument("-p", "--ports", default="1-1204", help="Port Range (1-1024)")

    args = parser.parse_args()
    address = args.target

    run_scanner(address,start,end)
