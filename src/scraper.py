import requests 
import json 
from time import sleep


def scrape(url):    
    headers = {
        'authority': 'www.yahoo.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # scrape the page using requests
    print("Scraping {}".format(url))
    r = requests.get(url, headers=headers)
    # check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Yahoo data please contact" in r.text:
            print("Page {} was blocked by Yahoo. Please try using better proxies".format(url))
        else:
            print("Page {} must have been blocked by Yahoo as the status code was {}".format(url,r.status_code))
        return None
    # pass the HTML of the page 
    return r.text


def run(url):
    with open('logs/output.html','w') as outfile:
        data = scrape(url) 
        if data:
            outfile.write(data)


if __name__ == "__main__":
    # Here we just scrape CRM page as an example
    # by the end of this you will get the page content in logs folder
    url = "https://finance.yahoo.com/quote/CRM/"
    run(url)
