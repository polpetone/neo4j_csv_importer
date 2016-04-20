from os import walk


def read_file_names_from_directory_filtered_by_suffix(directory_path, suffix):

    unfiltered_files = []
    for (dir_path, dir_names, file_names) in walk(directory_path):
        unfiltered_files.extend(file_names)
        break

    files = filter_files_by_suffix(suffix, unfiltered_files)

    return files


def filter_files_by_suffix(suffix, unfiltered_files):
    files = []
    for file in unfiltered_files:
        if has_file_suffix(file, suffix):
            files.append(file)
    return files


def has_file_suffix(file, suffix):
    return file.endswith(suffix)
