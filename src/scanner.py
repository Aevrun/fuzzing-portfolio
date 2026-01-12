import socket
import logging

from src.crawler import LOG_DIR

LOG_FILE = LOG_DIR / "Port_scanner.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ], force=True
)

def run_scanner(target,strt,final) -> None:
    # simple port scanner to check for open ports on the local host
    print("=" * 50)
    logging.info(f"Starting port scanning on {target} range({strt,final})")
    for port in range(strt,final + 1):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.01)
        try:
            result = sock.connect_ex((target,port))
            if result == 0:
                logging.info(f"SCANNER: Port {port} is open")
            sock.close()
        except socket.error as e:
            logging.error(f"could not connect to {target}: {e}")
    print("=" * 50)
    logging.info(f"Port Scanning for {target} done")