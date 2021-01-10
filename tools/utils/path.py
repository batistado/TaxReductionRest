import os


def get_parent_dir(file):
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_parent_dir_from_dir(path):
    return os.path.dirname(path)


def join_paths(dir, *paths):
    return os.path.join(dir, *paths)
