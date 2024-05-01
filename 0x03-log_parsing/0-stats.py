#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys


"""Parses a line of input and returns the IP address, status code, and file size."""
def parse_line(line):
    parts = line.split()
    if len(parts) != 7:
        return None
    ip_address = parts[0]
    status_code = parts[-3]
    file_size = int(parts[-2])
    return ip_address, status_code, file_size

def print_statistics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

def main():
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            data = parse_line(line.strip())
            if data:
                ip_address, status_code, file_size = data
                total_size += file_size
                status_counts[status_code] += 1
                lines_processed += 1

                if lines_processed % 10 == 0:
                    print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
