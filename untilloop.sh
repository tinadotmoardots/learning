#!/bin/bash
# This will count to 10 using an until loop.

counter=1

until [ $counter -gt 10 ]
do
	echo $counter
	((counter++))
done

echo All done