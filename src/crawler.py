from pathlib import Path

from bs4 import BeautifulSoup
import requests
import logging

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "crawler.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def run_crawler(url: str) -> list:
    interesting_keywords = ["admin", "login", "upload", "config"]
    print("=" * 50)
    discovered_links = []
    logging.info("Starting crawl for URL: %s", url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            logging.info(f"Following links were scraped from the site({url}):")
            for link in links:
                href  = link.get('href')
                logging.info(f"FOUND:{href}")
                discovered_links.append(href)
                if href:
                    for each in interesting_keywords:
                        if each in href:
                            print(f"[!]IMPORTANT: {link.get('href')}")
                            logging.info(f"[!]IMPORTANT: {link.get('href')}")
                            break
    except requests.exceptions.RequestException:
        print(f"[!] ERROR: unable to connect to the url: {url}")
        logging.error(f"[!] ERROR: unable to connect to the url: {url}")
    print("=" * 50)
    return discovered_links