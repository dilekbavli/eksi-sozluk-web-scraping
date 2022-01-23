# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 23:50:54 2022

@author: Dilek
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 09:43:11 2021

@author: dilekcay
"""

#!pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
import random 



s=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s)
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
# browser.get(url)
browser.maximize_window()

time.sleep(3)
pageCount = 1
entries = []
entryCount = 1

while pageCount <=10:
    randomPage = random.randint(1, 1290)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(2)
    pageCount += 1

    
with open("entries.json", "w", encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("***************\n")
        entryCount += 1
        
browser.close()
