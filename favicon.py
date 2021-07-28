import mmh3
import requests
import codecs
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if len(sys.argv) < 2:
	print("[!] Error!")
	print(f"[-] Use: python3 {sys.argv[0]} http://example.com/favicon.ico")
	print("[i] Get all hosts with the same favicon!")
	sys.exit()

def main():
	response = requests.get(sys.argv[1], verify=False)
	favicon = codecs.encode(response.content,"base64")
	hash_favicon = mmh3.hash(favicon)

	print("[!] http.favicon.hash:"+str(hash_favicon))
	print("[*] View Results:\n> https://www.shodan.io/search?query=http.favicon.hash%3A"+str(hash_favicon))

if __name__ == '__main__':
	main()