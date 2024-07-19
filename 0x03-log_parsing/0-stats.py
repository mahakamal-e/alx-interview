#!/usr/bin/python3
"""
This script reads log lines from standard input,
extracts relevant data, and computes statistics.
"""

import sys
import signal
import re

log_pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) - \['
    r'(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
)

# Define global variables
file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

def process_line(line, status_codes, itr_num, file_size):
    """
    Process a single line of the log and update metrics.

    Args:
        line (str): The log line to process.
        status_codes (dict): Dictionary to count status codes.
        itr_num (int): Number of valid lines processed.
        file_size (int): Total file size processed.

    Returns:
        tuple: Updated values of itr_num and file_size.
    """
    match = log_pattern.match(line)

    if match:
        _, _, status_code_str, file_size_str = match.groups()

        if status_code_str in status_codes:
            status_codes[status_code_str] += 1
            file_size += int(file_size_str)
            itr_num += 1

    return itr_num, file_size

def print_statistics(file_size, status_codes):
    """
    Print the statistics of file size and status codes.

    Args:
        file_size (int): Total file size processed.
        status_codes (dict): Dictionary of status code counts.
    """
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption and print metrics."""
    global file_size
    global status_codes
    print_statistics(file_size, status_codes)
    sys.exit(0)

def main():
    """Starting point for the log parser"""
    global file_size
    global status_codes

    itr_num = 0
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            itr_num, file_size = process_line(line,
                                              status_codes,
                                              itr_num,
                                              file_size)

            if itr_num % 10 == 0:
                print_statistics(file_size, status_codes)

        print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()
