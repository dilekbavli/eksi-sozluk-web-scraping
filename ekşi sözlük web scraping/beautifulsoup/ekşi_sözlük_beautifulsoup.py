#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:08:49 2021

@author: dilekcay
"""
from bs4 import BeautifulSoup 
import requests
import random
import time


headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"}
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
r = requests.get(url, headers = headers)
print(r) #response 200 dönerse devamke

soup = BeautifulSoup(r.content, "html.parser")
pageCount = 1
entries = []
entryCount = 1
while pageCount <=10:
    randomPage = random.randint(1, 1290)
    newUrl = url + str(randomPage)
    soup.get(newUrl)
    elements = soup.find_all("div", attrs = {"class":"content"})
    for element in elements:
        entries.append(element.text)
    time.sleep(2)
    pageCount += 1


with open("entries.txt", "w", encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("***************\n")
        entryCount += 1
