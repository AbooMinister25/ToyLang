import os

def open_file(filename, lines=None):
    with open(filename, "r") as f:
        if lines == None:
            data = f.read()
        elif lines == "lines":
            data = f.readlines()
        else:
            raise Exception(f"Invalid arguent {lines} given")
    return data


def write_file(filename, *data):
    with open(filename, "w") as f:
        f.write(data)


def append_file(filename, *data):
    with open(filename, "a") as f:
        f.write(data)


def check_path(path):
    if os.path.exists(path):
        return True
    else:
        return False


