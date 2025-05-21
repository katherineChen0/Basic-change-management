#!/usr/bin/python3
import sys
import subprocess
import collections

revision_range = sys.argv[1:]

cmd = ["git", "log", "--pretty=format:%cd", "--date=format:%z"] + revision_range
result = subprocess.run(cmd, capture_output=True, text=True)

timezones = result.stdout.strip().split("\n")

counts = collections.Counter(timezones)
sorted_counts = sorted((int(tz), tz, counts[tz]) for tz in counts)
for _, tz, count in sorted_counts:
    print(f"{tz} {count}")
