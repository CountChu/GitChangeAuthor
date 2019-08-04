#
# FILENAME.
#       Util.py - Util Module.
#
# FUNCTIONAL DESCRIPTION.
#       The module provide APIs. 
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2019/8/3
#

#
# Include standard packages.
#

import argparse
import logging
import pdb
import os
import json
import subprocess

#
# Include specific packages.
#

#
# It wraps subprocess.Popen().
#

def command(cmd, show=False, shell=False, env=None):
    if show:
        cmdStr = ''
        for str in cmd:
            cmdStr += (str + ' ')
        print(cmdStr)
        
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=shell, env=env)
    output = process.communicate()[0]
    text = output.decode('utf-8')    
    lines = text.split('\n')
    newLines = []
    for line in lines:
        if len(line) >= 2 and line[0] == '"' and line[-1] == '"':
            line = line[1:-1]
        newLines.append(line)
    return newLines
    
#
# print lines that is an array.
#    

def printLines(lines):
    for line in lines:
        print(line)

#        
# It is a high level function to get the logs of each record contains hash and timestamp.
#
        
def getLogs():
    cmd = ['git', 'log', '--pretty="%H %ai %an %aE"']
    lines = command(cmd, True)
    printLines(lines)
    logList = []
    for line in lines:
        if line.strip() == '':
            continue
        words = line.split(' ')
        #pdb.set_trace()
        hash = words[0]
        timestamp = '%sT%s' % (words[1], words[2])
        logList.append((hash, timestamp))
    return logList