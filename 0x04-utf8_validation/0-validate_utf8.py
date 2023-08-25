#!/usr/bin/python3
"""
0-validate_utf8
"""


def validUTF8(data):
    """
    determines if a given data set represents a
    valid UTF-8 encoding."""
    try:
        for i in data:
            if not (0 <= i <= 255):
                return False
        data_bytes = bytes(data)

        data_bytes.decode('utf-8')

        return True

    except UnicodeDecodeError:
        return False
