import os
import sys
import filecmp

def main():
    #take input
    path = get_path()

    #scan dir
    files = process(path)
    # files -> {"file_name" : "file_path"}

    #compare stored data
    duplicate_files = compare(files)

    #show dup files

    #allow to delete files


def get_path():
    path = input("Path: ")
    if os.path.isdir(path):
        return path
    sys.exit("Invalid Path")

def process(path):
    seen_files = {}

    for (root,dirs,files) in os.walk(path):
        for file in files :
            full_path = os.path.join(path, file)
            file_size = os.path.getsize(full_path)
            if file_size in seen_files:
                seen_files[file_size].append(full_path)
            else:
                seen_files.update({file_size : [full_path]})
            

    return seen_files

def compare(files):

    duplicate_files = []

    for size in files:
        if len(files[size]) > 1:
            for file in files[size]:
                refrence_file = file
                # to be continue


    
            


if __name__ == "__main__":
    main() 