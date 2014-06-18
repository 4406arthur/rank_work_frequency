#!/bin/sh

#keyword
echo 'search:'
keyword=`./key.py`

#google
alias finalcrawl="cd ~/rank_work_frequency/finalproject"
finalcrawl
rm out -r
finalcrawl
scrapy crawl finalproject -a query="$keyword" -o out/test.out -t json

#wiki

#'''
#for key in $(cat './what')
#    scrapy crawl wiki -a query=$(key) -o out/wiki/$(key) -t json
#
#'''
