#!/bin/bash
# This script will loop the numbers 1-10. 

counter=1
while [ $counter -le 10] ]
do
	echo $counter
	((counter ++))
done

echo All done