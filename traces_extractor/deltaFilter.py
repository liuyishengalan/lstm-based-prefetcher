# filter out 0 in delta.txt
# if the previous and next is 0, then the current line will be removed

# read delta.txt
# delta.txt: 
# 0x7f7f374b9075 -132997598
# 0x7f7f374b9075 0
# 0x7f7f374b907c 0
# 0x7f7f374b9091 -1

with open('delta.txt', 'r') as f:
    lines = f.readlines()

filtered_lines = []
for i in range(len(lines)):
    # Check if the current line has a delta value of 0
    if lines[i].split()[1] == '0':
        # Check if the previous and next lines also have a delta value of 0
        if i > 0 and i < len(lines) - 1 and lines[i-1].split()[1] == '0' and lines[i+1].split()[1] == '0':
            continue  # Skip this line if it has a delta value of 0 and is surrounded by other lines with a delta value of 0
    filtered_lines.append(lines[i])

with open('filtered_delta.txt', 'w') as f:
    f.writelines(filtered_lines)

############## Filter out the deltas that appear less than 10 times ##############
from collections import Counter

# Read the file
with open('filtered_delta.txt', 'r') as f:
    lines = f.readlines()

# Extract deltas
deltas = [int(line.split()[1]) for line in lines]

# Count the frequency of each delta
counter = Counter(deltas)

# Filter out infrequent deltas
filtered_deltas = {delta: count for delta, count in counter.items() if count >= 10}

# Create a new file that only contains the lines with deltas that appear at least 10 times
with open('filtered_delta.txt', 'w') as f:
    for line in lines:
        delta = int(line.split()[1])
        if delta in filtered_deltas:
            f.write(line)
