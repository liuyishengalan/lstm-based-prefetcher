pc_delta_list = []
with open('filtered_delta_one_hot.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        # Split each line into PC and delta, assuming they're separated by a space
        pc, *delta = line.strip().split()
        # Convert delta into string
        pc = int(pc, 16)
        delta= ''.join(str(i) for i in delta)

        # Add the PC and delta and next delta to the list
        pc_delta_list.append([pc, delta])

# add next delta to the list
for i in range(len(pc_delta_list) - 1):
    pc_delta_list[i].append(pc_delta_list[i + 1][1])

# Save the data in a new file but not saving the last element
# in format: [[pc1, delta1, delta2], [pc2, delta2, delta3], ...]
with open('input.txt', 'w') as f_x:
    f_x.write('[')
    for item in pc_delta_list[:-2]: # remove the last line because it doesn't have next delta
        f_x.write(str(item) + ', ')
    f_x.write(str(pc_delta_list[-2]) + ']')