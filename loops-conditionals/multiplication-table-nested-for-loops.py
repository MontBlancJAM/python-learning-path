#!/usr/bin/env python3

#multiplication table up to 12 using nested for loops
#using f' statements for clean string output

for number in range(12):
    number+=1
    for multiplier in range(12):
        multiplier+=1
        result = number*multiplier
        print(f'{number} x {multiplier} = {result}')
    print('---')