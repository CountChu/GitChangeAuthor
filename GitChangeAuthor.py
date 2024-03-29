#
# FILENAME.
#       GitChangeAuthor.py - Git Change Author Application.
#
# FUNCTIONAL DESCRIPTION.
#       The Python application GitChangeAuthor.py changes author name and email
#       of all commitments in a current branch , but keeps all timestamp in the branch
#       by doing the Git amend and rebase commands.
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

#
# Include specific packages.
#

import Util

#
# Build argument parser and return it.
#

def buildArgParser():

    desc = '''
The app changes an author but keeps timestamps for the current branch.

Usage:

    1. Go to your local repository.

    2. Run GitChangeAuthor.py to change the author.

        $ python HOME\GitChangeAuthor.py --name CountChu --email visualge@gmail.com
            HOME is a path that contains GitChangeAuthor.py

    3. Push your changes into the remote repository.
    
        $ git push --force
'''

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Standard arguments
    #

    parser.add_argument(
            "-v",
            dest="verbose",
            action='store_true',
            help="Verbose log")

    parser.add_argument(
            '--log',
            dest='logFn',
            help='A name of a log file.')

    #
    # Anonymous arguments.
    #

    #
    # Specific arguments
    #

    parser.add_argument(
            '--name',
            dest='name',
            required=True,
            help='Change the user.name of the repository.')

    parser.add_argument(
            '--email',
            dest='email',
            required=True,
            help='Change the user.email of the repository')

    return parser

def readConfig(jsonFn):
    if not os.path.exists(jsonFn):
        return None

    f = open(jsonFn, 'r')
    lines = f.readlines()
    jsonStr = ''.join(lines)
    jsonObj = json.loads(jsonStr)
    f.close()

    return jsonObj

def main():

    #
    # Parse arguments
    #

    args = buildArgParser().parse_args()

    #
    # Enable log if -v
    #

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info(args)

    #
    # Check arguments.
    #

    #
    # Open a log file if --log
    #

    if args.logFn != None:
        logF = open(args.logFn, 'w')

    #
    # Read config.
    #

    jsonFn = 'GitChangeAuthor.json'
    jsonObj = readConfig(jsonFn)

    #
    # Here is core function.
    #

    logList = Util.getLogs()

    cmd = ['git', 'config', 'user.name', args.name]
    lines = Util.command(cmd, True)
    Util.printLines(lines)

    cmd = ['git', 'config', 'user.email', args.email]
    lines = Util.command(cmd, True)
    Util.printLines(lines)

    cmd = ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
    lines = Util.command(cmd, True)
    Util.printLines(lines)
    branch = lines[0]

    for i in reversed(range(len(logList))):
        log = logList[i]
        print(i, log)

        date = log[1]

        logList2 = Util.getLogs()
        hash = logList2[i][0]

        cmd = ['git', 'checkout', '-b', 'temp', hash]
        lines = Util.command(cmd, True)
        Util.printLines(lines)

        os.environ['GIT_COMMITTER_DATE'] = '"%s"' % date
        print('set GIT_COMMITTER_DATE = "%s"' % date)

        cmd = ['git', 'commit', '--amend', '--date=%s' % date, '--reset-author', '--no-edit']
        lines = Util.command(cmd, True, shell=True, env=dict(os.environ))
        Util.printLines(lines)

        cmd = ['git', 'checkout', branch]
        lines = Util.command(cmd, True)
        Util.printLines(lines)

        cmd = ['git', 'rebase', hash, '--onto', 'temp']
        lines = Util.command(cmd, True)
        Util.printLines(lines)

        cmd = ['git', 'branch', '-d', 'temp']
        lines = Util.command(cmd, True)
        Util.printLines(lines)

    Util.getLogs()

    #
    # Close the log file if --log
    #

    if args.logFn != None:
        logF.close()

if __name__ == '__main__':

    main()
