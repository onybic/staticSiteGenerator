import unittest

from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_eq2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "1"),
                LeafNode(None, "2"),
                LeafNode("i", "3"),
                LeafNode(None, "4"),
                ParentNode(
                    "a",
                    [
                        LeafNode("b", "55"),
                        LeafNode(None, "66"),
                        LeafNode("i", "77"),
                        LeafNode(None, "88"),
                    ],
                )
            ],
        )
        self.assertEqual("<p><b>1</b>2<i>3</i>4<a><b>55</b>66<i>77</i>88</a></p>", node.to_html())

    def test_eq3(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "1"),
                ParentNode(
                    "a",
                    [
                        LeafNode("b", "55"),
                        ParentNode(
                            "p",
                            [
                                LeafNode("b", "1"),
                                ParentNode(
                                    "a",
                                    [
                                        LeafNode("b", "55"),
                                    ],
                                )
                            ],
                        )
                    ],
                )
            ],
        )
        self.assertEqual("<p><b>1</b><a><b>55</b><p><b>1</b><a><b>55</b></a></p></a></p>", node.to_html())


if __name__ == '__main__':
    unittest.main()
