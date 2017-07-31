#! /bin/bash
 

# check if server port is ready
portStatus=$(netstat -tulpen | grep 5432)
#echo $portStatus
if [ "$portStatus" != "" ]
then
    portReady=true
else
    portReady=false
fi
#echo $portReady

# check if postgresql process is running
processStatus=$(ps -ef | grep -v grep | grep 'postgres')
#echo $processStatus
if [ "$processStatus" != "" ]
then
    pidReady=true
else
    pidReady=false
fi
#echo $pidReady

# check if postgresql default DB(postgres) is running or not 
postgresDBStatus=$(psql -U postgres -t -c " SELECT 1;")  
#remove blank
postgresDBStatus=$(echo $postgresDBStatus | grep -o "[^ ]\+\( \+[^ ]\+\)*" )   
#echo $postgresDBStatus
if [ "$postgresDBStatus" == "1" ]
then
    postgresDBReady=true
else
    postgresDBReady=false
fi
#echo $postgresDBReady




if [ $portReady == "true" ]&&[ $pidReady == "true" ]&&[ $postgresDBReady == "true" ]
then
    exit 0
else
    exit -1
fi
