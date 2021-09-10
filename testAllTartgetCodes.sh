#!/bin/sh

TARGET_CODE_PATH='com'

for TARGET in $TARGET_CODE_PATH/*
do
	echo > /sys/kernel/debug/tracing/trace
	TARGET_FILE=${TARGET##*/}
	TARGET_FUNCTION=${TARGET_FILE%.*}
	echo "$TARGET_FUNCTION"	
	timeout 20 python3 main.py "$TARGET" "$TARGET_FUNCTION"
done
