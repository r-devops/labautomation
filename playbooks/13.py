#!/usr/bin/python

#print 'Hello World'
import os

REPO_URL='http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-release-3.4-2.el7.noarch.rpm'

out=os.system("rpm -qa | grep -w kernel")
print out

