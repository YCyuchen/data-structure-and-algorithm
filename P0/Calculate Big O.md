# Calculate Big O
#### Task 0
**Big O** for the first record of texts:
Ans:$O(n+3)$,   as n=1->O(1)
**Big O** the last record of calls:
Ans:O(n+4), as n=5213, and n is a constant -> O(1)
_Question：can python list get the last element directly? Say in this task, we can use a pointer to point the last element of calls instead of looping from the very begining?_
  
#### Task 1 
**Big O** for calculating different telephone numbers in the records
Ans: firstly loop each line in texts and calls, secondly loop the unique_numbers list to judge if  current number is in the  list -> $ O(2n^2)=  O(n^2) $. 

### Task2
**Big O** for print the  number spent the longest time on the phone
Ans: firstly loop each line in texts and calls, Secondly judge if it's the biggest and define the new value -> $O(n+3)=O(n)$

### Task3
Part1: **Big O** for finding all of the area codes and mobile prefixes called by people in Bangalore
Ans:$O(n^2)$
Part2:  **Big O** calculating the percent of calls from Bangalore are calls to Bangalore.
Ans:$O(n+2) = O(n)$
### Task4 
 **Big O**  for Creating a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts, receive texts or receive incoming calls.

Firstly 
```
for line in calls:
    out_calls.append(line[0])
    in_calls.append(line[1])

for line in texts:
    send_texts.append(line[0])
    receive_texts.append(line[1])
```
$O(2n)+O(2n)$ -> O(n)

Secondly
```
for phoneNumber in out_calls:
    if (phoneNumber not in in_calls) and (phoneNumber not in send_texts) and (phoneNumber not in receive_texts):
        telemarketers.append(phoneNumber)
```
$O(n^3)$ -> O(n^3) 

Ans:$ O(n)+O(n^3)=O(n^3)$