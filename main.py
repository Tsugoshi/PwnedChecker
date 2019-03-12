import hashlib as hl
import requests
import sys

def main():
    password = sys.argv[1]
    sha1 = hl.sha1(password.encode()).hexdigest()
    r=requests.get("https://api.pwnedpasswords.com/range/"+sha1[0:5])
    print (r.status_code)
    print (r._content)

if __name__ == "__main__":
    main()
