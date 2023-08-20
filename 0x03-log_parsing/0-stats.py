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
status_codes_dict = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
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


def process_data():
    """Process data from process_stdin"""
    try:
        global total_file_size
        global no_lines
        # Create a list to store processed data
        data_list = []
        while True:
            # Read input from stdin
            input_line = input()
            # process input
            data = process_stdin(input_line)
            if data:
                # Append processed data to the lis
                data_list.append(data)
                for item in data_list:
                    if item[2] in status_codes and isinstance(item[2], int):
                        status_codes_dict[item[2]] += 1
                    total_file_size += item[3]
                    no_lines += 1
                if no_lines % 10 == 0:
                    print_data()

    except KeyboardInterrupt:
        print_data()
        sys.exit()


def print_data():
    """Printss the metrics after data"""
    print('File size: {}'.format(total_file_size))
    for code, count in status_codes_dict.items():
        print('{}: {}'.format(code, count))


if __name__ == '__main__':
    process_data()
