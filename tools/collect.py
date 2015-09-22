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
    
    for parent,dirnames,filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            if filename.find(".md")==-1 or filename=='examples.md':
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
                   if re.search(u'^(- \[)', line.decode('utf8'))!=None or re.search(u'^(- \()', line.decode('utf8'))!=None:
                       # print line
                        xx+=line.strip('\n')
                   elif re.search('^(> 出处：)', line)!=None:
                        #print cc
                        cc=line.strip('\n')
                        print filename
                   elif re.search('^(> 知识点：)', line)!=None:
                        kn=line.strip('\n')
                        
                   elif re.search('> ', line)!=None:
                        js+=line.strip('\n')
                   elif re.search('^(\d\n)$', line)!=None:
                        i=line.strip('\n')
                   elif line.strip('\n')!='':
                        tg+=line.strip('\n')


               #print cc
               fr.close()
               if sys.argv[2]!='""':
                  if i==sys.argv[2]:
                       result=1
                  else:
                       continue
              
               if sys.argv[3]!='""':
                  if tg.find(sys.argv[3])!=-1:
                       result=1
                  else:
                       continue
               if sys.argv[4]!='""':
                  if xx.find(sys.argv[4])!=-1:
                       result=1
                  else:
                       continue
               if sys.argv[5]!='""':
                  if js.find(sys.argv[5])!=-1:
                       result=1
                  else:
                       continue
               if sys.argv[6]!='""':
                  if cc.find(sys.argv[6])!=-1:
                       result=1
                  else:
                       continue
         
               if result==1:
                  shutil.copyfile(parent+'/'+filename, "./result/"+filename)   
                       
                   
