#Lucas Manker
# import libraries
import requests
from bs4 import BeautifulSoup

url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C51&q=lung+cancer&btnG="
req = requests.request("GET", url)

s = req.content

soup = BeautifulSoup(s, 'html.parser')

rawAuthor = []
for row in soup.findAll('div', attrs={"class": "gs_a"}):
    rawAuthor.append(row.text)

authors = []
for x in range(len(rawAuthor)):
    authors.append(rawAuthor[x].split("-"))

authorsClean = []
separator = '\\'
for x in range(len(authors)):
    temp = authors[x][0].split(separator)
    authorsClean.append(temp[0])


rawCited = []
for row in soup.findAll('a'):
    rawCited.append(row.text)

cited = [s for s in rawCited if "Cited" in s]

combined = []

for x in range(len(authorsClean)):
    temp = authorsClean[x];
    temp += cited[x]
    combined.append(temp)

#data-clk-atid


titleRaw = []
for link in soup.findAll('a'):
    titleRaw.append(link)

titleString = []
for x in range(len(titleRaw)):
    titleString.append(str(titleRaw[x]))

titleRawer = [s for s in titleString if "<a data-clk" in s and "span" not in s]

titleNarrow = []
for x in range(len(titleRawer)):
    temp = titleRawer[x].split("id")
    titleNarrow.append(temp[2])

titleNarrower = []
for x in range(len(titleNarrow)):
    temp = titleNarrow[x].split("\">")
    titleNarrower.append(temp[1])

completedTitle = []
for x in range(len(titleNarrower)):
    temp1 = titleNarrower[x].replace("<a>", "")
    temp2 = temp1.replace("</a>", "")
    temp3 = temp2.replace("<b>", "")
    temp4 = temp3.replace("</b>", "")
    completedTitle.append(temp4)

finished = []
for x in range(len(completedTitle)):
    temp = authorsClean[x]
    temp += completedTitle[x]
    temp += " "
    temp += cited[x]
    temp += '\n'

    finished.append(temp)

file = open("C:\\Users\\Luke\\Desktop\\output.txt", "w+")
for x in range(len(finished)):
    file.write(finished[x],)

file.close()



