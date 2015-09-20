#!/usr/bin/python
#coding=utf-8

import sys
import random
import re
import os

editor='<textarea rows="5" cols="70"></textarea>'

reload(sys)  
sys.setdefaultencoding('utf8') 


if len(sys.argv) !=5:
   print "usage:%s %s <xz_count>  <tk_count>  <wd_count> " % (sys.argv[0], '<filepath>')
   exit(-1)

xz_list=[]
tk_list=[]
wd_list=[]

for parent,dirnames,filenames in os.walk(sys.argv[1]):
   for filename in filenames:
      #print filename
      if filename.find('md') == -1:
          continue
      fr=open(sys.argv[1]+'/'+filename, 'rb')
      line=fr.readline()
      #print line
      if line == '1\n':
         xz_list.append(filename)
      if line == '2\n':
         xz_list.append(filename)
      if line == '3\n':
         xz_list.append(filename)
      if line == '5\n':
         tk_list.append(filename)
      if line == '4\n':
         wd_list.append(filename)
      fr.close()
#print len(xz_list)
#print tk_list
#print wd_list      
number_xz=[random.randint(1, len(xz_list)) for i in range(int(sys.argv[2]))]
number_tk=[random.randint(1, len(tk_list)) for i in range(int(sys.argv[3]))]
number_wd=[random.randint(1, len(wd_list)) for i in range(int(sys.argv[4]))]
fsj=open('sj.md', 'wb')
fsj.write('#选择题\n')
fsj.write('---\n')

for j in range(len(number_xz)):
   print xz_list[number_xz[j]]
#print number_tk
#print number_wd

for j in range(len(number_xz)):
   fxz=open(sys.argv[1]+'/'+ xz_list[number_xz[j]], 'rb')
   text=fxz.read()
   text=re.sub('^([12345]\n)', '', text)
   fsj.write(text)
   fsj.write('\n')
   fxz.close()
fsj.write('---\n\n')
fsj.write('#填空题\n')

x=1
for k in range(len(number_tk)):
   fsj.write(str(x)+'.')
   ftk=open(sys.argv[1]+'/'+ tk_list[number_tk[k]], 'rb')
   text=ftk.read()
   text=re.sub('^([12345]\n)', '', text)
   text=re.sub('- \[x\] ', editor, text,  flags=re.M)
   #print text
   fsj.write(text)
   fsj.write('\n')
   ftk.close()
   x=x+1

y=1
fsj.write('#问答题\n')
for l in range(len(number_wd)):  
   fsj.write(str(y)+'.')
   fwd=open(sys.argv[1]+'/'+ wd_list[number_wd[l]], 'rb')
   text=fwd.read()
   text=re.sub('^([12345]\n)', '', text)
   text=re.sub('^(- \[x\] )', editor, text, flags=re.M)
   fsj.write(text)
   fsj.write('\n')
   fwd.close()
   y=y+1
fsj.close()
