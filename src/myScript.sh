#!/bin/sh

#keyword
echo 'search:'
keywords=`./key.py`
echo "keywords: '$keywords'"
'''
#google
alias finalcrawl="cd ~/rank_work_frequency/finalproject"
finalcrawl
rm out/*
finalcrawl
scrapy crawl finalproject -a query="$keywords"
'''
#wiki
alias wikicrawl="cd ~/rank_work_frequency/wiki"
wikicrawl
rm out/wiki*
#I = 1
for key in $keywords
do
	echo $key
	wikicrawl
	scrapy crawl wiki -a query=$key -o "out/wiki.$key" -t json
#	I=$I+1
done
