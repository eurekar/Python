# Project 1 简单日记本


## 使用sys模块实现输入

    
    import sys

    keywords = sys.argv[:]

    print keywords 

    for words in keywords: # 2nd way of output
	    print words, 

## 中文编码


    # _*_ coding:utf-8 _*_

    import sys

    # from sys import argv 貌似无意义

    reload(sys) # 
    sys.setdefaultencoding('utf-8') # default coding


    print ('中文') # coding does not work

    print ('中文' .encode(sys.stdout.encoding)) # coding works

    keywords = sys.argv[:]

    print keywords # coding doesn't work 

    for words in keywords: 
	    print words, 	#coding works