# Search for a framwork by favicon

## Usage

```
git clone https://github.com/phor3nsic/favicon_hash_shodan.git
cd favicon_hash_shoda
pip2 install -r requirements.txt
python2 favicon.py http://server/favicon.ico
```
**Example result**:

```
http.favicon.hash:657337228
```

- Search in Shodan:

[/search?query=http.favicon.hash:657337228](https://www.shodan.io/search?query=http.favicon.hash%3A657337228)