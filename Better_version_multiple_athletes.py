# importing the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

nr_list = []
b = 1

url = "https://www.worldathletics.org/records/all-time-toplists/jumps/pole-vault/outdoor/men/senior?regionType=world&page=1&bestResultsOnly=true&firstDay=1900-01-01&lastDay=2022-07-11"
#seasonbest url = "https://www.worldathletics.org/records/toplists/jumps/pole-vault/outdoor/men/senior/2022?regionType=world&page=1&bestResultsOnly=true"
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
tables = pd.read_html(html_content)
info = tables[0]

print("Last name of vaulters (if brothers: include first name) Limit 5.82 outdoors. Write the vaulters with comma inbetween:   ")
names = input().split(',')

for t in names:
    a = info['Competitor'].str.contains(t, na=False, case=False)

    p = 0
    for i in a:
        if i == True:
            nr_list.append(p)
            
            #print('The outdoor PB of', info['Competitor'][wanted_nr], 'is', info['Mark'][wanted_nr], 'meters.')
            break
        p = p+1

nr_list.sort()

print(" ")
print("Your athletes ranked from outdoor pb best to worst:")
print(" ")

for w in nr_list:
    print(b, ' ', info['Mark'][w], info['Competitor'][w])
    b+= 1

print(" ")