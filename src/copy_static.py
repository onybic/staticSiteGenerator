import os
import shutil


def copy_static_contents(source_path, destination_path):
    if not os.path.exists(destination_path):
        print("Creating destination directory...")
        os.mkdir(destination_path)

    for element in os.listdir(source_path):
        src_path = os.path.join(source_path, element)
        dst_path = os.path.join(destination_path, element)
        print(f"Copying {src_path} -> {dst_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_static_contents(src_path, dst_path)
