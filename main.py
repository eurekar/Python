# _*_ coding: utf-8 _*_
import sys

reload(sys) # 
sys.setdefaultencoding('utf-8') # default coding

print ('中文' .encode(sys.stdout.encoding)) 
keywords = sys.argv[:]

for words in keywords:
	print words,