#!/usr/bin/env python3

import os
import shutil

#opens up the linux hosts file and prints contents on terminal
with open("/etc/hosts") as file:
    print(file.read())
