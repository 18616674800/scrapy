#/usr/bin/python
from urllib import request
from lxml import etree
from selenium import webdriver
import time




#url = "https://so.m.jd.com/category/all.html"
url = "http://m.muyingzhijia.com/activity/activepage?id=1597"
browser = webdriver.PhantomJS(executable_path='/Library/Python/2.7/site-packages/phantomjs')
browser.get(url)
time.sleep(3)



html = browser.execute_script("return document.documentElement.outerHTML")
fp = open("test.html",'w')
fp.write(html)
fp.close()
#soup = BeautifulSoup(html, "lxml")

#print(soup.a)
