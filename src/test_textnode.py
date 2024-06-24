import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_node_to_html_node
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text, )
        node2 = TextNode("This is a text node", text_type_text, )
        self.assertEqual(node, node2)

    def test_notEqual(self):
        node = TextNode("Test1", text_type_italic, "https://url.test")
        node2 = TextNode("test2", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_notEqual2(self):
        node = TextNode("Test1", "italics", "https://url.test")
        node2 = TextNode("Test1", "bold", "https://url.test")
        self.assertNotEqual(node, node2)

    def test_incorrectData(self):
        self.assertRaises(TypeError, lambda: TextNode())

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(
            'TextNode("This is a text node", "bold", "None")', repr(node)
        )

    def test_t2html(self):
        node = text_node_to_html_node(TextNode("This is bolded text", text_type_bold, None))
        self.assertEqual(node.__repr__(), "LeafNode(Tag: b, Value: This is bolded text, Props: None)")


if __name__ == '__main__':
    unittest.main()
