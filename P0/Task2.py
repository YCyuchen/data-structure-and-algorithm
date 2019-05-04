"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
longest_time = 0.0
for line in calls:
    if float(line[3]) > longest_time:
        telephone_number = line[0]
        longest_time = float(line[3])

print("{} spent the longest time {} seconds on the phone during September 2016.".format(telephone_number, longest_time))
