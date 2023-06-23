import os


def rename_files(num_digits, source_ext, dest_ext, name_range=None, final_name=None):
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(source_ext)]
    files.sort()
    if name_range:
        start, end = name_range
    else:
        start, end = 0, None
    count = 1
    for file in files:
        name = file[:end][start:]
        if final_name:
            new_name = name + final_name + str(count).zfill(num_digits) + '.' + dest_ext
        else:
            new_name = name + str(count).zfill(num_digits) + '.' + dest_ext
        os.rename(file, new_name)
        count += 1


if __name__ == '__main__':
    rename_files(3, "txt", "doc", [0, 3])
