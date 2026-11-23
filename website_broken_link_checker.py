import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

website = input("Enter website URL: ")
response = requests.get(website, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
for link in soup.find_all("a", href=True):
    url = urljoin(website, link["href"])
    try:
        result = requests.head(url, timeout=5, allow_redirects=True)
        if result.status_code >= 400:
            print("Broken:", url, result.status_code)
    except requests.RequestException:
        print("Unreachable:", url)
