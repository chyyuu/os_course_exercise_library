#!/usr/bin/python
#coding=utf-8

import sys
import random
import re
import os

editor='''<div id="active-code">
<button class="btn btn-primary" type="button" id="run-code" value="{1}">提交</button>
<button class="btn btn-primary" type="button" id="reset-code">重置</button>
<div id="editor">
</div>
<div id="result"></div>
</div>'''

def mkdir(path):
    isexist=os.path.exists('test/'+path)
    if not isexist:
       os.makedirs('test/'+path)

reload(sys)  
sys.setdefaultencoding('utf8') 


if len(sys.argv) !=7 and len(sys.argv)!=3:
   print "usage:%s %s <xz_count> <dzd_count> <pd_count> <tk_count>  <wd_count> " % (sys.argv[0], '<filepath>')
   print "      %s %s %s" %(sys.argv[0], '<filepath>', '<zhishidian>')
   exit(-1)

if len(sys.argv)==3:
   if(isinstance(sys.argv[2], basestring)):
      ff=open(sys.argv[2], 'wb')
      for parent,dirnames,filenames in os.walk(sys.argv[1]):
        for filename in filenames:
          if parent==sys.argv[1]:  
            if filename.find('md') == -1 or filename.find('md~')!=-1:
               continue
            
            fr=open(sys.argv[1]+'/'+filename, 'rb')
            context=fr.read()
            result=re.search(u'(\u77e5\u8bc6\u70b9\uff1a)([\u4e00-\u9fa5]+|I/O)([、]*[\u4e00-\u9fa5]*)*', context.decode('utf8'))
            if result!=None:        
               if result.group().find(sys.argv[2])!=-1:
                  ff.write(filename + '\n')
            fr.close()
   ff.close()
   exit(-1)

xz_list=[]
dzd_list=[]
pd_list=[]
tk_list=[]
wd_list=[]

for parent,dirnames,filenames in os.walk(sys.argv[1]):
   for filename in filenames:
      #print filename
      if filename.find('md') == -1 or filename.find('md~')!=-1:
          continue
      fr=open(sys.argv[1]+'/'+filename, 'rb')
      line=fr.readline()
      #print line
      if line == '1\n':
         xz_list.append(filename)
      if line == '2\n':
         dzd_list.append(filename)
      if line == '3\n':
         pd_list.append(filename)
      if line == '5\n':
         tk_list.append(filename)
      if line == '4\n':
         wd_list.append(filename)
      fr.close()


print "xz:",len(xz_list)
print "dzd:",len(dzd_list)
print "pd",len(pd_list)
print "tk",len(tk_list)
print "wd",len(wd_list) 

if(int(sys.argv[2])>len(xz_list) or int(sys.argv[3])>len(dzd_list) or int(sys.argv[4])>len(pd_list) or int(sys.argv[5])>len(tk_list) or int(sys.argv[6])>len(wd_list)):
   print "error"
   exit(-1)
     
number_xz=random.sample(xz_list, int(sys.argv[2]))
number_dzd=random.sample(dzd_list, int(sys.argv[3]))
number_pd=random.sample(pd_list, int(sys.argv[4]))
number_tk=random.sample(tk_list, int(sys.argv[5]))
number_wd=random.sample(wd_list, int(sys.argv[6]))
fsj=open('test/SUMMARY.md', 'wb')
#fsj.write('#选择题\n')
fsj.write('#sj\n')

print number_xz
print number_dzd
print number_pd
print number_tk
print number_wd
print dzd_list
   #print tk_list[number_tk[j]]
   #print wd_list[number_wd[j]]

for j in range(len(number_xz)):
   fxz=open(sys.argv[1]+'/'+ number_xz[j], 'rb')
   text=fxz.read()
   text=re.sub('^([12345]\n)', '', text)
   tihao=re.sub('.md', '', number_xz[j])
   mkdir('xz'+str(tihao))
   f=open('test/xz'+str(tihao)+'/'+str(tihao)+'.md', 'wb')
   fsj.write('* [xz'+str(tihao)+'](xz' + str(tihao)+'/'+str(tihao)+'.md)')
   fsj.write('\n')
   f.write('---\n')
   f.write(text)
   f.write('\n')
   fxz.close()
   f.write('---\n')
   f.close()
#fsj.write('#填空题\n')

for j in range(len(number_dzd)):
   fxz=open(sys.argv[1]+'/'+ number_dzd[j], 'rb')
   text=fxz.read()
   text=re.sub('^([12345]\n)', '', text)
   tihao=re.sub('.md', '', number_dzd[j])
   mkdir('dzd'+str(tihao))
   f=open('test/dzd'+str(tihao)+'/'+str(tihao)+'.md', 'wb')
   fsj.write('* [dzd'+str(tihao)+'](dzd' + str(tihao)+'/'+str(tihao)+'.md)')
   fsj.write('\n')
   f.write('---\n')
   f.write(text)
   f.write('\n')
   fxz.close()
   f.write('---\n')
   f.close()

for j in range(len(number_pd)):
   fxz=open(sys.argv[1]+'/'+ number_pd[j], 'rb')
   text=fxz.read()
   text=re.sub('^([12345]\n)', '', text)
   tihao=re.sub('.md', '', number_pd[j])
   mkdir('pd'+str(tihao))
   f=open('test/pd'+str(tihao)+'/'+str(tihao)+'.md', 'wb')
   fsj.write('* [pd'+str(tihao)+'](pd' + str(tihao)+'/'+str(tihao)+'.md)')
   fsj.write('\n')
   f.write('---\n')
   f.write(text)
   f.write('\n')
   fxz.close()
   f.write('---\n')
   f.close()

x=1
for k in range(len(number_tk)):
   #fsj.write(str(x)+'.')
   ftk=open(sys.argv[1]+'/'+ number_tk[k], 'rb')
   text=ftk.read()
   text=re.sub('^([12345]\n)', '', text)
   text=re.sub('^(> )', '', text, flags=re.M)
   tihao=re.sub('.md', '', number_tk[k])
   mkdir('tk'+str(tihao))
   f=open('test/tk'+str(tihao)+'/'+str(tihao)+'.md', 'wb')
   fa=open('test/tk'+str(tihao)+'/'+str(tihao)+'_answer.md', 'wb')
   fsj.write('* [tk'+str(tihao)+'](tk' + str(tihao)+'/'+str(tihao)+'.md)')
   fsj.write('\n')
   index=text.find('- [x] ')
   f.write(text[:index])
   editor1=editor.replace('{1}', 'tk'+str(tihao))
   f.write(editor1)
   fa.write(text[index+9:])
   #text=re.sub('- \[x\] ', editor, text,  flags=re.M)
   #print text
   #fsj.write(text)
  # fsj.write('\n')
   f.close()
   fa.close()
   ftk.close()
   x=x+1

y=1
#fsj.write('#问答题\n')
for l in range(len(number_wd)):  
   #fsj.write(str(y)+'.')
   fwd=open(sys.argv[1]+'/'+ number_wd[l], 'rb')
   text=fwd.read()
   text=re.sub('^([12345]\n)', '', text)
   text=re.sub('^(> )', '', text, flags=re.M)
   tihao=re.sub('.md', '', number_wd[l])
   mkdir('wd'+str(tihao))
   f=open('test/wd'+str(tihao)+'/'+str(tihao)+'.md', 'wb')
   fa=open('test/wd'+str(tihao)+'/'+str(tihao)+'_answer.md', 'wb')
   fsj.write('* [wd'+str(tihao)+'](wd' + str(tihao)+'/'+str(tihao)+'.md)')
   fsj.write('\n')
   index=text.find('- [x] ')
   f.write(text[:index])
   editor2=editor.replace('{1}', 'wd'+str(tihao))
   f.write(editor2)
   fa.write(text[index+9:])
   #text=re.sub('^(- \[x\] )', editor, text, flags=re.M)
   #fsj.write(text)
  # fsj.write('\n')
   fwd.close()
   f.close()
   fa.close()
   y=y+1
fsj.close()
