#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 02:44:19 2018

@author: nomdebrew
"""

import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup

url = input('Enter a url - ex: https://en.wikipedia.org/wiki/Austin_Lucas (Y to use default) ') #allows user to enter a url
#url = 'https://en.wikipedia.org/wiki/Austin_Lucas'  #used for testing
if url == "y" or url == "Y" :
    url = "https://en.wikipedia.org/wiki/Austin_Lucas"

print('\nBelow is the output for page:',url,"\n")

print("\nUsing Regular Expressions\n")

link_count = 0

fhand = urllib.request.urlopen(url)
for line in fhand:
    line = line.decode().strip()
    match = re.findall('href="[^#].*?(?=")', line)
    if match:
        for i in match:
            print(i)
            link_count +=1

print("\nTotal # of links:",link_count)





print("\n\nUsing BeautifulSoup\n")

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup ('a')  # retrive all of the anchor tags
print(len(tags)) #prints lenght of tag list
for tag in tags:
    print(tag.get('href', None)) #https://en.wikipedia.org/wiki/Austin_Lucas