import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("test", "Value", {"key": "value"})
        node2 = LeafNode("test", "Value", {"key": "value"})
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            "<p>This is a paragraph of text.</p>",
            node.to_html()
        )

    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>',
            node.to_html()
        )

    def test_to_html3(self):
        node = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            'Click me!',
            node.to_html()
        )

    def test_to_html4(self):
        node = LeafNode(None, "", {"href": "https://www.google.com"})
        self.assertRaises(ValueError, lambda: node.to_html())

    def test_repr(self):
        node = LeafNode("a", "test click", {"href": "https://www.google.com"})
        self.assertEqual("LeafNode(Tag: a, Value: test click, Props: {'href': 'https://www.google.com'})",
                         node.__repr__())


if __name__ == '__main__':
    unittest.main()
