#!/usr/bin/python3

"""
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0  # initializes size to zero
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_codes = {}  # creates a dictionary of status codes

    count = 0

    try:
        for line in sys.stdin:  # read each lines from standard input
            if count == 10:  # if the lines are 10 in number
                print_stats(size, status_codes)  # print the status
                count = 1
            else:
                count += 1

            line = line.split()  # split the logs using generic spaces

            try:
                size += int(line[-1])  # convert the last value to int and add to size
            except (IndexError, ValueError):  #catch errors
                pass  # ignore if errors are raised

            try:
                if line[-2] in valid_codes:  # check if the status_codes are valid_codes
                    if status_codes.get(line[-2], -1) == -1:  # chks if a key is not present
                        # creates the k:v pair 
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1  # if present increase the value by 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
