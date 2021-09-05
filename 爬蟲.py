# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:27:46 2021

@author: twson
""" 

import requests
from bs4 import BeautifulSoup


response = requests.get(
    "https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("div", itemprop="itemListElement")
print(result.select("a"))
