url = input("Enter URL: ")

if url.startswith("https://"):
    url = url.replace("https://", "")
elif url.startswith("http://"):
    url = url.replace("http://", "")

url = url.strip("/")

print("Clean URL:", url)

if "." in url:
    print("Domain detected")
