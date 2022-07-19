from bs4 import BeautifulSoup
import urllib.request as ur
from html_table_parser import HTMLTableParser

# Collect tables from a web-page
def webtables(target_url, disc=True):
    
    if disc == True:
        print("Need improvements -> user-rotation")
        # User-rotation not implemented yet
        
    headers = {'User-Agent': 'okay'} # Some user-agent name
    try:
        req = ur.Request(url=target_url) # Without headers
        f = ur.urlopen(req)
        xhtml = f.read().decode('utf-8')
        p = HTMLTableParser()
        p.feed(xhtml) 
    
    except:
        req = ur.Request(url=target_url,headers=headers)
        f = ur.urlopen(req)
        xhtml = f.read().decode('utf-8')
        p = HTMLTableParser()
        p.feed(xhtml)
    
    return p.tables
