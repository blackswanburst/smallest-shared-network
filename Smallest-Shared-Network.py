#! /usr/bin/env python
# coding=UTF-8
# Filename: Smallest-Shared-Subnet.py
# Template python-shodan code from:
# eireann.leverett@cantab.net

import sys

def ip2binaryip (iplist):
    biplist = []
    for ip in iplist:
        bip = ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
        biplist.append(bip)
    return biplist


if len(sys.argv) == 1:
	print 'Usage: Please provide a filename with an IPv4 address in each line.%s' %sys.argv[0]
	sys.exit(1)

list_of_ips = ' '.join(sys.argv[1:])
biplist = ip2binaryip(open(list_of_ips))
i = 0
terminate = False
while (i <= 31):
    bit = int(biplist[0][i])
    for bip in biplist:
        if bit ^ int(bip[i]) == 1:
            terminate = True
            break
    if terminate == True:
        host = ''
        #Construct and print CIDR
        for j in xrange(i):
            #assemble host network
            host += biplist[0][j]
        add = 32-len(host)
        host+='0'*add
        print str(int(host[0:8],2))+'.'+str(int(host[8:16],2))+'.'+str(int(host[16:24],2))+'.'+str(int(host[24:32],2))+'/'+str(i)
        break
    i += 1
