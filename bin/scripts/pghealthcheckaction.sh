#! /bin/bash
echo "`date "+%Y-%m-%d %H:%M:%S"` : After healthcheck,it needs to restart posgresql" >> /var/log/syslog
service postgresql restart 
echo "`date "+%Y-%m-%d %H:%M:%S"` : Postgresql restarted!" >> /var/log/syslog

