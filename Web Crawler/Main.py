import requests
import calendar
import datetime
import os
from bs4 import BeautifulSoup
import urllib
import re
import time

base_url = 'https://www.stpauls.com/sitemap.html'


'''def getDays():
    date = datetime.date.today()
    date_re = re.findall('-(\d\d)-', str(date))
    date_re = str(date_re).rstrip('\'\]')
    date_re = date_re.lstrip('\[\'')
    month = int(date_re)
    monthAbbr = calendar.month_abbr[month]
    print monthAbbr
    cal = calendar.Calendar(6)
    weekList = cal.monthdatescalendar(int(time.strftime('%Y')), int(time.strftime('%m')))
    return weekList'''


def getSiteMap():
    html = requests.get(base_url).content
    return html


def parseSitemap(html):
    soup = BeautifulSoup(html, "html.parser")
    table = BeautifulSoup.find_all(soup, 'td')
    linkList = []
    for tag in table:
        if re.search('post', str(tag)):
            linkList.append(tag)

    re1 = '.*?'  # Non-greedy match on filler
    '.*
    re2 = '((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3})))(?![\\d])'  # Year 1
    re3 =?'  # Non-greedy match on filler
    re4 = '((?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'  # Day 1

    dateList = []
    for tag in linkList:
        dateList.append(re.findall(re1+re2+re3+re4, str(tag)))
    dateList.sort(reverse=True)
    for tag in linkList:
        if dateList[0][0][0] + '-' + dateList[0][0][1] in str(tag):
            mostRecentSite = tag


    soup = BeautifulSoup(str(mostRecentSite), "html.parser")
    soup = soup.a
    final_site = soup['href']
    return final_site


def getPDF(link):
    os.chdir('C:' + os.getenv('HOMEPATH') + '\\Desktop')
    urllib.urlretrieve(link, 'Newsletter.pdf')

'''osenv = os.getenv('HOMEPATH')
    os.chdir('C:' + osenv + '\\Desktop')
    file2 = open('test2.txt', 'w')
    file2.write(str(soup))'''

try:
    parseSitemap(getSiteMap())
except AttributeError as e:
    print "Unfortunately, this program does not keep track of all holidays that the school follows, so the newsletter cannot be downloaded"
    print e



