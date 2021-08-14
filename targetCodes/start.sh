#!/bin/sh
DIR="strace_log/"
DATE=$(date +"%Y%m%d%H%M%S")
LOGFILENAME="$DIR$DATE"

for i in 1 2 3 4 5 6 7 8 9 10
do
	FUNCTION=$(python targetCodeGenerator.py)
	sh targetSourceCompile.sh
	for j in 1 2 3 4 5
	do
		strace -c -o "$DIR$FUNCTION($j).txt" python main.py
		echo "\n$FUNCTION strace result:"
		cat "$DIR/$FUNCTION($j).txt"
	done
done
