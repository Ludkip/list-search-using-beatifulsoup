# importing the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.worldathletics.org/records/all-time-toplists/jumps/pole-vault/outdoor/men/senior?regionType=world&page=1&bestResultsOnly=true&firstDay=1900-01-01&lastDay=2022-07-11"
#seasonbest url = "https://www.worldathletics.org/records/toplists/jumps/pole-vault/outdoor/men/senior/2022?regionType=world&page=1&bestResultsOnly=true"
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
tables = pd.read_html(html_content)
info = tables[0]

name = input("Last name of vaulter (if brothers: include first name) Limit 5.82 outdoors:   ")
a = info['Competitor'].str.contains(name, na=False, case=False)


p = 0
for i in a:
    if i == True:
        wanted_nr = p
        break
        
    p = p+1
    
if p == 100:
    print ('Did not find', name, 'in top 100 outdoors')  

else:
    print('The outdoor PB of', info['Competitor'][wanted_nr], 'is', info['Mark'][wanted_nr], 'meters.')


#wanted = info[info['Competitor']==name]
#print(wanted['Mark'][0])