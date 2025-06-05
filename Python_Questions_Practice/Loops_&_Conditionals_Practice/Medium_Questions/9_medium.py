# Use a loop with  continue and  break to skip even numbers and stop at 25.

for i in range(1, 51):
    
    if i % 2 == 0:  # skip even numbers
        continue
    if i == 25:     # stop loop when i is 25
        break

    print(i)