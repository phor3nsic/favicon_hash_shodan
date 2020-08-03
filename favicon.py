import mmh3
import requests
import sys
import urllib3
urllib3.disable_warnings()


if len(sys.argv) < 2:
	print("Example: ./favicon.py http://server/favicon.ico")
	sys.exit()

url = sys.argv[1]
req = requests.get(url, verify=False)
result = req.content.encode('base64')
favicon= str(mmh3.hash(result))
print("[!]http.favicon.hash:"+favicon)
print("[*]View Results:\nhttps://www.shodan.io/search?query=http.favicon.hash%3A"+favicon)