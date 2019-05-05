"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import OrderedDict

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
timeSummary_dict = OrderedDict()
for line in calls:
    caller, receiver = line[0], line[1]
    time = int(line[3])

    if caller in timeSummary_dict.keys():
        timeSummary_dict[caller] += time
    else:
        timeSummary_dict[caller] = time

    if receiver in timeSummary_dict.keys():
        timeSummary_dict[receiver] += time
    else:
        timeSummary_dict[receiver] = time

timeSummary_dict = sorted(timeSummary_dict.items(), key=lambda x: x[1])
longestTime_number = timeSummary_dict[-1][0]
longestTime = timeSummary_dict[-1][1]

print("{0} spents the longest time {1} seconds, on the phone during Sep 2016".format(longestTime_number, longestTime))
