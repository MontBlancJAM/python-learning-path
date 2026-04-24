#!/usr/bin/env python3

import os
import shutil

# open a file, put all contents in a variable, close the file
# this will allow us to get the contents one time, and manipulate
# the contents by assigning contents to a variable

# it isn't recommended to use this method for large files or system logs
# if file is too large, variable holding the contents would consume memory

file = open('/etc/hosts')
lines = file.readlines()
file.close

print(lines)