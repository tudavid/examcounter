file="/home/shadowrunner/Programme/BashSkripte/examdates"
counter=0;
while read line;
do 
IFS=';' read -ra ADDR <<< "$line"
	for i in "${ADDR[@]}"; do
		if [ `expr $counter % 2` -eq 1 ];  then
			current_date=$(date +%s)
			exam_date=$(date --date="$i" +%s)
			secondsleft=$(($exam_date - $current_date))
			days=$(($secondsleft/86400))
			hours=$(($secondsleft%86400/3600)) 
			minutes=$(($secondsleft%3600/60))
			seconds=$(($secondsleft%60))
		
		fi
		if [ `expr $counter % 2` -eq 0 ];  then
			name=$i		
		fi 
		counter=$[counter+1]
	done
echo $name $days $hours $minutes $seconds
done<$file
