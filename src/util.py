import logging
import sys
from urllib.parse import urlparse,parse_qs

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("Scanner.log"),
        logging.StreamHandler()
    ]
)

def get_parameters(url):
    """Extracts Parameter names from a URL string"""
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    return list(params.keys())

def port_parser(ports: str) -> tuple[int,int]:
    # Ports error checking
    if '-' in ports:
        split_range = ports.split('-')
        try:
            start = int(split_range[0])
            end = int(split_range[1])
            return start,end
        except ValueError:
            logging.error("Invalid port format. Use numbers or 'start-end")
            sys.exit()
    else:
        try:
            start = int(ports)
            end = int(ports)
            return start,end
        except ValueError:
            logging.error("Invalid port format. Use numbers or 'start-end")
            sys.exit()