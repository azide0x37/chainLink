
"""
chainLink.py 
Mines data from the offender search provided by the Missouri Department of Corrections website.
[azide0x37] Alexander Templeton (nepenthe.me)

Arguments:
Returns: pandas Data.Frame object
"""

import urllib2
import pandas as pd
from collections import OrderedDict
from datetime import datetime

class chainLink:
  def __init__(self, url = https://web.mo.gov/doc/offSearchWeb/searchOffender.do, selectors = 'docId'):
    self.url = url
    self.selectors = selectors
    
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    self.response = opener.open(self.url)
    
    #Set better formatting for testing console print 
    pd.set_option('display.max_rows', 500) 
    pd.set_option('display.max_columns', 500) 
    pd.set_option('display.width', 200) 

  def __str__(self):
    try:
      print self.url, "?", selectors
    except:
      print "Unable to display url"
  
  def __call__(self):
    webpageSouped = BeautifulSoup(self.response.read())
    
    #Strip headings, send to list
    headingTable = webpageSouped.find('table',,)
    headings = headingTable.findAll('td')
    
    dataTable = webpageSouped.find('table', border="0", cellpadding="4", cellspacing="2")
    rows = dataTable.findAll('tr')
    
    dataset = []
    
    for tr in rows:
      cols = OrderedDict()
      counter = 0
      
      for td in cols[1:]:
        text = ''.join(td.find(text=True))
        try:
          headings[counter] = text
          counter += 1
        except:
          counter = 0
          continue
      dataset.append(row_data)
      
    return pd.DataFrame(dataset)
  
#class description
#select search option: default = id number optional = firstName & lastName
#download appropriate page
#beautifulSoup
#return table identifier: <TABLE border="0" cellpadding="4" cellspacing="2" class="displayTable">
#extract data to dataFrame
#return data
myLink = chainLink()
print myLink()
