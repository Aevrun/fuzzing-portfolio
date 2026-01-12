import os.path

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

BASEDIR = os.path.dirname(os.path.abspath(__file__))
error_list = os.path.join(BASEDIR,"sql_error.txt")


def check_sqli(url, parameter_name) -> None:
    cleaned_url = url.rstrip("/")
    separator = "?" if "?" not in cleaned_url else "&"
    payload = "'"
    final_url = f"{cleaned_url}{separator}{parameter_name}={payload}"
    try:
        print(f"[*] Probing for SQLi on: {parameter_name}...")
        response = requests.get(final_url,headers=headers,timeout=2)
        with open(error_list,"r") as file:
            for error in file:
                clean_error = error.strip()
                if clean_error.lower() in response.text.lower():
                    print(f"[!!] ALERT: database vulnerability: {final_url}")
                    return
    except requests.exceptions.RequestException:
        print(f"[!] ERROR: could not connect to {url}")
