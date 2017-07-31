#!/usr/bin/python3
import os
import time
import logging
import pylogger


logger = logging.getLogger('pgbackuplogger') 
pylogger.createLogger(logger)
logger.info("********************PG data backup starts.******************") 

ISOTIMEFORMAT = '%Y%m%d %X'
ISOTIMEFORMAT1= '%Y%m%d'

#backupDate="20170701"
backupDate =  time.strftime(ISOTIMEFORMAT1, time.localtime() )
logger.info("Data backup date is "+backupDate)

starttime = time.strftime(ISOTIMEFORMAT, time.localtime() )
logger.info("Backup starts at : "+ starttime)

#step initial:check to store only 4 times backup
dirs = os.listdir("/data/pgdatabackup/pgbasebackupdir")
dirs.sort()
dirs.reverse()
#for file in dirs:
#	print(file)

i = 0
for file in dirs:
	date=time.strptime(file,ISOTIMEFORMAT1)
	bkdate=time.strptime(backupDate,ISOTIMEFORMAT1)

	if date < bkdate and i<=3:
		logger.info("keep backup for  "+ file)
		i=i+1
	else:
		logger.info("delete backup for  "+ file)
		os.system("rm -r /data/pgdatabackup/pgbasebackupdir/"+file)

#step0:create directory for databackup 
os.system("mkdir /data/pgdatabackup/pgbasebackupdir/"+backupDate);

#step1:copy archived wal to backup directory
os.system("cp -r /data/pgdatabackup/pgwalarchivedir /data/pgdatabackup/pgbasebackupdir/"+backupDate+"/pgwalarchivedir")
os.system("rm -r /data/pgdatabackup/pgwalarchivedir/*")


#step2:make a base databackup for specific day
basebkcmd = "pg_basebackup -h 127.0.0.1 -U postgres -F t  -P  -D /data/pgdatabackup/pgbasebackupdir/"
basebkcmd = basebkcmd + backupDate + "/base/ -l basebackup"+ backupDate;
#logger.debug("basebkcmd"+basebkcmd)
os.system(basebkcmd)

#step3:copy pg_xlog tp backup directory
cpwalcmd = "cp -r /data/pgsql/main/pg_xlog/  /data/pgdatabackup/pgbasebackupdir/"+backupDate;
#logger.debug("cpwalcmd="+cpwalcmd)
os.system(cpwalcmd)

endtime =time.strftime(ISOTIMEFORMAT, time.localtime() )
logger.info("Backup ends at : "+ endtime)


logger.info("********************PG data backup ends.******************")




