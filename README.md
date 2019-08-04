# GitChangeAuthor
The Python application GitChangeAuthor.py changes author, but keeps timestamp for the current branch.

It changes author names and emails of all commitments in a current branch, but keeps all timestamp in the branch by doing the Git amend and rebase commands

## Usage

1. Go to your local repository.

For examples:
```
D:\DashboardPusher
```

2. Run GitChangeAuthor.py with to change the author
```
$ python $HOME\GitChangeAuthor.py --name CountChu --email visualge@gmail.com
```
- $Home is a path that contains GitChangeAuthor.py 
- --name changes the user.name for the repository
- --email changes the user.email for the repository

3. Push your changes into the remote repository.
```
$ git push --force
```
