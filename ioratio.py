#!/usr/bin/env python3
# ioratio.py
#
# A python utility to show percentage of read & write utilization for disks
#
# Disk usage data is gathered from /proc/diskstats & then
# processed accordingly.
#
# License: MIT
# Author: Ricky Hewitt <contact@rickyhewitt.dev>

import time
import os
from tabulate import tabulate
import argparse


def main(device):
    stats = []

    with open('/proc/diskstats') as infile:
        for line in infile:
            disk = line.split()[2]
            if not disk.startswith(device):
                continue

            reads = int(line.split()[3])
            writes = int(line.split()[7])
            try:
                read_ratio = float((reads / (reads+writes))*100)
                write_ratio = float((writes / (reads+writes))*100)
            except ZeroDivisionError:
                continue

            stats.append([disk, reads, writes, "%.2f" % read_ratio, "%.2f" % write_ratio])


    header = ['Disk', 'Reads', 'Writes', 'Read Ratio (%)', 'Write Ratio (%)']
    data = [header] + list(stats)

    for i, d in enumerate(data):
        line = ' | '.join(str(x).ljust(14) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('device', nargs='?', default='/dev/sd', help="e.g. /dev/sda5")
    args = parser.parse_args()

    device = args.device.replace('/dev/', '')
    
    main(device)
