#/bin/bash
OUTPUTFILENAME="result"
function calculate_weight() {
weight=0 
while read line_keyword      
do           
    while read line_web
    do
        keyword=$(echo $line_keyword | tr -cd '[[:alpha:]]' | tr '[[:upper:]]' '[[:lower:]]' )
        word=$(echo $line_web | tr -cd '[[:alpha:]]' | tr '[[:upper:]]' '[[:lower:]]' )
        if [ "$keyword"x == "$word"x ]; then
            num=$(echo $line_keyword | tr -cd '[[:digit:]]')
            num2=$(echo $line_web | tr -cd '[[:digit:]]')
	    weight=$(( $weight + $num * $num2 ))
	    #echo "$keyword" . "$(( $num * $num2 ))"
        fi
    done < $2
done < $1

echo -n "$weight"

}

p="websKey"
#echo "$p/web.1"
calculate_weight "wiki.vector" "$p/web.1" > $OUTPUTFILENAME
#echo "$p/web.1 finish"
echo " web.1" >> $OUTPUTFILENAME
for i in $(seq -f '%01g' 2 $1)
do
    #echo "web$1 running.."
    #echo "$p/web.${i}"
    calculate_weight "wiki.vector" "$p/web.${i}" >> $OUTPUTFILENAME
    echo " web.${i}" >> $OUTPUTFILENAME
    #echo "web$i"
done

sort -n -r $OUTPUTFILENAME > r
fin=$(sed -n '1p' < r | cut -d ' ' -f 2)
rm $OUTPUTFILENAME r
cp "$p/$fin" result
echo $fin
