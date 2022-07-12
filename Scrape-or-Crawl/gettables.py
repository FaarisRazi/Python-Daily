from bs4 import BeautifulSoup
import urllib.request as ur
from html_table_parser import HTMLTableParser

# Collect tables from a web-page
def webtables(target, disc=True):
    
    
    if disc == True:
        print("Need improvements -> user-rotation")
        
    headers = {'User-Agent': 'okay'}
    try:
        req = ur.Request(url=target)
        f = ur.urlopen(req)
        xhtml = f.read().decode('utf-8')
        p = HTMLTableParser()
        p.feed(xhtml)
        
        return p.tables 
    
    except:
        req = ur.Request(url=target,headers=headers)
        f = ur.urlopen(req)
        xhtml = f.read().decode('utf-8')
        p = HTMLTableParser()
        p.feed(xhtml)
        
        return p.tables
