'''
Created on Apr 22, 2015

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
from os import listdir
from os.path import isfile, join
import nltk 
from nltk.tag.hunpos import HunposTagger
from nltk.tokenize import word_tokenize
import os
import sys
reload(sys)  
#sys.setdefaultencoding('utf8')
mypath = "texts_burek/"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
corpus = "zeleni ko polje, blagi ko oboje"
#please help me to correct my python syntax errors, i'm new to python 
#but i really need this to work. sorry
##from nltk.tag import hunpos.HunPosTagger
print os.environ['HUNPOS']
ht = HunposTagger('model.hunpos.mte5.defnpout')
tagged =  ht.tag(word_tokenize(corpus))
print tagged
i = 0
for t in tagged:
    if(tagged[i-1]!=None and ('A' in tagged[i-1][1] or 'N' in tagged[i-1][1]) and (tagged[i][0]=='kao' or tagged[i][0]=='ko') and tagged[i+1]!=None and 'N' in tagged[i+1][1]):
        print tagged[i-1][0].encode('utf8')+' '+tagged[i][0].encode('utf8')+' '+tagged[i+1][0].encode('utf8')
    i = i+1
for file in onlyfiles:
    file_object = open(mypath+file, "r")
    corpus = unicode(file_object.read(),"utf8")
    corpus = unicode(corpus.encode('utf8'), "ISO-8859-1")
    tagged =  ht.tag(word_tokenize(corpus))
    #tokens = word_tokenize(corpus)
    #print tagged
    i = 0
    for t in tagged:
        if(tagged[i-1]!=None and ('A' in tagged[i-1][1] or 'N' in tagged[i-1][1]) and (tagged[i][0]=='kao' or tagged[i][0]=='ko') and tagged[i+1]!=None and 'N' in tagged[i+1][1]):
            print tagged[i-1][0].encode('utf8')+' '+tagged[i][0].encode('utf8')+' '+tagged[i+1][0].encode('utf8')
            #print tagged[i-1][0].decode('ISO-8859-1').encode('utf8')+' '+tagged[i][0].decode('ISO-8859-1').encode('utf8')+' '+tagged[i+1][0].decode('ISO-8859-1').encode('utf8')
        i = i+1
    