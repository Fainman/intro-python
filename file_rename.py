"""
Rename files from a folder
Get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""
import os


def main():
    """
    Remove numerics from file names
    :return: nothing
    """
    folder_dir = r"C:\Users\johnguerra.AD\Downloads\prank\prankOrig"
    files = os.listdir(folder_dir)
    saved_path = os.getcwd()  # Save current working directory
    os.chdir(folder_dir)
    for file in files:
        # Remove digits from name
        new_file = file.lstrip('0123456789')
        print("old name", file, "new name", new_file)
        # Rename file to new name
        os.rename(file, new_file)
    os.chdir(saved_path)


if __name__ == "__main__":
    main()
    exit(0)