# pre-commit automation example

## Test steps

- four test files were created in an empty test directory.
- pc was run to initialize the repo.
- files are tested for function after the process.
- configuration files are examined and tested.
- github repo is examined for errors.

```bash
~/temp
❯ mkdir pc_test
mkdir: created directory 'pc_test'

~/temp
❯ cd pc_test

~/temp/pc_test
❯ echo 'testing ... this ...' >test.txt

~/temp/pc_test
❯ echo '<?php phpinfo(); ?>' >test.php

~/temp/pc_test
❯ echo 'import sys; print(sys.path[0])' >test.py

~/temp/pc_test
❯ echo -e "
NAME\n\tdc - use paramter expansion for pattern matching\n\nSYNOPSIS\n\tdc PARAMETER [PATTERN] [STRING]\n\nDESCRIPTION\n\n\t"'"DirtyClean" uses parameter expansion to perform command line pattern matching. The basic pattern used is:'"\n\n\t\t"'${parameter/pattern/string}'"\n\n\tWhile this can be done on the command line easily, (e.g.)\n\n\t\t"'$ dirty="Â10.41.89.50 "\n\t\t$ clean=${dirty//[^[:digit:].-]/}\n\t\t$ echo "$clean"\n\t\t10.41.89.50\n\n\tIt is handy to have a way to save presets, pipe outputs, or call from scripts without the overhead of manipulating variables directly.' >dc_usage.sh

~/temp/pc_test
❯ la
total 16K
-rw-r--r-- 1 skeptycal staff 545 Apr 30 04:02 dc_usage.sh
-rw-r--r-- 1 skeptycal staff  20 Apr 30 03:57 test.php
-rw-r--r-- 1 skeptycal staff  31 Apr 30 04:00 test.py
-rwxrwxr-x 1 skeptycal staff  21 Apr 30 03:57 test.txt*
```

---

## pc tests begin here and all test feedback is shown.

```bash
~/temp/pc_test
❯ pc
Project setup: Brew, git, hub, pipenv, pre-commit, travis, codecov.

Template file (.pre-commit-template.yaml) NOT found in current directory.
Using generic template ...

This is not a git repo. Setting up git and github ...

Git repo setup ...

Initialized empty Git repository in /Volumes/Data/skeptycal/temp/pc_test/.git/
GitHub remote repo setup ...

Updating origin
https://github.com/skeptycal/pc_test

This is not a pipenv virtual environment.
Setting up pipenv --python 3.7 ...

Creating a virtualenv for this project…
Pipfile: /Volumes/Data/skeptycal/temp/pc_test/Pipfile
Using /usr/local/bin/python3 (3.7.3) to create virtualenv…
⠴ Creating virtual environment...Using base prefix '/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7'
New python executable in /Volumes/Data/skeptycal/.virtualenvs/pc_test-0XRhmGqG/bin/python3.7
Also creating executable in /Volumes/Data/skeptycal/.virtualenvs/pc_test-0XRhmGqG/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /usr/local/bin/python3

✔ Successfully created virtual environment!
Virtualenv location: /Volumes/Data/skeptycal/.virtualenvs/pc_test-0XRhmGqG
Creating a Pipfile for this project…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Updated Pipfile.lock (a65489)!
Checking PEP 508 requirements…
Passed!
Checking installed package safety…
All good!
[master (root-commit) 3eecbb0] initial commit
 12 files changed, 773 insertions(+)
 create mode 100644 .info.cfg
 create mode 100644 .pre-commit-template.yaml
 create mode 100644 .travis.yml
 create mode 100644 Pipfile
 create mode 100644 Pipfile.lock
 create mode 100644 README.md
 create mode 100644 codecov.yml
 create mode 100755 dc_usage.sh
 create mode 100644 requirements.txt
 create mode 100755 test.php
 create mode 100755 test.py
 create mode 100755 test.txt
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 8 threads
Compressing objects: 100% (11/11), done.
Writing objects: 100% (14/14), 9.84 KiB | 3.28 MiB/s, done.
Total 14 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To github.com:skeptycal/pc_test.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
origin	git@github.com:skeptycal/pc_test.git (fetch)
origin	git@github.com:skeptycal/pc_test.git (push)
Template file (.pre-commit-template.yaml) found in current directory.
-> config file created: .pre-commit-config.yaml
Configuration has been migrated.
Updating git://github.com/pre-commit/pre-commit-hooks...updating master -> 6d7906e131976a1ce14ab583badb734727c5da3e.
Updating git://github.com/pre-commit/mirrors-pylint...updating master -> v2.3.1.

Pre-commit successfully updated your configuration.
Check Yaml...............................................................Passed
Check for added large files..............................................Passed
Check for byte-order marker..............................................Passed
Check docstring is first.............................(no files to check)Skipped
Check for case conflicts.................................................Passed
Check JSON...........................................(no files to check)Skipped
Check for merge conflicts................................................Passed
Check for broken symlinks............................(no files to check)Skipped
Detect Private Key.......................................................Passed
Fix End of Files.........................................................Passed
Flake8...............................................(no files to check)Skipped
Pretty format JSON...................................(no files to check)Skipped
Fix requirements.txt.................................(no files to check)Skipped
Trim Trailing Whitespace.................................................Passed
pylint...............................................(no files to check)Skipped

~/temp/pc_test master* 1m 12s
❯ gst
On branch master
Your branch is up to date with 'origin/master'.
~/temp/pc_test master
```

---

## pc program run ends here. files are examined and tested.

```bash
❯ tree
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── bak
│   └── README.bak.md
├── codecov.yml
├── dc_usage.sh
├── requirements.txt
├── test.php
├── test.py
└── test.txt

1 directory, 10 files
```

```bash
~/temp/pc_test master
❯ cat test.txt
testing ... this ...

~/temp/pc_test master
❯ php test.php
phpinfo()
PHP Version => 7.3.4

System => Darwin skeptycals-MacBook-Pro.local 18.5.0 Darwin Kernel Version 18.5.0: Mon Mar 11 20:40:32 PDT 2019; root:xnu-4903.251.3~3/RELEASE_X86_64 x86_64
Build Date => Apr 19 2019 00:18:53
...

~/temp/pc_test master
❯ python test.py
/Volumes/Data/skeptycal/temp/pc_test

~/temp/pc_test
❯ cat dc_usage.sh

NAME
	dc - use paramter expansion for pattern matching

SYNOPSIS
	dc PARAMETER [PATTERN] [STRING]

DESCRIPTION

	"DirtyClean" uses parameter expansion to perform command line pattern matching. The basic pattern used is:

		${parameter/pattern/string}

	While this can be done on the command line easily, (e.g.)

		$ dirty="Â10.41.89.50 "
		$ clean=${dirty//[^[:digit:].-]/}
		$ echo "$clean"
		10.41.89.50

	It is handy to have a way to save presets, pipe outputs, or call from scripts without the overhead of manipulating variables directly.

```
