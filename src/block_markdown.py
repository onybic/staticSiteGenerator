from parentnode import ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'code'
block_type_quote = 'quote'
block_type_unordered_list = 'unordered_list'
block_type_ordered_list = 'ordered_list'


def markdown_to_blocks(markdown):
    new_blocks = []
    for line in markdown.split("\n\n"):
        if line == "":
            continue
        block = line.strip()
        new_blocks.append(block)
    return new_blocks


def is_block_heading_block(block):
    return (block.startswith("# ")
            or block.startswith("## ")
            or block.startswith("### ")
            or block.startswith("#### ")
            or block.startswith("##### ")
            or block.startswith("###### "))


def is_block_code_block(lines):
    return len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```")


def is_unordered_list_block(lines):
    return all(line.startswith("* ") or line.startswith("- ") for line in lines)


def is_ordered_list_block(lines):
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            return False
    return True


def block_to_block_type(block):
    lines = block.split("\n")
    if is_block_heading_block(block):
        return block_type_heading
    if is_block_code_block(lines):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
            return block_type_quote
    if is_unordered_list_block(lines):
        return block_type_unordered_list
    if block.startswith("1. ") and is_ordered_list_block(lines):
        return block_type_ordered_list
    return block_type_paragraph


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


def heading_block_to_html(block):
    h_size = 0
    for char in block:
        if char == "#":
            h_size += 1
        else:
            break
    text = block[h_size + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{h_size}", children)


def paragraph_block_to_html(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def code_block_to_html(block):
    code_value = block[4:-3]
    children = text_to_children(code_value)
    code_html = ParentNode("code", children)
    return ParentNode("pre", [code_html])


def quote_block_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)


def unordered_list_block_to_html(block):
    lines = block.split("\n")
    html_line = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_line.append(ParentNode("li", children))
    return ParentNode("ul", html_line)


def ordered_list_block_to_html(block):
    lines = block.split("\n")
    html_line = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_line.append(ParentNode("li", children))
    return ParentNode("ol", html_line)


def block_to_html(block):
    type_of_block = block_to_block_type(block)
    if type_of_block == block_type_paragraph:
        return paragraph_block_to_html(block)
    if type_of_block == block_type_heading:
        return heading_block_to_html(block)
    if type_of_block == block_type_code:
        return code_block_to_html(block)
    if type_of_block == block_type_quote:
        return quote_block_to_html(block)
    if type_of_block == block_type_ordered_list:
        return ordered_list_block_to_html(block)
    if type_of_block == block_type_unordered_list:
        return unordered_list_block_to_html(block)
    raise ValueError("Invalid block type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html(block)
        children.append(html_node)
    return ParentNode("div", children)
