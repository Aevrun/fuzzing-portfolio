from bs4 import BeautifulSoup
import requests
import logging
import argparse

def run_crawler(url: str) -> None:
    interesting_keywords = ["admin", "login", "upload", "config"]
    # first lets ask the user for the url
    print("=" * 30)
    #url = input("Please enter the url you want to crawl:")

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            print(f"Following links were scraped from the site({url}):")
            for link in links:
                href  = link.get('href')
                print(f"FOUND:{href}")
                if href:
                    for each in interesting_keywords:
                        if each in href:
                            print(f"[!]IMPORTANT: {link.get('href')}")
                            break
    except requests.exceptions.RequestException:
        print(f"[!] ERROR: unable to connect to the url: {url}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Web Crawler to find links")

    parser.add_argument('-l','--link', required=True, help='Link to the website to crawl (eg. https://www.google.com)')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("Crawler.log"),
            logging.StreamHandler()
        ]
    )

    args = parser.parse_args()
    run_crawler(args.link)