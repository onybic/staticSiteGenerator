import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_image,
    text_type_link)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not text_type_text:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid Markdown syntax! Missing delimeter")
        split_nodes = []
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_text[i], text_type_text))
            else:
                split_nodes.append(TextNode(split_text[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        while True:
            node_images = extract_markdown_images(node.text)
            if len(node_images) == 0:
                new_nodes.append(node)
                break
            img_alt, img_url = node_images[0]
            parts = node.text.split(f"![{img_alt}]({img_url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(img_alt, text_type_image, img_url))
            node.text = parts[1]
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        while True:
            node_links = extract_markdown_links(node.text)
            if len(node_links) == 0:
                new_nodes.append(node)
                break
            url_dec, url = node_links[0]
            parts = node.text.split(f"[{url_dec}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(url_dec, text_type_link, url))
            node.text = parts[1]
    return new_nodes


def text_to_textnodes(text):
    new_nodes = [TextNode(text, text_type_text)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes
