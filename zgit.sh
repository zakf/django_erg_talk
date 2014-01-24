#!/bin/bash
# 
# File: zgit.sh
# 
# Helpful Git shortcuts
# 
# To use this file:
# sh> source zgit.sh
# 
# You may want to add this file to your PATH. Maybe add it as a soft link 
# (a symbolic link) using the command 'ln -s actual_file link_name' in a 
# directory which is already on PATH, such as /usr/local/bin.
# 
# Here is how I made the soft link (symbolic link) on my Mac:
# mac> cd /usr/local/bin
# mac> sudo ln -s /Users/zakf/progs/zgit.sh zgit.sh

function gss {
    git status -s
    curr_time.py
}

alias gas="git add *"
    # WARNING: git add * does NOT add deleted items. You need either 
    # git add -u or git add -A.

alias gaA="git add -A"
    # This is better than 'gas' when you have deleted or renamed things.

alias gcm="git commit -m"

alias gcr="git commit -m \"Routine commit\""

function gcar {
    # Doing "git add *" is better than doing "git commit -a" because 
    # "git commit -a" will only add M files (modified existing files), but 
    # "git add *" will additionally add ?? files (new unknown files). It 
    # is confusing to me that "git commit -a" is more limited than 
    # "git add *", but whatever.
    
    git add *
    git commit -m "Routine commit"
}

alias gdiff="GIT_PAGER='' git diff"

alias gdnum="git diff --numstat"

alias gsl="git shortlog -sn"

function ghelp {
    if [ ! "$1" ]   # Did the first argument exist?
    then
        # ghelp was called with no arguments
        echo "New commands:"
        echo "    ghelp - Print this help message"
        echo "    ghelp {{ command }} - Print information about {{ command }}" 
        echo "    gss - Status"
        echo "    gas - Add *"
        echo "    gaA - git add -A    # Use with caution"
        echo "    gcm - Commit -m"
        echo "    gcr - Routine commit"
        echo "    gcar - gas then gcr"
        echo "    gdiff - git diff"
        echo "    gdnum - git diff --numstat"
        echo "    gsl - Count all commits"
        echo
        echo "Good arguments for gdiff and gdnum:"
        echo "    [no arg] - Working copy vs. staging area"
        echo "    --cached - Staging area vs. latest commit"
        echo "    HEAD     - Working copy vs. latest commit"
        echo
        echo "    # Latest commit is *usually* synonymous with HEAD."
        echo "    # Staging area is synonymous with index and cache."
        echo
        echo "    # Working copy --> Staging area --> Commit"
        echo "    # HEAD = [no arg] + --cached"
    elif [ "$1" == "gdiff" ]
    then
        echo "gdiff - Help:"
        echo
        echo "# Example 1:"
        echo "# Do a diff of all files, working copy vs. latest commit:"
        echo
        echo "mac> gdiff HEAD"
        echo
        echo "# Example 2:"
        echo "# Do a diff of one file, staged version vs. latest commit:"
        echo
        echo "mac> gdiff --cached trunk/my_file.txt"
    else
        echo "Unrecognized zgit.sh command: $1"
    fi
}

ghelp
