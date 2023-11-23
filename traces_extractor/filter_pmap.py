def read_memory_ranges_from_file(file_path):
    memory_ranges = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2 and parts[0] != 'total':
                try:
                    start_address_hex = parts[0]
                    size_kbytes = parts[1].replace('K', '')
                    start_address = int(start_address_hex, 16)
                    size_bytes = int(size_kbytes) * 1024
                    end_address = start_address + size_bytes - 1
                    memory_ranges.append((start_address, end_address))
                except ValueError:
                    continue
    return memory_ranges

def filter_page_accesses(page_file, memory_ranges, output_file):
    with open(page_file, 'r') as file, open(output_file, 'w') as outfile:
        for line in file:
            parts = line.split()
            if len(parts) != 3:
                continue
            _, page_addr, _ = parts
            page_addr = int(page_addr, 16)
            if any(start <= page_addr <= end for start, end in memory_ranges):
                continue
            outfile.write(line)
    

# File paths
page_file_path = 'page.txt'
# get memory ranges from pmap_output1 to pmap_output7
memory_ranges = read_memory_ranges_from_file('pmap_output1')
memory_ranges += read_memory_ranges_from_file('pmap_output2')
memory_ranges += read_memory_ranges_from_file('pmap_output3')
memory_ranges += read_memory_ranges_from_file('pmap_output4')
memory_ranges += read_memory_ranges_from_file('pmap_output5')
memory_ranges += read_memory_ranges_from_file('pmap_output6')
memory_ranges += read_memory_ranges_from_file('pmap_output7')
output_file = 'page_filtered.txt'
filter_page_accesses(page_file_path, memory_ranges, output_file)


# print number of lines in page.txt
print('length of page.txt:' + str(sum(1 for line in open('page.txt'))))

# print number of lines in page_filtered.txt
print('length of page_filtered.txt:' + str(sum(1 for line in open('page_filtered.txt'))))