#!/usr/bin/env python3

import shutil
import psutil

# check disk usage, return ok if free is greater than 20% disk
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

# check cpu usage, return ok if less than 75% usage
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


disk_ok = check_disk_usage('/')
cpu_ok = check_cpu_usage()

if disk_ok and cpu_ok:
    print('Everything is OK Julius!')
else:
    print('Error! Pls check cpu or disk usage')

# if not check_disk_usage("/") or not check_cpu_usage():
#      print("Error!")
# else:
#     print("Everything is OK!")

