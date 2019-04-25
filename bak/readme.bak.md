# pc version 0.7.2

---

## pre-commit repo automation for macOS

```bash


###############################################################################
# pc : pre-commit repo automation for macOS (version 0.7.2)

# author    - Michael Treanor  <skeptycal@gmail.com>
# copyright - 2019 (c) Michael Treanor
# license   - MIT <https://opensource.org/licenses/MIT>
# github    - https://www.github.com/skeptycal

# Usage: pc {init|version|help}

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


# Sample yaml template ########################################################
default_language_version:
    python: python3.7
default_stages: [commit, push]
exclude: '^$'
fail_fast: false
repos:
-   repo: git://github.com/pre-commit/pre-commit-hooks
    sha: master
    hooks:
    -   id: check-added-large-files
    -   id: check-byte-order-marker
    -   id: check-docstring-first
    -   id: check-case-conflict
    -   id: check-json
    -   id: check-merge-conflict
    -   id: check-symlinks
    -   id: check-yaml
#   -   id: detect-aws-credentials
    -   id: detect-private-key
    -   id: end-of-file-fixer
    -   id: flake8
    -   id: pretty-format-json
    -   id: requirements-txt-fixer
    -   id: trailing-whitespace
-   repo: git://github.com/pre-commit/mirrors-pylint
    sha: master
    hooks:
    -   id: pylint

```
