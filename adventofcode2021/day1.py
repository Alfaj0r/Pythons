#!/usr/bin/env python3
# https://adventofcode.com/2021/day/1
file = open('./inputday1','r')
contents = file.readlines()
totalmeasurements = len(contents)
for i in range(totalmeasurements):
    if (i > 0) and (i < 5):
        print(contents[i-1])
        #if contents[i] > contents[i-1]:
         #   increasetally +=1
    
