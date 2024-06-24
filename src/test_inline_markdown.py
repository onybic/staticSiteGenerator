import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_image,
    text_type_link)


class TestInlineMarkdown(unittest.TestCase):

    def test_delim_bold(self):
        node = TextNode("This text is **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This text is ", text_type_text, None),
                TextNode("bolded", text_type_bold, None),
                TextNode(" word", text_type_text, None),
            ],
            new_nodes
        )

    def test_delim_bold_multiple(self):
        node = TextNode("This **text** really **has** 3 **bolded** words", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This ", text_type_text, None),
                TextNode("text", text_type_bold, None),
                TextNode(" really ", text_type_text, None),
                TextNode("has", text_type_bold, None),
                TextNode(" 3 ", text_type_text, None),
                TextNode("bolded", text_type_bold, None),
                TextNode(" words", text_type_text, None),
            ],
            new_nodes
        )

    def test_delim_italic(self):
        node = TextNode("This text is *italics* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This text is ", text_type_text, None),
                TextNode("italics", text_type_italic, None),
                TextNode(" word", text_type_text, None)
            ],
            new_nodes
        )

    def test_delim_italic_bold_code(self):
        node = TextNode("This text is *italics* and also **bold** with `code included`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)

        self.assertListEqual(
            [
                TextNode("This text is ", text_type_text, None),
                TextNode("italics", text_type_italic, None),
                TextNode(" and also ", text_type_text, None),
                TextNode("bold", text_type_bold, None),
                TextNode(" with ", text_type_text, None),
                TextNode("code included", text_type_code, None)
            ],
            new_nodes
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This text has an ![image](https://image.url/image.png)")
        self.assertListEqual([("image", "https://image.url/image.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)")
        self.assertListEqual(
            [("link", "https://www.example.com"), ("another", "https://www.example.com/another")],
            matches
        )

    def test_text_to_textnode(self):
        test_nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode("", "text", None)
            ],
            test_nodes
        )

        if __name__ == "__main__":
            unittest.main()
