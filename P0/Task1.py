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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_numbers = []

for line in texts:
    if line[0] not in unique_numbers:
        unique_numbers.append(line[0])
    if line[1] not in unique_numbers:
        unique_numbers.append(line[1])

for line in calls:
    if line[0] not in unique_numbers:
        unique_numbers.append(line[0])
    if line[1] not in unique_numbers:
        unique_numbers.append(line[1])

print("There are {} different telephone numbers in the records".format(len(unique_numbers)))

# np_texts = np.asarray(texts)
# np_calls = np.asarray(calls)
# unique_numbers = set(np_texts[:, 0] + np_texts[:, 1] + np_calls[:, 0] + np_calls[:, 1])
