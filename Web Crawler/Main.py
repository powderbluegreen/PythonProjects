import requests
import calendar
import datetime
import os
from bs4 import BeautifulSoup
import urllib
import re
import time

base_url = 'https://www.stpauls.com/weekly-newsletter-for-'
def getDays():
    '''date = datetime.date.today()
    date_re = re.findall('-(\d\d)-', str(date))
    date_re = str(date_re).rstrip('\'\]')
    date_re = date_re.lstrip('\[\'')
    month = int(date_re)
    monthAbbr = calendar.month_abbr[month]
    print monthAbbr'''
    cal = calendar.Calendar(6)
    weekList = cal.monthdatescalendar(int(time.strftime('%Y')), int(time.strftime('%m')))
    return weekList


def getUrl(month, day, month2, day2):
    if len(day) == 1:
        day = day.zfill(2)
    if len(day2) == 1:
        day2 = day2.zfill(2)
    if month == month2:
        final_url = base_url + str(calendar.month_abbr[int(month)]).lower() + '-' + day + '-' + day2 + '\\'
    else:
        final_url = base_url + str(calendar.month_abbr[int(month)]).lower() + '-' + day + '-' + \
                               str(calendar.month_abbr[int(month2)]).lower() + '-' + day2 + '/'
    html = requests.get(final_url).content
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

'''osenv = os.getenv('HOMEPATH')
    os.chdir('C:' + osenv + '\\Desktop')
    file2 = open('test2.txt', 'w')
    file2.write(str(soup))'''


weekList = getDays()
try:
    getPDF(parseHtml(getUrl(str(weekList[0][0].month), str(weekList[0][1].day),
    str(weekList[0][6].month), str(weekList[0][7].day))))
except AttributeError as e:
    print "Unfortunately, this program does not keep track of all holidays that the school follows, so the newsletter cannot be downloaded"
    print e



