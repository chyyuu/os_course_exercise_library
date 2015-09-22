#!/usr/bin/python
#coding=utf-8

import sys
import random
import re
import os
import shutil
reload(sys)  
sys.setdefaultencoding('utf8') 

try:
    os.mkdir("result")
except Exception,e:
    print e
finally:
    if len(sys.argv) !=7:
       print "usage:%s %s %s %s %s %s %s" %(sys.argv[0], "<filepath>", "<1-5>", "<str>", "<str>", "<str>", "<str>")  
       exit(-1)
    count=0
    pa1=sys.argv[2].strip('"').split(',')
    pa2=sys.argv[3].strip('"').split(',')
    pa3=sys.argv[4].strip('"').split(',')
    pa4=sys.argv[5].strip('"').split(',')
    pa5=sys.argv[6].strip('"').split(',')
    print pa1,pa2,pa3,pa4,pa5
    for parent,dirnames,filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            if filename.find(".md")==-1 or filename=='examples.md' or filename.find(".md~")!=-1:
               continue
            else:
               i=""
               tg=""
               xx=""
               cc=""
               js=""
               kn=""
               result=1
               fr=open(sys.argv[1]+'/'+filename, 'rb')
   
               
               for line in fr.readlines():   
                   if re.search(u'^(- \[)', line)!=None or re.search('^(- \()', line)!=None:
                       # print line
                        xx+=line.strip('\n')
                   elif re.search('^(> 出处：)', line)!=None:
                        #print cc
                        cc=line.strip('\n')
    
                   elif re.search('^(> 知识点：)', line)!=None:
                        kn=line.strip('\n')
                        #print kn
                   elif re.search('> ', line)!=None:
                        js+=line.strip('\n')
                   elif re.search('^(\d\n)$', line)!=None:
                        i=line.strip('\n')
                   elif line.strip('\n')!='':
                        tg+=line.strip('\n')


               #print cc
               fr.close()
               if sys.argv[2]!='""':
                  flag=0
                  for j in range(len(pa1)):
                    if i.find(pa1[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue

               if sys.argv[3]!='""':
                  flag=0
                  for j in range(len(pa2)):
                    if tg.find(pa2[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue
               if sys.argv[4]!='""':
                  flag=0
                  for j in range(len(pa3)):
                    if xx.find(pa3[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue
               if sys.argv[5]!='""':
                  flag=0
                  for j in range(len(pa4)):
                    if js.find(pa4[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue
               if sys.argv[6]!='""':
                  flag=0
                  for j in range(len(pa5)):
                    if cc.find(pa5[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue

               if result==1:
                  count=count+1
                  print filename
                  shutil.copyfile(parent+'/'+filename, "./result/"+filename)
    print count,"个文件" 
                       
                   
