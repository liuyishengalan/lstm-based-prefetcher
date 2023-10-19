prev_page_addr = None

with open("page.txt", "r") as f_in, open("delta.txt", "w") as f_out:
    for line in f_in:
        elements = line.split()
        pc = int(elements[0], 16)
        page_addr = int(elements[1], 16)
        if prev_page_addr is not None:
            delta = (page_addr - prev_page_addr)//4096
            f_out.write(f"{hex(pc)} {delta}\n")
        else:
            f_out.write(f"{hex(pc)} {0}\n")

        prev_page_addr = page_addr