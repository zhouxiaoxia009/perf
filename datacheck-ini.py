import os
import string

cwd = os.getcwd()
fileConfig = open(str(cwd+'\config.txt'), 'r')
fileSource = open(str(cwd+'\checkadd.txt'), 'r')
fileOutput = open(str(cwd+'\ini.txt'), 'w')

config=''
for line in fileConfig.readlines():
    if line == '\n':
        line = line.strip("\n")
    config+=line
config+='\n'

line = fileSource.readline()
while line:
    line_list=line.split()
    temple = string.Template(config)
    fileOutput.write(temple.substitute(var1=line_list[0], var2=line_list[1]))
    line = fileSource.readline()

fileOutput.close()
fileSource.close()
fileOutput.close()
