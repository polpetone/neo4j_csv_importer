from os import walk


def read_files_from_directory(directory_path):
    f = []
    for (dir_path, dir_names, file_names) in walk(directory_path):
        f.extend(file_names)
        break
    return f