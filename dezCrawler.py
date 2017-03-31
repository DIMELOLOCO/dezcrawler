#Using BeautifulSoup soup and requests create a bot views pages
#insert functionality to download pictures as it visits the pages.
#add functionality to create a log of sites visited, and sites it still needs
#to visit
#add functionality to create save images out so that they are searchable
#scrape all images from designboom is the goal.
from io import StringIO
import collections
import argparse, os, time, random
import urllib.request
from urllib.parse import urlparse
import bs4 as bs
import csv
from sys import argv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
"""
#retrieve page data
def make_soup(url):
    #specify the url
    r = urllib.request.urlopen(url).read()
    soupdata = BeautifulSoup(r, 'lxml')
    return soupdata
"""

#create a json database file
dict_main = {
    'project_id' : " ",
    'information': {
        'title': " ",
        'author': " ",
        'date': " "
    },
    'images': {
        'h_links': [],
        'f_loc': []
    },
    'content': {
        'text': " ",
        'tags': " "
    }
}

#retrieve project links from page return list of links
def getProjectLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            for i in range(1998,2019):
                if '/{}/'.format(i) in url:
                    links.append(url)
    return links

#retrieve nav links from page return list of links
def getPagesLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if '/page/' in url: #redo this to include all years
                links.append(url)
    return links
#parse the id so that only the path is captured
def getID(url):
    link = urlparse(url)
    return (link[2])

#save information out to csv. optional as of now
def outputLink (save, out, write):
    print ("File saved!")
    with open(out, write) as f:
        f.write(save)

def csvToList(in):
    with open(in, 'rb') as f:
        reader = csv.reader(f)
        pList=list(reader)
        return pList

def proj_title(s):
    return(s.main.h1.text)

def proj_date(s):
    return(s.article.time.a.text)

def find_section(s):
    par = s.section.find_all('p')
    paragraph = []
    for each in par:
        if each.string != None:
            paragraph.append(each.text)
    return paragraph

def imagegroup(s):
    img = s.find_all('figure')
    imagelist = []
    for link in img:
        im = link.get('data-lightboximage')
        if im != None:
            imagelist.append(im)
    return imagelist

def websiteToJSON (url, dic):
    dic['information']['title'] = proj_title(url)
    dic['information']['date'] = proj_date(url)
    dic['content']['text'] = find_section(url)
    dic['images']['h_links'] = imagegroup(url)
    return json.dumps(dic, indent = 4, sort_keys = True)


#define the bot that will view the sites
def ViewBot(browser):
    visited = {} #dict automatically overwrites duplicates. used for comparison
    pList = [] #holds links captured
    count = 0 #used for forloops
    #load webpage

    while True:
        #time.sleep(random.uniform(4.5,8.5)) #pauses the code so page can load, and to appear more human
        p = BeautifulSoup(browser.page_source, 'lxml') #parses the current page's source
        #if page is a project link then take all of the information.
        pd = websiteToJSON(url, dict_main)
        outputLink(pd, "test_dict.json", "a+")
        projects = getProjectLinks(p) #list of 'pages' links
        if projects:
            for project in projects:
                ID = getID(project)
                if ID not in visited: #compare to dict
                    pList.append(project)
                    visited[ID] = 1
                    outputLink("\n{},", output, 'a+').format(project)
                    savedProj.append(project)
        if pList:
            project = pList.pop()
            browser.get(project)
            count +=1
        else:
            archives = getPagesLinks(p)
            if archives:
                archive = random.choice(archives)
                root = 'https://www.dezeen.com'
            if root not in archive:
                archive = root + archive
                browser.get(archive)
            else:
                print ("I'm Lost. Exiting")
                break
        print ("[+]" + browser.title + " Visited! \n ("\
            +str(count) + "/" + str(len(pList)) + ") Visited/Queue")

#where everything goes down
def Main():
    output = 'outputID.txt'
    browser = webdriver.Chrome()
    browser.get("https://www.dezeen.com/architecture/")
    #clear command line windows
    clear = lambda: os.system('cls')
    clear()
    print ("[+] Success! I'm in! Bot Starting!")
    savedProj = csvToList(output)
    ViewBot(browser)
    browser.close()
    #print(main_text)
    #log information to file
    #outputText(soup.main.text)

    #log links into file
    #outputLink(link.get('href'))

if __name__ == '__main__':
    Main()
