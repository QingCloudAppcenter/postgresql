#!/usr/bin/python3

import logging 

def createLogger(logger):   
# 创建一个logger 
#	logger = logging.getLogger('mylogger') 
	logger.setLevel(logging.DEBUG) 
   
# 创建一个handler，用于写入日志文件 
	fh = logging.FileHandler('/data/pgsql/main/pg_log/pgscripts.log') 
#fh = logging.FileHandler('test.log') 
	fh.setLevel(logging.DEBUG) 
   
# 再创建一个handler，用于输出到控制台 
	ch = logging.StreamHandler() 
	ch.setLevel(logging.DEBUG) 
   
# 定义handler的输出格式 
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
	fh.setFormatter(formatter) 
	ch.setFormatter(formatter) 
   
# 给logger添加handler 
	logger.addHandler(fh) 
	logger.addHandler(ch)
	return 
   
# 记录一条日志
#logger = logging.getLogger('mylogger')
#createLogger(logger)
#logger.info('foorbar') 

