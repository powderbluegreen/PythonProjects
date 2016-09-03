import requests
import datetime
import os
from bs4 import BeautifulSoup
import re


def getUrl():
    base_url = 'https://www.stpauls.com/weekly-newsletter-for-aug-22-28'
    html = requests.get(base_url).content
    return html


def parseHtml(html):
    soup = BeautifulSoup(html, "html.parser")
    divPost = soup.find('div', class_="post")
    divPost_p = divPost.find('p')
    divPost_pa = divPost_p.find('a')
    link = divPost_pa['href']
    return link

def getPDF():

    '''osenv = os.getenv('HOMEPATH')
    os.chdir('C:' + osenv + '\\Desktop')
    file2 = open('test2.txt', 'w')
    file2.write(str(soup))'''


parseHtml(getUrl())
