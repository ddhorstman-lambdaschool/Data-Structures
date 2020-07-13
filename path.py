import os


def dotdot(path):
    return os.path.dirname(path)


def get_path():
    return dotdot(os.path.realpath(__file__))
