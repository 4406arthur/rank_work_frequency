#/bin/sh
cat $1 | \
tr -d '[:punct:]' | \
tr ' ' '\n' | \
tr 'A-Z' 'a-z' | \
sort | \
uniq -c | \
sort -rn
