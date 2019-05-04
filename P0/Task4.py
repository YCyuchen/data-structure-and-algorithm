"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
out_calls, in_calls, send_texts, receive_texts = [], [], [], []
telemarketers = []
for line in calls:
    out_calls.append(line[0])
    in_calls.append(line[1])

for line in texts:
    send_texts.append(line[0])
    receive_texts.append(line[1])

for phoneNumber in out_calls:
    if (phoneNumber not in in_calls) and (phoneNumber not in send_texts) and (phoneNumber not in receive_texts):
        telemarketers.append(phoneNumber)

set(telemarketers)
print("These numbers could be telemarketers: ")
for phoneNumber in telemarketers:
    print(phoneNumber)

