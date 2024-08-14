import os
import shutil

def clear_directory(directory_path):
    """Remove all files and subdirectories within a directory, but keep the directory itself."""
    if os.path.isdir(directory_path):
        try:
            # Iterate over all files and subdirectories in the directory
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                # If it's a file, remove it
                if os.path.isfile(item_path):
                    os.remove(item_path)
                # If it's a directory, remove it and all its contents
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            print(f"Contents of directory '{directory_path}' have been removed.")
        except PermissionError as e:
            print(f"Permission error: {e}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Directory '{directory_path}' does not exist.")

