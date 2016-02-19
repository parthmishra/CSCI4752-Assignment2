#!/usr/bin/python

import subprocess
import csv
import time


mibEntries = ['.1.3.6.1.2.1.2.2.1.10',	# InOctets
			  '.1.3.6.1.2.1.2.2.1.11',	# InUCastPkts
			  '.1.3.6.1.2.1.2.2.1.12',	# InNUcastPkts
			  '.1.3.6.1.2.1.2.2.1.16',	# OutOCtets
			  '.1.3.6.1.2.1.2.2.1.17',	# OutUcastPkts
			  '.1.3.6.1.2.1.2.2.1.18',	# OutNUcastPkts
			 ]

test = [{'Name': 'Parth', 'Last': 'Mishra'}]

mibs = [10,11,12,16,17,18]

interface = [1,2,3,6,7,9,10,11]

def writeToFile(sample, interface, outUCastPkts, inOctets, outOctets, inUcastPkts, 
	outNUCastPkts, inNUcastPkts):
	with open('data.csv', 'w') as csvfile:
		fieldnames = ['sample', 'if', 'outUCastPkts', 'inOctets', 'outOctets', 'inUcastPkts', 
		'outNUCastPkts', 'inNUcastPkts']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'sample': sample, 'if': interface, 'outUCastPkts': outUCastPkts,
		 'inOctets': inOctets, 'outOctets': outOctets, 'inUcastPkts': inUcastPkts, 
		 'outNUCastPkts': outNUCastPkts, 'inNUcastPkts': inNUcastPkts})

def runCmd(value, interface):
	print "value is ", value
	print "interface is ", interface
	number = '0'

	if value == 10:
		number = mibEntries[0]+'.'+str(interface)
	elif value == 11:
		number = mibEntries[1]+'.'+str(interface)
	elif value == 12:
		number = mibEntries[2]+'.'+str(interface)
	elif value == 16:
		number = mibEntries[3]+'.'+str(interface)
	elif value == 17:
		number = mibEntries[4]+'.'+str(interface)
	elif value == 18:
		number = mibEntries[5]+'.'+str(interface)
	else:
		print "value not in bounds"



	cmd = [ "/usr/bin/snmpget",
        	"-v", "2c",
        	"-c", "public",
        	"128.138.207.5:7777", number]
	output = subprocess.check_output(cmd)
	output = output.split()
	print "Cmd is", cmd
	print "Output is ", output[-1]
	return output[-1]


with open('data.csv', 'w') as csvfile:
	fieldnames = ['sample', 'if', 'outUCastPkts', 'inOctets', 'outOctets', 'inUcastPkts', 
	'outNUCastPkts', 'inNUcastPkts']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for i in range(0,12):
		for j in interface:
			If = j
			inOctets = runCmd(10, j)
			inUcastPkts = runCmd(11, j)
			inNUcastPkts = runCmd(12, j)
			outOctets = runCmd(16, j)
			outUCastPkts = runCmd(17, j)
			outNUCastPkts = runCmd(18, j)
			writer.writerow({'sample': i, 'if': If, 'outUCastPkts': outUCastPkts,
		 'inOctets': inOctets, 'outOctets': outOctets, 'inUcastPkts': inUcastPkts, 
		 'outNUCastPkts': outNUCastPkts, 'inNUcastPkts': inNUcastPkts})
		time.sleep(10)

	

