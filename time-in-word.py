#!/bin/python3
#import num2word
import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    numbers = ("zero one two three four five six seven eight nine").split()
    numbers.extend("ten eleven twelve thirteen fourteen fifteen sixteen".split())
    numbers.extend("seventeen eighteen nineteen".split())
    numbers.extend(tens if ones == "zero" else (tens + " " + ones) 
    for tens in "twenty thirty forty fifty sixty seventy eighty ninety".split() for ones    in numbers[0:10])
    if m==00:
        return(numbers[h]+ " o' clock")
    elif m==15:
        return("quarter past "+numbers[h])
    elif m==30:
        return("half past "+numbers[h])
    elif m==45:
        h=h+1
        return("quarter of "+numbers[h])
    elif m>45:
        h=h+1
        m=60-m
        return(numbers[m] +" minutes to "+ numbers[h])
    else:
        return(numbers[m] ," minutes past ",numbers[h])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
