#!/usr/bin/python3

import sys, re, os, urllib, urllib.request
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys

driver_path = os.environ["WEBDRIVER_PATH"]

def getImageURLs(driver, query):
        driver.get('https://www.google.co.jp/search?q=%s&tbm=isch'% query)
        for i in range(1,3):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(5)

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
        except :
                import traceback
                traceback.print_exc()

                
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
        print("-------- Image URL to be fetched ---------")
        for v in list:
                print(v)
        print("------------------------------------------")



        for i,url in enumerate(list):
                print("[{}] Download: {}".format(i, url))
                downloadImage(url, "{0}/{1:04}".format(folder,i))
                print("")
        driver.quit() 
            
