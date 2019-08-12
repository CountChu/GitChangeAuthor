# GitChangeAuthor
The Python application [GitChangeAuthor.py](GitChangeAuthor.py) changes author, but keeps timestamp for the current branch.

It changes author names and emails of all commitments in a current branch, but keeps all timestamp in the branch by doing the Git amend and rebase commands

## Usage
```
usage: GitChangeAuthor.py [-h] [-v] [--log LOGFN] --name NAME --email EMAIL

The app changes an author but keeps timestamps for the current branch.

Usage:

    1. Go to your local repository.

    2. Run GitChangeAuthor.py to change the author.

        $ python HOME\GitChangeAuthor.py --name CountChu --email visualge@gmail.com
            HOME is a path that contains GitChangeAuthor.py

    3. Push your changes into the remote repository.

        $ git push --force

optional arguments:
  -h, --help     show this help message and exit
  -v             Verbose log
  --log LOGFN    A name of a log file.
  --name NAME    Change the user.name of the repository.
  --email EMAIL  Change the user.email of the repository
```
