#!/usr/bin/env python3

#looks for a matching letter, replaces it with another one
name = 'Julius'
new_name = ''
for c in name:
    if c == 's':
        c = '$'
    new_name += c

print(new_name)