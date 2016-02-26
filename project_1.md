# Project 1 简单日记本


```# _*_ coding:utf-8 _*_

import sys

 # from sys import argv

reload(sys) # 
sys.setdefaultencoding('utf-8') # default coding


print ('中文') # coding does not work

print ('中文' .encode(sys.stdout.encoding)) # coding works

keywords = sys.argv[:]

print keywords # coding doesn't work 

for words in keywords: 
	print words, 	#coding works```