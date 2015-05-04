'''
Created on Apr 23, 2015

@author: Nikola

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import collections
with open('output_burek.txt') as f:
    lines = f.read().splitlines()
lines.sort()
for x in sorted(lines):
    print x
myset = set(lines)
counter=collections.Counter(lines)
for key, value in counter.iteritems() :
    print key+"    "+ str(value)
file = open("unique_burek.txt",'w')
for key, value in counter.iteritems() :
    file.write(key+"    "+ str(value)+'\n')
file.close()