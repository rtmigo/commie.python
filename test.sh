#!/bin/bash
set -e

thisFileParentDir="$(dirname "$(perl -MCwd -e 'print Cwd::abs_path shift' "$0")")"
cd "$thisFileParentDir"

nosetests --all-modules
# python3 setup.py test