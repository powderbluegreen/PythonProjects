import requests
import calendar
import datetime
import os
from bs4 import BeautifulSoup
import urllib
import re



def getDays():
    date = datetime.date.today()
    date_re = re.findall('-(\d\d)-', str(date))
    date_re = str(date_re).rstrip('\'\]')
    date_re = date_re.lstrip('\[\'')
    month = int(date_re)
    monthAbbr = calendar.month_abbr[month]
    print monthAbbr


''' def getUrl():
    base_url = 'https://www.stpauls.com/weekly-newsletter-for-'
    html = requests.get(base_url).content
    return html


def parseHtml(html):
    soup = BeautifulSoup(html, "html.parser")
    divPost = soup.find('div', class_="post")
    divPost_p = divPost.find('p')
    divPost_pa = divPost_p.find('a')
    link = divPost_pa['href']
    return link


def getPDF(link):
    os.chdir('C:' + os.getenv('HOMEPATH') + '\\Desktop')
    urllib.urlretrieve(link, 'Newsletter.pdf')
'''

'''osenv = os.getenv('HOMEPATH')
    os.chdir('C:' + osenv + '\\Desktop')
    file2 = open('test2.txt', 'w')
    file2.write(str(soup))'''





# getPDF(parseHtml(getUrl()))
getDays()