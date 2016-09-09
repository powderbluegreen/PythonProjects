import requests
import calendar
import datetime
import os
from bs4 import BeautifulSoup
import urllib
import re
import time
from types import NoneType

base_url = 'https://www.stpauls.com/sitemap.html'
test_url = 'https://www.stpauls.com/sitemap-pt-post-2016-08.html'


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


def getUrl(url):
    html = requests.get(url).content
    return html


def parseSitemap(html):
    soup = BeautifulSoup(html, "html.parser")
    table = BeautifulSoup.find_all(soup, 'td')
    linkList = []
    for tag in table:
        if re.search('post', str(tag)):
            linkList.append(tag)

    re1 = '.*?'  # Non-greedy match on filler
    re2 = '((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3})))(?![\\d])'  # Year 1
    re3 = '.*?'  # Non-greedy match on filler
    re4 = '((?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'  # Day 1

    dateList = []
    for tag in linkList:
        dateList.append(re.findall(re1+re2+re3+re4, str(tag)))
    dateList.sort(reverse=True)
    for tag in linkList:
        if dateList[0][0][0] + '-' + dateList[0][0][1] in str(tag):
            mostRecentSite = tag
            break

    soup = BeautifulSoup(str(mostRecentSite), "html.parser")
    soup = soup.a
    final_site = soup['href']
    print final_site
    return final_site


def parseSitemapSecond(html):
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.find_all('td')
    linkList = []
    for tag in soup:
        linkList.append(tag.a)
    for tag in linkList:
        if type(tag) == NoneType:
            linkList.remove(tag)
    linkListNewsletter = []
    for tag in linkList:
        if 'newsletter' in str(tag):
            linkListNewsletter.append(tag)
    final_site = linkListNewsletter[0]['href']
    print final_site
    return final_site


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

'''osenv = os.getenv('HOMEPATH')
    os.chdir('C:' + osenv + '\\Desktop')
    file2 = open('test2.txt', 'w')
    file2.write(str(soup))'''

try:
    getPDF(parseHtml(getUrl(parseSitemapSecond(getUrl(parseSitemap(getUrl(base_url)))))))
except AttributeError as e:
    print "Unfortunately, this program does not keep track of all holidays that the school follows, so the newsletter cannot be downloaded"
    print e