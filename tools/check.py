#!/usr/bin/python
#coding=utf-8

import sys
import random
import re
import os
import shutil
import json

reload(sys)  
sys.setdefaultencoding('utf8')


if len(sys.argv)!=2:
   print "usage:%s %s" %(sys.argv[0], "<filepath>")
   exit(-1)


try:
   for parent,dirnames,filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            if filename.find(".md")==-1 or filename.find(".md~")!=-1:
               continue
            else:
                result=[]
                i=0
                fr=open(parent + "/"+ filename, 'rb')
                for line in fr.readlines():
                     i=i+1
                     a={"context": line, "line":i}
                     result.append(a)
                fr.close()
                kn=0
                cc=0
                for j in range(len(result)):
                    b=result[j]
                    if j==0:
                      if re.match('^([1-5]\n)',b["context"])==None:
                        print filename,'第',j+1,'行错误'
                    if re.match('^(> 知识点：)', b["context"])!=None:
                        kn=1
                        if result[j-1]["context"]!='\n':
                           print filename,'第',j+1,'少一个空行'
                    if re.match('^(> 出处：)', b["context"])!=None:
                        cc=1
                        if re.match('^(> 知识点：)', result[j-1]["context"])==None:
                           print filename,'第',j+1,'少知识点'
                        
                if kn==0:
                    print filename,'没有找到知识点'
                if cc==0:
                    print filename,'没有找到出处'
                  
except Exception,e:
    print e          
