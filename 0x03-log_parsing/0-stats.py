#!/usr/bin/python3
"""
This script reads log lines from standard input,
extracts relevant data, and computes statistics.
"""
import re
import sys


def parse_log_line(log_line):
    """
    Extracts relevant data from a log line.

    Args:
        log_line (str): A single line from the log input.

    Returns:
        tuple: A tuple containing the response code and the response size.
    """
    patterns = (
        r"\s*(?P<ip_address>\S+)\s*",
        r"\s*\[(?P<timestamp>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]",
        r'\s*"(?P<request_details>[^"]*)"\s*',
        r"\s*(?P<response_code>\S+)",
        r"\s*(?P<response_size>\d+)(?:\s*(?P<additional_info>\S*))?",
    )

    response_code = '0'
    response_size = 0

    log_format = "{}\\-{}{}{}{}\\s*".format(patterns[0],
                                            patterns[1],
                                            patterns[2],
                                            patterns[3],
                                            patterns[4])
    match = re.fullmatch(log_format, log_line)
    if match:
        response_code = match.group("response_code")
        response_size = int(match.group("response_size"))

    return response_code, response_size


def handle_log_line(log_line, code_counts, total_lines, total_size):
    """
    Update metrics based on a single log line.

    Args:
        log_line (str): A single line from the log input.
        code_counts (dict): Dictionary of counts for each status code.
        total_lines (int): Total number of lines processed.
        total_size (int): Total size of responses processed.

    Returns:
        tuple: Updated total number of lines and total size.
    """
    response_code, extracted_size = parse_log_line(log_line)

    if response_code in code_counts:
        code_counts[response_code] += 1

    total_lines += 1
    total_size += extracted_size
    return total_lines, total_size


def display_metrics(total_size, code_counts):
    """
    Display the total file size and status code counts.

    Args:
        total_size (int): Total size of responses processed.
        code_counts (dict): Dictionary of counts for each status code.
    """
    print(f"File size: {total_size}")

    non_zero_counts = {
        code: count
        for code, count in code_counts.items()
        if count > 0
    }

    sorted_counts = sorted(non_zero_counts.items())

    for code, count in sorted_counts:
        print(f'{code}: {count}')


def main():
    """Main function to parse log lines and compute metrics."""
    total_lines = 0
    code_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    total_size = 0

    try:
        for log_line in sys.stdin:
            total_lines, total_size = handle_log_line(log_line,
                                                      code_counts,
                                                      total_lines,
                                                      total_size)

            if total_lines % 10 == 0:
                display_metrics(total_size, code_counts)

        display_metrics(total_size, code_counts)

    except KeyboardInterrupt:
        display_metrics(total_size, code_counts)
        raise


if __name__ == '__main__':
    main()
