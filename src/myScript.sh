#!/bin/sh

#keyword


#google
scrapy crawl finalproject -a query=$(cat './what') -o out/test.out -t json
#'''
#for key in $(cat './what')
#    scrapy crawl wiki -a query=$(key) -o out/wiki/$(key) -t json
#
#'''
