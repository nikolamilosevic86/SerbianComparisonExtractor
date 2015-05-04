'''
Created on Apr 23, 2015

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
mypath = "../crawler/SerbCrawler/SerbCrawler/files_burek/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
for file in onlyfiles:
    file_object = open(mypath+file, "r")
    sdata = file_object.read()
    soup = BeautifulSoup(sdata)
    mydivs = soup.findAll("body")
    with open("texts_burek/"+file.split("/")[-1]+".txt", 'wb') as f:
        if mydivs != None and len(mydivs)>0:
            f.write(mydivs[0].text.encode("utf8"))
print "Hello"
