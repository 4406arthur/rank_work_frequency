#!/bin/sh

rm websKey/* -f

for file in `ls ../finalproject/out`
do
    echo "`./readGg.py ../finalproject/out/$file`" > websKey/$file
    echo "`./sort.sh websKey/$file`" > websKey/key.$file
done
