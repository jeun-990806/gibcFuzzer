#!/bin/sh
DIR="strace_log/"
DATE=$(date +"%Y%m%d%H%M%S")
LOGFILEPATH="$DIR$DATE.txt"
sh targetSourceCompile.sh
strace -c -o $LOGFILEPATH python main.py
echo "\nstrace result:"
cat $LOGFILEPATH
