import string
import time

import requests
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def run_param_fuzzer(url, param_list) -> None:
    base_url = url.rstrip('/')
    response = requests.get(base_url)
    baseline_length = len(response.text)
    target_url = (f"{base_url}?" if "?" not in base_url else f"{base_url}&")
    param1 = random.randrange(1,9999)
    param2 = "".join(random.choice(string.ascii_letters) for _ in range(5))
    target_path = [param1,param2]
    try:
        with open(param_list,'r') as file:
            for word in file:
                time.sleep(0.1)
                clean_word = word.strip()
                for path in target_path:
                    try:
                        print(f"Testing word: {clean_word}           ", end="\r")
                        final_url = f"{target_url}{clean_word}={path}"
                        feedback = requests.get(final_url,headers=headers,timeout=2)
                        new_length = len(feedback.text)
                        if new_length != baseline_length:
                            print(f"Found: {final_url} (Length: {new_length}")
                            with open("Param_fuzzing_result.txt", 'a') as f:
                                f.write(f"Found: {final_url} (Diff: {new_length-baseline_length})\n")
                    except requests.exceptions.RequestException:
                        continue
    except FileNotFoundError:
        print("[!] ERROR: File not found.")

    print("\n[+] Parameter fuzzing complete.")
