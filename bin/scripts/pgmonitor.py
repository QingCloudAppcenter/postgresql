#!/usr/bin/python3
import os 
 
 

def execCmd(cmd):
  p = os.popen(cmd)
  result =(p.read()).strip()
  return result 


#connections cmd 
connCmd = 'psql -U postgres -t -c "select sum(numbackends) from pg_stat_database;"' 
connCnt = execCmd(connCmd)  
#print(connCnt)

#xact_commit cmd, the total count of transactions 
commitCmd = 'psql -U postgres -t -c "select sum(xact_commit) from pg_stat_database;"' 
commitCnt = execCmd(commitCmd)  
#print(commitCnt)


#deadlocks cmd 
deadlocksCmd = 'psql -U postgres -t -c "select sum(deadlocks) from pg_stat_database;"' 
deadlocksCnt = execCmd(deadlocksCmd)  
#print(deadlocksCnt) 

#wait event count
waiteventCmd = 'psql -U postgres -t -c " SELECT count(*) FROM pg_stat_activity WHERE wait_event is NOT NULL;"' 
waiteventCnt = execCmd(waiteventCmd)  
#print(waiteventCnt)


#As most of the static data in pg_stat_database is accumulated values since last reset(except numbackends),so need to reset after each monitor.
resetCmd = 'psql -U postgres -t -c "select pg_stat_reset();"' 
os.system(resetCmd)
 
 
print('{"connCnt":'+connCnt+',"commitCnt":'+commitCnt+',"deadlocksCnt":'+deadlocksCnt+',"waiteventCnt":'+waiteventCnt+'}')