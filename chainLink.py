
"""
mshpScraper.py 
Missouri State Highway Patrol scraper for crash data!
[azide0x37] Alexander Templeton (nepenthe.me)
Arguments:
Returns: pandas Data.Frame object
""
import urllib2
import pandas as pd
from collections import OrderedDict
from datetime import datetime

url = https://web.mo.gov/doc/offSearchWeb/searchOffender.do
selectors = {firstName = 'firstName', lastName = 'lastName', offenderId = 'docId'}

#class description
#select search option: default = id number optional = firstName & lastName
#download appropriate page
#beautifulSoup
#return table identifier: <TABLE border="0" cellpadding="4" cellspacing="2" class="displayTable">
#extract data to dataFrame
#return data
