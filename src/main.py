import os
import sys
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static: str = "./static"
dir_path_public: str = "./docs"
dir_path_content: str = "./content"
template_path: str = "./template.html"
default_basepath: str = "/"


def main():

    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()
