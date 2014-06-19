#!/bin/sh

rm wiki.info

for f in `ls ../wiki/out`
do
	echo `./readWiki.py ../wiki/out/$f` >> wiki.info
done

`./sort.sh wiki.info > wiki.vector`

