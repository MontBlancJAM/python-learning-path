#!/usr/bin/env python3

import os
import shutil

#iterating through file contents after opening it

with open('/etc/hosts') as file:
    for line in file:
        print(line.lower())


#print it again but this time formatting it
with open('/etc/hosts') as file:
    for line in file:
        print(line.strip().upper())