import mmh3
import requests
import sys


if len(sys.argv) < 2:
	print("Example: ./favicon.py http://server/favicon.ico")
	sys.exit()

url = sys.argv[1]
req = requests.get(url, verify=False)
favicon = req.content.encode('base64')
hash = mmh3.hash(favicon)
print("http.favicon.hash:"+str(hash))