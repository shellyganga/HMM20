#!/usr/bin/env python
# coding: utf-8
import re
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math
# Reading the data from the text file


if len(sys.argv) != 2:
    raise RuntimeError('Input Error: Requires the name of the data file you want to run.')
file_name = sys.argv[1]
with open(file_name) as f:
    raw_text = f.readlines()
data = [line.strip() for line in raw_text]

with open('newfile.txt') as f:
    raw_text2 = f.readlines()
data2 = [line.strip() for line in raw_text2]
# Parsing data
# possible operational indicators: meanSignalLenght', 'amplCor', 'syncVar', 'metr6.velSum'
# insert into variable
variable = ('metr6.velSum')
all_data = [1]
all_data2 = [1]

for line in data:
    match = re.search('{} = ([0-9]+.[0-9]+) '.format(variable), line)
    if match:
        all_data.append(float(match.group(1)))

for line in data2:
    match = re.search('{} = ([0-9]+.[0-9]+) '.format(variable), line)
    if match:
        all_data2.append(float(match.group(1)))
# histogram

# Colours for different percentiles
perc_50_colour = 'mediumaquamarine'

# Plot the Histogram from the random data
x = np.arange(min(all_data2), max(all_data2),0.5)
# fig, ax, counts, patches, bins = plt.hist(all_data, bins, facecolor= 'blue', alpha=0.5)
fig, ax = plt.subplots(figsize=(10, 10))
counts, bins, patches = ax.hist(all_data, bins=x, range=[min(all_data2), max(all_data)], facecolor=perc_50_colour, edgecolor='gray')
# Set the ticks to be at the edges of the bins.
plt.xticks(np.arange(min(all_data2), max(all_data2)+.5, .5))
plt.xticks(rotation=70)

# Set the graph title and axes titles
plt.ylabel('Count', fontsize=15)
plt.xlabel('value of ' + variable + ' given ' + file_name, fontsize=15)

# Calculate bar centre to display the count of data points and %
bin_x_centers = 0.5 * np.diff(bins) + bins[:-1]
bin_y_centers = ax.get_yticks()[1] * 0.2
# Display the the count of data points and % for each bar in histogram
for i in range(len(bins) - 1):
    bin_label = "{0:,}".format(counts[i]) + "  ({0:,.2f}%)".format((counts[i] / counts.sum()) * 100)
    plt.text(bin_x_centers[i], bin_y_centers, bin_label, rotation=90, rotation_mode='anchor')
# Annotation for bar values
ax.annotate('',
            xy=(.85, .30), xycoords='figure fraction',
            horizontalalignment='center', verticalalignment='bottom',
            fontsize=10, bbox=dict(boxstyle="round", fc="white"),
            rotation=-90)
# display
plt.show()
