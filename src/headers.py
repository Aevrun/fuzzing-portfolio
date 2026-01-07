import requests

url = input("HEADER TESTING: Enter the url:")

try:
    response = requests.get(url)
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