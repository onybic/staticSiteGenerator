import unittest
from block_markdown import (
    markdown_to_blocks, block_to_block_type, markdown_to_html_node,
    block_type_paragraph,
    block_type_unordered_list,
    block_type_quote,
    block_type_code,
    block_type_ordered_list,
    block_type_heading
)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_type_paragraph(self):
        block = "####### 12 test block ```"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_type_heading(self):
        block = ("### heading check\n## another")
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_type_code(self):
        block = "```\n code block\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)

    def test_block_type_quote(self):
        block = ">sample\n>quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)

    def test_block_type_ulist(self):
        block = "- first\n* second"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_type_olist(self):
        block = "1. first element\n2. second element\n3. third"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_markdown_to_html(self):
        md = """
### this is heading 3\n
```
piece of code here
```\n
rando paragraph
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, """<div><h3>this is heading 3</h3><pre><code>piece of code here
</code></pre><p>rando paragraph</p></div>""", )


if __name__ == "__main__":
    unittest.main()
