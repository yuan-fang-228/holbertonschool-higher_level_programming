#!/usr/bin/python3
"""101-stats module"""


import sys


def print_stats(stats_size, size):
    print(f"File size: {size}")
    for key in sorted(stats_size):
        if stats_size[key]:
            print(f"{key}: {stats_size[key]}")


if __name__ == "__main__":

    stats_size = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    file_size = 0
    line_count = 0

    try:
        for lines in sys.stdin:
            token = lines.split()
        file_size = file_size + int(token[-1])
        key = token[-2]
        if key in stats_size:
            stats_size[key] += 1
        line_count = line_count + 1
        if line_count % 10 == 0:
            print_stats(stats_size, file_size)
    except KeyboardInterrupt:
        print_stats(stats_size, file_size)
        raise
    print_stats(stats_size, file_size)
