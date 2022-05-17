import pandas as pd
import plotly_express as px
import csv
from collections import Counter

with open('SOCR-HeightWeight.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()
total = 0

for x in new_data:
    total+=x

mean = total/n
print("Mean Average is " + str(mean))

if n % 2 == 0:
    median1 = new_data[n//2]
    median2 = new_data[n//2 - 1]
    median = (median1 + median2)//2

else:
    median = new_data[n//2]

print("The median is: " + str(median))

data = Counter(new_data)

mode_of_data_range={
    '75-85': 0,
    '85-95': 0,
    '95-105': 0,
    '105-115': 0,
    '115-125': 0,
    '125-135': 0,
    '135-145': 0,
    '145-155': 0,
    '155-165': 0,
    '165-175': 0
}

for weight,occurence in data.items():
    if 75<weight<85:
        mode_of_data_range['75-85'] += occurence
    if 85<weight<95:
        mode_of_data_range['85-95'] += occurence
    if 95<weight<105:
        mode_of_data_range['95-105'] += occurence
    if 105<weight<115:
        mode_of_data_range['105-115'] += occurence
    if 115<weight<125:
        mode_of_data_range['115-125'] += occurence
    if 125<weight<135:
        mode_of_data_range['125-135'] += occurence
    if 135<weight<145:
        mode_of_data_range['135-145'] += occurence
    if 145<weight<155:
        mode_of_data_range['145-155'] += occurence
    if 155<weight<165:
        mode_of_data_range['155-165'] += occurence
    if 165<weight<175:
        mode_of_data_range['165-175'] += occurence

mode_range=0
mode_occurence=0

for range,occurence in mode_of_data_range.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
        mode = float((mode_range[0]+mode_range[1]) / 2)

print("The mode is : " + str(mode))