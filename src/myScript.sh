#!/bin/sh

alias CDreturn="cd ~/rank_work_frequency/src"
#keyword
echo 'search:'
keywords=`./key.py`
echo "keywords: '$keywords'"

#google
alias finalcrawl="cd ~/rank_work_frequency/finalproject"
finalcrawl
rm out/* -f
scrapy crawl finalproject -a query="$keywords"

#wiki
alias wikicrawl="cd ~/rank_work_frequency/wiki"
wikicrawl
rm out/* -f
i = 1
for key in $keywords
do
	i=$(($i+1))
	scrapy crawl wiki -a query=$key -o "out/wiki.${i}" -t json
done
#compute vector
CDreturn
rm wiki.info -f
for f in `ls ../wiki/out`
do
	echo `./readWiki.py ../wiki/out/$f` >> wiki.info
done
#sort wiki.vector
`./sort.sh wiki.info > wiki.vector`

