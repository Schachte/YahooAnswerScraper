'''
Yahoo Web App that tells you how many answers a single question has
'''

import urllib2
import re
from bs4 import BeautifulSoup

print 'Please enter a link to a yahoo answers web page:'

url = raw_input ('>>')

url_open = urllib2.urlopen(url)

print 'URL opened!'

soup = BeautifulSoup(url_open)

answer_count = soup.find("h3", {"class": 'ya-oa-header'})
title_word = soup.find("h1", {'class': 'subject inline'})

#print answer_count.text
'''
regular_ex = re.compile('(' + (.+?) + ')')
Create a regular expression to extract the numerical digit out of the string then use a string formatter to output properly
'''

s = str(answer_count)

print title_word.text[5:] + "has " + re.search(r".*\((\d)\)", s).group(1) + " answer(s)."
