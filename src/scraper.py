# TBD
import urllib
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup


url='https://www.google.com/search?q=嗎知乎'

opt = Options() 
opt.add_argument('--headless')
opt.add_argument('start-maximized')
opt.add_argument('--disable-gpu')
browser = webdriver.Firefox(opt)

f = open(r'rawtext\google.txt', 'a', encoding='utf-8')

browser.get(url)
soup = BeautifulSoup(browser.page_source, 'html.parser')


for tag in soup.find_all('a'):
    if ('data-sb' in tag.attrs) and ('data-ved' in tag.attrs):
        try:
            l = str(urllib.parse.unquote(tag.get('href')))
            if re.search(u'[\u4e00-\u9fff]+', l) == None:
                pass
            else:
                text = str(re.split('=|/', l)[-1])
                print(text)
                f.write(text)
                f.write('\n')
        except:
            pass
        

f.close()