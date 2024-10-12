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
    for path in duplicate_files:
        print(f"{os.path.basename(path)} at {path}")

    #allow to delete files
    choice = input("Press 'y' to delete duplicate files: ")
    if choice.strip().lower() == "y":
        delete(duplicate_files)


def get_path():
    path = input("Path: ")
    if os.path.isdir(path):
        return path
    sys.exit("Invalid Path")

def process(path):
    seen_files = {}

    for (root,dirs,files) in os.walk(path):
        for file in files :
            full_path = os.path.join(root, file)
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
            for i, file in enumerate(files[size]):
                refrence_file = file
                for file in files[size][i+1:]:
                    if filecmp.cmp(refrence_file, file, shallow=False):
                        duplicate_files.append(file)

    return set(duplicate_files)

def delete(files):
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted: {os.path.basename(file)}")
        except Exception as e:
            print(f"Error deleting {os.path.basename(file)}: {e}")

if __name__ == "__main__":
    main() 