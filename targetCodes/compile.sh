#!/bin/sh
CURRENTPATH=$(dirname $(realpath $0))

for entry in $CURRENTPATH/*
do
	FILENAME=${entry%%.*}
	FILENAME=${FILENAME##*/}
	SRC="$FILENAME.c"
	DES="sharedLibs/$FILENAME.so"
	cc -fPIC -shared -o $DES $SRC
done

