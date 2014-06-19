#!/bin/sh

rm websKey/* -f

for file in `ls ../finalproject/out`
do
#    echo $file
    echo "`./readGg.py ../finalproject/out/$file`" > websKey/$file
    `./sort.sh websKey/$file > websKey/$file`
done
