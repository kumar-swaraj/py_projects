import os
import shutil


def create_folder(path: str, extension: str, /) -> str:
    """Creates a folder that is named after the extension of the file passed in."""
    folder_name = extension.lstrip(".")
    folder_path = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def sort_files(source_path: str, /) -> None:
    """Sorts files based on a given path."""
    for root_dir, _, filenames in os.walk(source_path):
        for filename in filenames:
            file_path = os.path.join(root_dir, filename)
            extension = os.path.splitext(filename)[1]
            if extension:
                target_folder = create_folder(source_path, extension)
                target_path = os.path.join(target_folder, filename)
                shutil.move(file_path, target_path)


def remove_empty_folders(source_path: str, /) -> None:
    """Remove all empty folder from given path."""
    for root_dir, sub_dir, _ in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path = os.path.join(root_dir, current_dir)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main() -> None:
    user_input = input("Please provide a file path to sort: ")

    if os.path.exists(path=user_input):
        sort_files(user_input)
        remove_empty_folders(user_input)
        print("Files sorted successfully.")
    else:
        print("Invalid path, please provide a valid file path.")


if __name__ == "__main__":
    main()
