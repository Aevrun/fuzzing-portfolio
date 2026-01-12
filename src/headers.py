
import requests
import logging

from src.crawler import LOG_DIR

LOG_FILE = LOG_DIR / "Header.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ], force=True
)

def run_header_tester(link: str) -> None:
        try:
            print("=" * 50)
            logging.info(f"Beginning Header Testing for: {link}")
            response = requests.get(link)
            code  = response.status_code
            if code == 200:
                header = response.headers
                print(header.get('Server'))

                security_check = ['X-Frame-Options', 'Content-Security-Policy', 'Strict-Transport-Security']

                for each in security_check:
                    if each not in header:
                        print("=" * 30)
                        logging.info(f"WARNING! {each} is missing in the Header")
                        print("=" * 30)

        except requests.exceptions.RequestException:
            logging.error("[!] ERROR: could not connect to the target")

