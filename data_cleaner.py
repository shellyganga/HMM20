#!/usr/bin/env python
# coding: utf-8
import re
import numpy as np
import sys

# Reading the data from the text file
if len(sys.argv) != 2:
    raise RuntimeError('Input Error: Requires the name of the data file you want to run.')
file_name = sys.argv[1]
with open(file_name) as f:
    raw_text = f.readlines()
data = [line.strip() for line in raw_text]

# Parsing data
variables = ('meanSignalLenght', 'amplCor', 'syncVar', 'metr6.velSum')
all_data = [[] for _ in variables]

for line in data:
    for i, variable in enumerate(variables):
        match = re.search('{} = ([0-9]+.[0-9]+) '.format(variable), line)
        if match:
            all_data[i].append(float(match.group(1)))


# Cutting out outliers
def trim_outliers(data, percentile):
    '''
    removes all numbers below and above a certain percentile, given a list of numbers
    returns a list of trimmed values

    data: a list of numbers you want to trim; the data can be unsorted
    percentile: the percentile in the form n% = n which you want to cut off the data
    '''
    data = np.array(data)
    lower_trimmed = [i for i in data if i >= np.percentile(data, percentile)]
    return [i for i in lower_trimmed if i <= np.percentile(data, 100 - percentile)]


all_trimmed_data = [trim_outliers(data, 5) for data in all_data]

# Displaying Data
for i, all_data in enumerate(all_data):
    print('*** Data for', variables[i], '***')
    print('Max: {}'.format(max(all_data)))
    print('Min: {}'.format(min(all_data)))
    print('------------------------------------------------------')
