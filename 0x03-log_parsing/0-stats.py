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
        ip_address = match_input.group(1)
        str_date = match_input.group(2)
        status_code = int(match_input.group(3))
        file_size = int(match_input.group(4))

        return ip_address, str_date, status_code, file_size

    else:
        return None


def process_data():
    """Process data from process_stdin"""
    try:
        while True:
            # Read input from stdin
            input_line = input()
            # process input
            data = process_stdin(input_line)
            if data:
                ip_address, str_date, status_code, file_size = data
                print('Ip Address {}'.format(ip_address))
                print('Date String {}'.format(str_date))
                print('Status Code {}'.format(status_code))
                print('File size {}'.format(file_size))

    except KeyboardInterrupt:
        print('There was a keyboard interupt')
        sys.exit()


if __name__ == '__main__':
    process_data()
