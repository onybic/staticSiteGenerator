import os
import shutil

from copy_static import copy_static_contents
from site_generator import generate_pages_recursive

static_dir_path = "./static"
public_dir_path = "./public"


def main():
    if os.path.exists(public_dir_path):
        print("Cleaning up destination directory...")
        shutil.rmtree(public_dir_path)

    print("Copying static files to public directory...")
    copy_static_contents(static_dir_path, public_dir_path)

    generate_pages_recursive("content/", "template.html", "public/")


main()
