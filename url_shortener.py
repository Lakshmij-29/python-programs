import random, string

urls = {}

def shorten(url):
    code = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    urls[code] = url
    return code

long_url = input("Enter URL: ")
short = shorten(long_url)
print("Short code:", short)