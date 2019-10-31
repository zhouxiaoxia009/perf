import os
import string
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputpath', type=str)
args = parser.parse_args()
cwd = args.outputpath
if cwd is None:
	cwd = os.getcwd()
	cwd = cwd + '\datacheck_ini_utility'


fileConfig = open(str(cwd+'\config.txt'), 'r')
fileSource = open(str(cwd+'\checkadd.txt'), 'r')
fileOutput = open(str(cwd+'\ini.txt'), 'w')


config = ''
for line in fileConfig.readlines():
	if line == '\n':
		line = line.strip("\n")
	config += line
config += '\n'


line = fileSource.readline()
while line != '\n':
	if len(line)==0:
		break
	else:
		line_list = line.split('\t')
		temple = string.Template(config)
		diction = {}
		for number in range(1, len(line_list)+1):
			varnum = 'var'+str(number)
			diction[varnum] = str(line_list[number-1].strip('\n'))
		out = temple.substitute(diction)
		fileOutput.write(out)
		line = fileSource.readline()

fileOutput.close()
fileSource.close()
fileOutput.close()
