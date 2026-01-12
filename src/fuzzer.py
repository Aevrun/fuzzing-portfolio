
import time
import requests
import logging
from src.crawler import LOG_DIR

LOG_FILE = LOG_DIR / "fuzzer.log"
print("LOG_FILE is:", LOG_FILE.resolve())
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ], force=True
)

def run_fuzzer(url: str, wordlist: str, extension: str) -> None:
    print("=" * 50)
    print(f"Running fuzzer on: {url}")
    url = url.rstrip('/')
    findings = 0
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        with open(wordlist,'r') as file:
            for line in file:
                word = line.strip()
                target_paths = [word]
                if extension:
                    ext_list = extension.split(',')
                    for ext in ext_list:
                        clean_ext = ext.lstrip('.')
                        target_paths.append(f"{word}.{clean_ext}")
                for path in target_paths:
                    time.sleep(0.1)
                    final_url = f"{url}/{path}"
                    try:                    # spacing to clear out the previous word
                        print(f"[*] Testing: {path}         ",end="\r")
                        response = requests.get(final_url,headers=headers,timeout=2)
                        feedback = response.status_code
                        if feedback != 404:
                            findings += 1
                            logging.info(f"[{response.status_code}] Found: {final_url}")
                            with open("fuzz_results.txt", "a") as f:
                                f.write(f"{feedback} Found: {final_url}\n")
                    except requests.exceptions.RequestException:
                        continue
    except FileNotFoundError:
        logging.error(f"[!]ERROR: Wordlist {wordlist} not found.")
    logging.info(f"[!] Link found: {findings}")
    print("=" * 50)