import mmh3
import requests
import codecs
import argparse

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
	parser = argparse.ArgumentParser(add_help=True)
	parser.add_argument('-u', '--url', help='Url to get favicon hash Ex: https://example.com/favicon.ico', required=True)
	parser.add_argument('--uncover', action='store_true', help='Uncover output mode github.com/projectdiscovery/uncover')
	arg = parser.parse_args()

	response = requests.get(arg.url, verify=False)
	favicon = codecs.encode(response.content,"base64")
	hash_favicon = mmh3.hash(favicon)
	
	if arg.uncover:
		print(f'http.favicon.hash:{str(hash_favicon)}') 
	else:
		print(f"""
[+] http.favicon.hash:{str(hash_favicon)}
[+] View Results:> 
https://www.shodan.io/search?query=http.favicon.hash%3A{str(hash_favicon)}""")

