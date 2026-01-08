

import requests

def run_fuzzer(url: str, wordlist: str) -> None:
    url = url.rstrip('/')
    findings = 0
    try:
        with open(wordlist,'r') as file:
            for line in file:
                word = line.strip()
                final_url = f"{url}/{word}"
                try:                    # spacing to clear out the previous word
                    print(f"[*] Testing: {word}         ",end="\r")
                    response = requests.get(final_url,timeout=2)
                    feedback = response.status_code
                    if feedback != 404:
                        findings += 1
                        with open("fuzz_results.txt", "a") as f:
                            f.write(f"Found: {final_url}\n")
                except requests.exceptions.RequestException:
                    continue
    except FileNotFoundError:
        print(f"[!]ERROR: Wordlist {wordlist} not found.")
    print()
    print(f"[!] Link found: {findings}")