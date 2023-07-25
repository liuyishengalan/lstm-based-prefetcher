from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Read the file
with open('filtered_delta.txt', 'r') as f:
    lines = f.readlines()

# Extract deltas
deltas = [int(line.split()[1]) for line in lines]

# Create a mapping from each unique delta to a unique integer index
delta_to_index = {delta: i for i, delta in enumerate(set(deltas))}

# Convert deltas to indices
indices = [delta_to_index[delta] for delta in deltas]

# Convert indices to one-hot encoding
encoder = OneHotEncoder(sparse_output=False)
one_hot = encoder.fit_transform(np.array(indices).reshape(-1, 1))

# Replace the original delta with its one-hot encoded representation
new_lines = []
for line, one_hot_vector in zip(lines, one_hot):
    pc, _ = line.split()
    new_line = pc + ' ' + ' '.join(map(str, one_hot_vector.astype(int))) + '\n'
    new_lines.append(new_line)

# Write the new lines to a new file
with open('filtered_delta_one_hot.txt', 'w') as f:
    f.writelines(new_lines)
