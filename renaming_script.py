import os
import argparse

SOURCE_DIRECTORY = "."


def get_new_name(old_name: str):
    splitted_file_name = old_name.split('.')[0].split('_')
    if splitted_file_name[0] != 'fin':
        return None
    if splitted_file_name[3] != 'Channel':
        return None
    try:
        int(splitted_file_name[1])
        int(splitted_file_name[2])
        int(splitted_file_name[4])
    except ValueError:
        return None
    try:
        return f"S{splitted_file_name[4]}С1_Strip_{splitted_file_name[2][-4:]}.{old_name.split('.')[1]}"
    except IndexError:
        return None


def main():
    parser = argparse.ArgumentParser(prog='renaming_script.py', description='Rename las files.')
    parser.add_argument('path', metavar='Path', type=str, nargs=1, help='Folder for renaming')
    args = parser.parse_args()
    working_dir = f"{args.path[0]}\\"
    print(f"ARGS: {args}")
    list_of_files = os.listdir(working_dir)
    print(f"{list_of_files}")
    for file_name in list_of_files:
        print(f"{working_dir + file_name} - {os.path.isfile(os.path.normpath(working_dir + file_name))}")
        if os.path.isfile(os.path.normpath(working_dir + file_name)):
            if get_new_name(file_name):
                print(f"{get_new_name(file_name)}")
                try:
                    os.rename(f"{working_dir + file_name}", f"{working_dir + get_new_name(file_name)}")
                except FileExistsError:
                    print(f"Unable to rename file <{working_dir + file_name}> "
                          f"(destination file {get_new_name(file_name)} already exists).")


if __name__ == '__main__':
    main()
