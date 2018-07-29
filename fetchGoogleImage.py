#!/usr/bin/python3

import sys, re, os, urllib
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys

driver_path = os.environ["WEBDRIVER_PATH"]

def getImageURLs(driver, query):
        driver.get('https://www.google.co.jp/search?q=%s&tbm=isch'% query)
        pattern = '"ou":"(.*?)"'
        src=driver.page_source
        urls=re.findall(pattern, src)
        return urls

def downloadImage(url, path):
        try:
                folder = os.path.dirname(path)
                if not os.path.exists(folder):
                        os.makedirs(folder)
                with urllib.request.urlopen(url) as response:
                        maintype = response.info().get_content_maintype()
                        subtype = response.info().get_content_subtype()
                        data = response.read()
                        with open("{path}.{subtype}".format(path=path,subtype=subtype), mode="wb") as f:
                                f.write(data)
        except urllib.error.URLError as e:
                print(e)
        except UnicodeEncodeError as e:
                print(e)
                
if __name__ == '__main__':
        args = sys.argv
        if len(args) != 3 :
                print("Usage: fetchGoogleImage.py <query> <folder>")
                exit(0)
        query=args[1]
        folder=args[2]        

        options = ChromeOptions()
        options.add_argument('--headless')
        driver = Chrome(driver_path, options=options)
        list=getImageURLs(driver=driver, query=query)
        for i,u in enumerate(list):
                print(u)
                downloadImage(u, "{0}/{1:04}".format(folder,i))
        driver.quit() 
            
