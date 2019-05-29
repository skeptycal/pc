# pc version 1.2.1
\n[![Netlify Status](https://api.netlify.com/api/v1/badges/416b8ca3-82db-470f-9adf-a6d06264ca75/deploy-status)](https://app.netlify.com/sites/mystifying-keller-ab5658/deploys)  ![Azure DevOps builds](https://img.shields.io/azure-devops/build/skeptycal0275/skeptycal/1.svg?color=blue&label=Azure%20DevOps&style=popout) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask.svg?color=Yellow&label=Python&style=popout) ![Twitter Follow](https://img.shields.io/twitter/follow/skeptycal.svg?label=%40skeptycal&style=social) ![GitHub followers](https://img.shields.io/github/followers/skeptycal.svg?style=social)\n
Last update: 05-13-2019 | 09:14:53
\n---\n
## pre-commit and auto deploy on macOS\n
```bash\n

###############################################################################
# pc : pre-commit and auto deploy on macOS (version 1.2.1)

# author    - Michael Treanor  <skeptycal@gmail.com>
# copyright - 2019 (c) Michael Treanor
# license   - MIT <https://opensource.org/licenses/MIT>
# github    - https://www.github.com/skeptycal

# Usage: pc {init|reset|version|help}

#   Parameters:
#       [init, -i, --init]        -- install and initialize
#       [commit, -m] MESSAGE      -- git commit and push with MESSAGE
#       [reset, -r, --reset]      -- reset initial repo files (with backup)
#       [version, -v, --version]  -- display version information
#       [help, -h, --help]        -- display usage and information

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


```\n
\n---\n
```bash\n
.
├── Pipfile
├── Pipfile.lock
├── bak
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── README.md.bak
│   ├── baklist.txt
│   ├── codecov.yml
│   ├── pc
│   ├── readme.md
│   ├── readme.template.md
│   ├── requirements.txt
│   ├── script_example.md
│   └── setup.py
├── bitbucket-pipelines.yml
├── build
│   └── bdist.macosx-10.14-x86_64
├── codecov.yml
├── dist
│   └── skeptycal.github.io-0.1.0-py3.7.egg
├── gpg_public.txt
├── pc
├── readme.md
├── readme.template.md
├── requirements.txt
├── script_example.md
├── setup.py
├── skeptycal.github.io.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
└── static
    └── license-MIT-blue.svg

6 directories, 28 files
```\n
