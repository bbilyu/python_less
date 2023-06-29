import os
import json
import csv
import pickle


def _directory_info(path):

    files = []
    directories = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            size = sum(
                [os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(full_path)
                 for filename in filenames])
            directories.append({'name': item, 'parent': path, 'size': size})
            files += _directory_info(full_path)[0]
            directories += _directory_info(full_path)[1]
        elif os.path.isfile(full_path):
            files.append({'name': item, 'parent': path, 'size': os.path.getsize(full_path)})

    return files, directories


def directory_info_var_one(dir_path, save_path):

    files, directories = _directory_info(dir_path)

    json_file = os.path.join(save_path, 'directory_info.json')
    with open(json_file, 'w') as f:
        json.dump({'files': files, 'directories': directories}, f)

    csv_file = os.path.join(save_path, 'directory_info.csv')
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'parent', 'size', 'type'])
        for item in files + directories:
            writer.writerow(
                [item['name'], item['parent'], item['size'], 'file' if "." in item['name'] else 'directory'])

    pickle_file = os.path.join(save_path, 'directory_info.pickle')
    with open(pickle_file, 'wb') as f:
        pickle.dump({'files': files, 'directories': directories}, f)


def directory_info_var_two(path):

    files = []
    directories = []


    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            size = sum(
                [os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(full_path)
                 for filename in filenames])
            directories.append({'name': item, 'parent': path, 'size': size})
            directory_info_var_two(full_path)
        elif os.path.isfile(full_path):
            files.append({'name': item, 'parent': path, 'size': os.path.getsize(full_path)})


    json_file = os.path.join(path, 'directory_info.json')
    with open(json_file, 'w') as f:
        json.dump({'files': files, 'directories': directories}, f)

    csv_file = os.path.join(path, 'directory_info.csv')
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'parent', 'size', 'type'])
        for item in files + directories:
            print(item)
            writer.writerow(
                [item['name'], item['parent'], item['size'], 'file' if "." in item['name'] else 'directory'])

    pickle_file = os.path.join(path, 'directory_info.pickle')
    with open(pickle_file, 'wb') as f:
        pickle.dump({'files': files, 'directories': directories}, f)

    return files, directories


if __name__ == '__main__':
    dir_pth = 'K:\python_lessons\home_work\hw_eight\dirs'
    save_pth = 'K:\python_lessons\home_work\hw_eight'
    directory_info_var_one(dir_pth, save_pth)
    # directory_info_var_two(dir_pth)
