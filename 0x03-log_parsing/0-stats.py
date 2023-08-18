#!/usr/bin/python3
"""
0-stats
"""
import re
import sys


pattern_match = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'


def process_stdin(line):
    """
    Reads stdin input, checks if its of expected pattern
    """
    match_input = re.match(pattern_match, line)

    if match_input:
        ip_address = match.group(1)
        str_date = match.group(2)
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        return ip_address, str_date, status_code, file_size

    else:
        return None
