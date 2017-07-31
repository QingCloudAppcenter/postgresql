#! /bin/bash
cp -rf /var/lib/postgresql/9.6/ /data/pgsql/;
chown -R postgres:postgres /data/pgsql/;  
chmod 700 /data/pgsql/;  
chown -R postgres:postgres /data/pgsql/main/;  
chmod 700 /data/pgsql/main/;

mkdir /data/pgdatabackup/;
mkdir /data/pgdatabackup/pgwalarchivedir/;
mkdir /data/pgdatabackup/pgbasebackupdir;
chown -R postgres:postgres /data/pgdatabackup/pgwalarchivedir/;
chmod 700 /data/pgdatabackup/pgwalarchivedir/;
