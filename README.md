# Search for a framework by favicon

__Get all hosts with the same favicon!__

### Install

```bash
pipx install git+https://github.com/phor3nsic/favicon_hash_shodan.git
```

### Usage

#### Simple use:
```bash
favhash -u https://github.com/favicon.ico
```

> Example to https://github.com/favicon.ico
```bash
~$ favhash -u https://hackerone.com/favicon.ico
[+] http.favicon.hash:1848946384
[+] View Results:> 
https://www.shodan.io/search?query=http.favicon.hash%3A1848946384
```

#### [Uncover](https://github.com/projectdiscovery/uncover) mode

```bash
favhash -u https://github.com/favicon.ico --uncover
```

### Search example

[/search?query=http.favicon.hash:3A595148549](https://www.shodan.io/search?query=http.favicon.hash%3A595148549)

<a href="https://www.buymeacoffee.com/phor3nsic" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
