import os 

def main():

    path = input("Path: ")
    duplicate_files = process(path)
    display(duplicate_files)

    
def process(path):

    seen_file = {}
    duplicates = []

    for (root,dirs,files) in os.walk(path):
        for file_name in files :
            full_path = os.path.join(root, file_name)
            if file_name in seen_file :
                try:
                    duplicates.append(full_path)
                    # os.remove(full_path)
                except Exception as e:
                    print(f"Error: {e}") 
            else :
                seen_file[file_name] = full_path


    return duplicates


def display(list):
    print("Duplicate files are:")

    for i, file in enumerate(list):
        print(i, file)


if __name__ == "__main__":
    main()