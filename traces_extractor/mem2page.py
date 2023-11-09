# Step2: Convert memory addresses to page addresses
page_size = 4 * 1024 # 4KB

def convert_address_to_page(memory_address):
    page_number = memory_address & ~((1 << 12) - 1)
    
    offset = memory_address % page_size
    return page_number, offset

# read input file
with open("pinatrace.out", "r") as file:
    lines = file.readlines()

# clean the file page.txt
open('page.txt', 'w').close()

# file structure in pinatrace.out:
# 0x7f205266c2b3: W 0x7ffd3b00e188
# 0x7f205266d054: W 0x7ffd3b00e180
# 0x7f205266d058: R 0x7ffd3b00e178

# PC: operation MEM addr
count = 0
# Retrieve MEM addr and convert to page address
for line in lines:
    elements = line.split()
    if len(elements) == 3:
        if len(elements[0]) != 15 or len(elements[2]) != 14:
            count += 1
            continue
        program_counter = int(elements[0].replace(':', ''), 16)
        memory_address = int(elements[2], 16)
        page_number, offset = convert_address_to_page(memory_address)
        # print([hex(memory_address), hex(page_number), hex(offset)])

        with open("page.txt", "a") as file:
            file.write(hex(program_counter) + " " + hex(int(page_number)) + " " + hex(offset) + "\n")

print("Total number of lines ignored: ", count)
