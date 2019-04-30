# project version 0.0.1

[![Netlify Status](https://api.netlify.com/api/v1/badges/416b8ca3-82db-470f-9adf-a6d06264ca75/deploy-status)](https://app.netlify.com/sites/mystifying-keller-ab5658/deploys)

04-30-2019 | 03:41:17

---

## portfolio project for macOS

```bash


###############################################################################
# project : portfolio project for macOS (version 0.0.1)

# author    - Michael Treanor  <skeptycal@gmail.com>
# copyright - 2019 (c) Michael Treanor
# license   - MIT <https://opensource.org/licenses/MIT>
# github    - https://www.github.com/skeptycal

# Usage: project {init|reset|version|help}

#   Parameters:
#       init, -i, --init        -- install and initialize
#       reset, -r, --reset      -- reset initial repo files (with backup)
#       version, -v, --version  -- display version information
#       help, -h, --help        -- display usage and information

#   .pre-commit-template.yaml must be in current directory
#       If not, a generic template will be created
#   .pre-commit-bak.yaml will be created (if possible)
#       from .pre-commit-config.yaml as backup
#   .pre-commit-config.yaml will be *overwritten*
#       and updated to current master sha from GitHub
###############################################################################


# Run this script if changes to the pre-commit or yaml configuration are added.

# Please make changes directly to the 'template' file:
#     <.pre\-commit-template.yaml>
# and run the script 'pc' to update the yaml to current versioning.

# Please do not make changes directly to the 'config' file. The 'config' file:
#     <.pre-commit-config.yaml>
#   is created and updated by the 'pc' script automatically in order to maintain
#   the correct, current versioning from git (master sha) so changes to the
#   commit file will be overwritten when updating.
###############################################################################


# Pre-commit Sample yaml template
default_language_version:
    python: python3.7
default_stages: [commit, push]
exclude: "^$"
fail_fast: false
# @see http://pre-commit.com/
repos:
    - repo: git://github.com/pre-commit/pre-commit-hooks
      sha: master
      hooks:
          - id: check-yaml
            files: \.(yaml|yml)$
          - id: check-added-large-files
          - id: check-byte-order-marker
          - id: check-docstring-first
          - id: check-case-conflict
          - id: check-json
          - id: check-merge-conflict
          - id: check-symlinks
          #   -   id: detect-aws-credentials
          - id: detect-private-key
          - id: end-of-file-fixer
          - id: flake8
            args: [--max-line-length=79]
          - id: pretty-format-json
          - id: requirements-txt-fixer
          - id: trailing-whitespace
    # Python settings ... replace as needed
    - repo: git://github.com/pre-commit/mirrors-pylint
      sha: master
      hooks:
          - id: pylint
# PHP settings ... replace as needed
# - repo: git@github.com:hootsuite/pre-commit-php.git
#   sha: 1.1.0
#   hooks:
#   - id: php-lint-all
#   - id: php-unit
#   - id: php-cs
#     files: \.(php)$
#     args: [--standard=PSR1 -p]
#   - id: php-cbf
#     files: \.(php)$
#     args: [--standard=PSR1 -p]
# The tool will fail a build when it has made changes to the staged files. This allows a developer to do a git diff and examine the changes that it has made. Remember that you may omit this if needed with a SKIP=php-cs-fixer git commit.
#   - id: php-cs-fixer
#     files: \.(php)$
#     args: [--level=PSR2]

```


---

```bash

.
├── Pipfile
├── Pipfile.lock
├── bak
│   ├── codecov.yml.bak
│   ├── pc.bak
│   └── readme.bak.md
├── codecov.yml
├── pc
├── readme.md
├── readme.template.md
├── requirements.txt
└── setup.py

1 directory, 11 files
```
