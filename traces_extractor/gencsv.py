# read delta.txt, convert to traces.csv
# with the head pc,delta_in,delta_out
# and the last column is the next delta
# input format:
# pc delta1
# pc delta2
# ...

# output format:
# pc,delta_in,delta_out
# pc, delta1, delta2
# pc, delta2, delta3
# ...
import csv
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 gencsv.py <input file> <output file>")
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as f:
        lines = f.readlines()
        pc_delta_list = []
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
        with open(output_file, 'w') as f_x:
            writer = csv.writer(f_x)
            writer.writerow(['pc', 'delta_in', 'delta_out'])
            for item in pc_delta_list[:-2]: # remove the last line because it doesn't have next delta
                writer.writerow([item[0], item[1], item[2]])

if __name__ == "__main__":
    main()