import argparse
import logging
import os

from src.crawler import run_crawler
from src.fuzzer import run_fuzzer
from src.headers import run_header_tester
from src.param_fuzzer import run_param_fuzzer
from src.scanner import run_scanner
from src.util import port_parser
from src.xss_scanner import check_xss
from src.sqli_scanner import check_sqli
from src.util import get_parameters

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Parameter_path = os.path.join(BASE_DIR,"params.txt")

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
    fuzz_parser.add_argument("-e","--extension",default="")

    # Param_fuzz command
    param_fuzz_parser = subparser.add_parser("param_fuzz",help="fuzz parameter on server")
    param_fuzz_parser.add_argument('-u','--url',required=True)
    param_fuzz_parser.add_argument("-w","--wordlist",required=True)

    # automation
    auto_parser = subparser.add_parser("auto",help="Automatically crawl links and fuzz them")
    auto_parser.add_argument("-u","--url",required=True)


    # xss
    xss_parser = subparser.add_parser("xss",help="XSS scanner")
    xss_parser.add_argument("-u","--url",required=True)
    xss_parser.add_argument("-p","--parameter",required=True)

    # sqli
    sqli_parser = subparser.add_parser("sqli", help="SQL vulnerabilities scanner")
    sqli_parser.add_argument("-u","--url",required=True)
    sqli_parser.add_argument("-p","--parameter",required=True)

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
        run_fuzzer(args.url,args.wordlist,args.extension)
    elif args.command == "param_fuzz":
        run_param_fuzzer(args.url,args.wordlist)
    elif args.command == "auto":
        unique_links = set(run_crawler(args.url))

        with open(Parameter_path,"r") as file:
            wordlist_params = [line.strip() for line in file if line.strip()]

        for link in unique_links:
            if not link or not isinstance(link,str):
                continue
            if link.startswith(("mailto:","javascript:","#")):
                continue
            if not link.startswith("http"):
                full_target = args.url.rstrip("/") + "/" + link.lstrip("/")
            else:
                full_target = link
            if args.url in full_target:
                #if "?" in full_target or ".php" in full_target:
                    #print(f"\n[+] Auto-Starting Fuzzer on: {full_target}")
                    #run_param_fuzzer(full_target,Parameter_path)

                discovered_params = get_parameters(full_target)
                if discovered_params:
                    for p in discovered_params:
                        print(f"[!] Testing discovered parameter: {p}")
                        check_xss(full_target,p)
                        check_sqli(full_target,p)
                if ".php" in full_target:
                    print(f"\n[*] Brute-forcing parameters from wordlist on: {full_target}")
                    # We only take the top 5-10 to keep it fast, or the whole list
                    for p in wordlist_params[:10]:
                        check_xss(full_target, p)
                        check_sqli(full_target, p)
                else:
                    check_xss(full_target,"searchFor")
                    check_sqli(full_target, "id")
    elif args.command == "xss":
        check_xss(args.url, args.parameter)
    elif args.command == "sqli":
        check_sqli(args.url, args.parameter)

if __name__ == "__main__":
    main()
