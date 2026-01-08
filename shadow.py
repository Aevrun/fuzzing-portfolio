import argparse
import logging

from src.crawler import run_crawler
from src.fuzzer import run_fuzzer
from src.headers import run_header_tester
from src.scanner import run_scanner
from src.util import port_parser

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s',
    handlers=[
        logging.FileHandler("Shadow_toolkit.log"),
        logging.StreamHandler()
    ]
)

def main():
    parser = argparse.ArgumentParser(description="Shadow Toolkit - Week 1 Security Suite")
    subparser = parser.add_subparsers(dest="command", required=True, help="Available Tools")

    # Scanner command
    scan_parser = subparser.add_parser("scan", help="TCP Port Scanner")
    scan_parser.add_argument("-t","--target",required=True)
    scan_parser.add_argument("-p","--ports",default="1-1024")

    # Header Command
    header_parser = subparser.add_parser("header", help="HTTP header analyser")
    header_parser.add_argument('-l','--link',required=True)

    # Crawl Command
    crawler_parser = subparser.add_parser("crawl",help="Web link crawler")
    crawler_parser.add_argument("-u","--url",required=True)

    # fuzz command
    fuzz_parser = subparser.add_parser("fuzz",help="Fuzzing server file system")
    fuzz_parser.add_argument("-u","--url",required=True)
    fuzz_parser.add_argument("-w","--wordlist",required=True)

    args = parser.parse_args()

    if args.command == "scan":
        target = args.target
        start,end = port_parser(args.ports)
        run_scanner(target,start,end)
    elif args.command == "header":
        run_header_tester(args.link)
    elif args.command == "crawl":
        run_crawler(args.url)
    elif args.command == "fuzz":
        run_fuzzer(args.url,args.wordlist)

if __name__ == "__main__":
    main()
