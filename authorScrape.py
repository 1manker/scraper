#Lucas Manker
#import libraries
import sys
import requests
from bs4 import BeautifulSoup

url = str(sys.argv[1])
req = requests.request("GET", url)

s = req.content

soup = BeautifulSoup(s, 'html.parser')

def printer(arr1, arr2):
    file = open("C:\\Users\\Luke\\Desktop\\output.txt", "w+")
    for x in range(len(arr1)):
        file.write(arr1[x] + "," + arr2[x] + "\n",)

def scrape():
    citRow = []
    authorRow = []
    yearRow = []
    count = 0
    for row in soup.findAll('a', attrs={"class": "gsc_a_ac gs_ibl"}):
        citRow.append(row.text)
    for row in soup.findAll('a', attrs={"class": "gsc_a_at"}):
        authorRow.append(row.text)
    for row in soup.findAll('span', attrs={"class": "gsc_a_h gsc_a_hc gs_ibl"}):
        yearRow.append(row.text)
    printer(citRow, yearRow)

scrape();