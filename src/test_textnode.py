import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_notEqual(self):
        node = TextNode("Test1", "italics", "https://url.test")
        node2 = TextNode("test2", "italics")
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
            "TextNode(This is a text node, bold, None)", repr(node)
        )


if __name__ == '__main__':
    unittest.main()
