import requests
res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
type(res)
print(res.status_code == requests.codes.ok)
print(res.text[:200])