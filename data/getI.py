import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import ast
import re
from selenium import webdriver

chromePath=r'/usr/bin/chromedriver'

driver = webdriver.Chrome(chromePath)
URL = 'https://www.google.com/search?safe=active&biw=1299&bih=620&tbm=isch&sa=1&ei=PvOnXZnyJ8mH9QPG9YeYBQ&q=phone&oq=phone&gs_l=img.3...6840.7466..7815...0.0..0.0.0.......0....1..gws-wiz-img.1dPqEepO4q8&ved=0ahUKEwiZifu6v6LlAhXJQ30KHcb6AVMQ4dUDCAc&uact=5'
directory = 'phones'
def getURLs(URL):
	
    driver.get(URL)
    a=input()
    page = driver.page_source
    soup = Soup(page, 'xml')
    #print(soup)
    desiredURLs = soup.findAll('div', {'class':'rg_meta notranslate'})
    print(desiredURLs)
    ourURLs = []

    for url in desiredURLs:
        theURL = url.text
        theURL = ast.literal_eval(theURL)['ou']

        ourURLs.append(theURL)

    return ourURLs


def save_images(URLs, directory):

    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, url in enumerate(URLs):
        savePath = os.path.join(directory, '{:06}.jpg'.format(i))

        try:
            ulib.urlretrieve(url, savePath)

        except:
            print('I failed with', url)

URLs = getURLs(URL)


for url in URLs:
    print(url)

save_images(URLs, directory)
