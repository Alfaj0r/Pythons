#!/usr/bin/env python3
# https://adventofcode.com/2021/day/1
file = open('./inputday1','r')
contents = file.readlines()
totalmeasurements = len(contents)
tally = 1  #hmmm originally had it at 0, but i was off by 1
for i in range(totalmeasurements):
    if (i > 0) and (i < totalmeasurements):
        if contents[i] > contents[i-1]:
            tally = tally +1
print(tally)