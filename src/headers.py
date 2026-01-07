import argparse
import logging

import requests


def run_header_tester(link: str) -> None:
        try:
            response = requests.get(link)
            code  = response.status_code
            if code == 200:
                header = response.headers
                print(header.get('Server'))

                security_check = ['X-Frame-Options', 'Content-Security-Policy', 'Strict-Transport-Security']

                for each in security_check:
                    if each not in header:
                        print("=" * 30)
                        print(f"WARNING! {each} is missing in the Header")
                        print("=" * 30)

        except requests.exceptions.RequestException:
            print("=" * 30)
            print("[!] ERROR: could not connect to the target")
            print("=" * 30)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Header Tester")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('headers.log'),
            logging.StreamHandler()
        ]
    )

    parser.add_argument('-l','--link',required=True,help="Header Testing, simply enter the url of the website you want to check (eg. https://www.google.com)")
    args = parser.parse_args()
    url = args.link
    run_header_tester(url)
