#!bin/bash

#Working with Arrays in Bash


#this declares the array
NUMBERS=(1 2 3 four 5 six seven "this is eight")


#This prints the first item in the list
echo $NUMBERS

#This prints this is eight because the array counts from 0
echo ${NUMBERS[7]}

#this prints the full array
echo ${NUMBERS[@]}

#this prints the number of indexes in the array
echo ${#NUMBERS[@]}

#this counts the number of indexes
echo ${!NUMBERS[@]}

#This adds to the array
NUMBERS+=(10)

#print new addition
echo ${NUMBERS[8]}

#this prints a subset of the array
echo ${NUMBERS[@]:4:7}





