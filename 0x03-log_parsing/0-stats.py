#!/usr/bin/python3
"""
0-stats
"""
import re
import sys


pattern_match = (
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
)
total_file_size = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_codes_dict = {code: 0 for code in status_codes}
no_lines = 0


def process_stdin(line):
    """
    Reads stdin input, checks if its of expected pattern
    """
    match_input = re.match(pattern_match, line)

    if match_input:
        ip_address = match_input.group(1)
        str_date = match_input.group(2)
        status_code = int(match_input.group(3))
        file_size = int(match_input.group(4))

        return ip_address, str_date, status_code, file_size

    else:
        return None


def print_data():
    """Prints the metrics after data"""
    print('File size: {}'.format(total_file_size))
    for code, count in sorted(status_codes_dict.items()):
        if count > 0:
            print('{}: {}'.format(code, count))


try:
    for line in sys.stdin:
        data = process_stdin(line)
        if data:
            ip_address, str_date, status_code, file_size = data

            total_file_size += file_size
            no_lines += 1
            if status_code in status_codes and isinstance(status_code, int):
                status_codes_dict[status_code] += 1
            if no_lines % 10 == 0:
                print_data()

except KeyboardInterrupt:
    print_data()
    sys.exit()
