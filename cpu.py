#!/usr/bin/env python3
import psutil
from time import sleep

def get_usage():
    return psutil.cpu_times_percent()

def format_usage(u):
    return "{0:.1f}u {1:.1f}s {2:.1f}w {3:.1f}i ".format(u.user, u.system, u.iowait, u.idle)
sleep(.5)
print(format_usage(get_usage()))
