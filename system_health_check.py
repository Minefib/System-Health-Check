import shutil
import psutil
import time
import argparse
import os
import sys

def diskSpace(path):
    stat = shutil.disk_usage(path)
    total_size = round(stat.total / 1e9, 2)
    used_size = round(stat.used / 1e9, 2)
    free_size = round(stat.free / 1e9, 2)
    percent_size = round((used_size / total_size) * 100)
    return total_size, used_size, free_size, percent_size


def ramUsage():
    ram = psutil.virtual_memory()
    ramUsed = round(ram.used / 1e9, 2)
    ramTotal = round(ram.total / 1e9, 2)
    ramPercent = round(ram.percent)
    ramFree = round(ram.available / 1e9, 2)

    return ramUsed, ramTotal, ramPercent, ramFree

def uptime(): 
    seconds = int(time.time() - psutil.boot_time())
    hours, rest = divmod(seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return hours, minutes

if __name__ == "__main__":
    def parseArgs():
        parser = argparse.ArgumentParser(description="Print disk, RAM and uptime of this machine")
        parser.add_argument("--path", default="/", help="folder whose disk to check (default: /)")
        parser.add_argument("--limit",type=int, default=90, help="disk percent that triggers a warning (default: 90)")
        args = parser.parse_args()
        return args

    args = parseArgs()
    ramUsed, ramTotal, ramPercent, ramFree = ramUsage()
    hours, minutes = uptime()

    if os.path.isdir(args.path):
        total_size, used_size, free_size, percent_size = diskSpace(args.path)
        if args.limit > 100:
            sys.exit(f"Error: {args.limit} can't be above 100%")
        elif args.limit <= 0:
            sys.exit(f"Error: {args.limit} can't be below 1%")
        else:
            if percent_size > args.limit:
                print(f"----WARNING YOU ARE ABOVE {args.limit}% OF YOUR SIZE----")

        print(f"Disk usage: {used_size} GB / {total_size} GB ({percent_size}%)") 
        print(f"Disk free space: {free_size} GB")

    else:
        sys.exit(f"Erros: {args.path} is not a directory")

    print(f"Ram usage: {ramUsed} GB / {ramTotal} GB ({ramPercent}%)")
    print(f"Ram free: {ramFree} GB")

    print(f"Uptime: {hours}h {minutes}m")

