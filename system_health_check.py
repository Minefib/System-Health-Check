import shutil
import psutil
import time
import os


def uptime(): 
    seconds = int(time.time() - psutil.boot_time())
    hours, rest = divmod(seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return hours, minutes

def diskSpace():
    path = "/"
    stat = shutil.disk_usage(path)
    total_size = round(stat.total / 1e9, 2)
    used_size = round(stat.used / 1e9, 2)
    free_size = round(stat.free / 1e9, 2)
    return total_size, used_size, free_size


def ramUsage():
    ram = psutil.virtual_memory()
    ramUsed = round(ram.used / 1e9, 2)
    ramTotal = round(ram.total / 1e9, 2)
    ramPercent = round(ram.percent)
    ramFree = round(ram.available / 1e9, 2)

    return ramUsed, ramTotal, ramPercent, ramFree

total_size, used_size, free_size = diskSpace()
ramUsed, ramTotal, ramPercent, ramFree = ramUsage()
hours, minutes = uptime()

print(f"Disk total space: {total_size} GB") 
print(f"Disk used space: {used_size} GB")
print(f"Disk free space: {free_size} GB")


print(f"Ram usage: {ramUsed} / {ramTotal} ({ramPercent}%)")
print(f"Ram free: {ramFree}")

print(f"Uptime: {hours}h {minutes}m")

