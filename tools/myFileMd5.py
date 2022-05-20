#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os,os.path
import sys
from optparse import OptionParser
import hashlib

#######functions##########
def getFileMd5(fileName):
	fp=open(fileName,'rb')
	content=fp.read()
	fp.close()

	md5=hashlib.md5()
	md5.update(content)
	return md5.hexdigest()

#######functions##########	
def init(filePath):
	print('parm:'+filePath)
	md5Str=getFileMd5(filePath)
	print(md5Str)
	print(md5Str.upper())

# -------------- main --------------
if __name__ == '__main__':
	
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="file_name", help='it is not used')
	(opts, args) = parser.parse_args()

	init(opts.file_name)
		