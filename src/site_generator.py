import os.path

from block_markdown import markdown_to_blocks, is_block_heading_block, markdown_to_html_node


def extract_title(markdown):
    for block in markdown_to_blocks(markdown):
        if not is_block_heading_block(block):
            continue
        stripped_block = block.strip()
        h_size = 0
        for char in stripped_block:
            if char == "#":
                h_size += 1
            else:
                break
        if h_size == 1:
            title = stripped_block[h_size:].strip()
            if not title:
                raise ValueError("No text under h1 tag provided in markdown")
            return title
    raise ValueError("No h1 tags available in provided markdown!")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        site_template = f.read()

    site_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    output_content = site_template.replace("{{ Title }}", title).replace("{{ Content }}", site_content)

    destination_dir = os.path.dirname(dest_path)
    if destination_dir != "":
        os.makedirs(destination_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(output_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for element in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, element)
        dst_path = os.path.join(dest_dir_path, element)
        if os.path.isfile(src_path):
            if element.lower().endswith(".md"):
                generate_page(src_path, template_path, dst_path.replace(".md", ".html"))
        else:
            generate_pages_recursive(src_path, template_path, dst_path)
