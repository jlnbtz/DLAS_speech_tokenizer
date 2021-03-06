# -*- coding: utf-8 -*-

# Filename: progress.py
# Author: Julian Betz
# Created: 2018-06-23
# Version: 2019-01-24
#
# Description: Provides a progress bar.

import math
import sys

def print_bar(part, whole, length, prefix='', suffix='', delimiter='\r', end='\n'):
    number = part / whole * length
    floor = math.floor(number)
    sys.stdout.write(prefix + '█' * floor)
    rest = number - floor
    if part < whole:
        if rest < 0.125:
            sys.stdout.write(' ')
        elif rest < 0.25:
            sys.stdout.write('▏')
        elif rest < 0.375:
            sys.stdout.write('▎')
        elif rest < 0.5:
            sys.stdout.write('▍')
        elif rest < 0.625:
            sys.stdout.write('▌')
        elif rest < 0.75:
            sys.stdout.write('▋')
        elif rest < 0.875:
            sys.stdout.write('▊')
        else:
            sys.stdout.write('▉')
    print(' ' * (length - floor - 1) + suffix, end=delimiter if part < whole else end)

# progress.py ends here
