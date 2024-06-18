import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("test", "Value", "Child", {"key": "value"})
        node2 = HTMLNode("test", "Value", "Child", {"key": "value"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        check_props = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(check_props, node.props_to_html())

    def test_notEqual(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("tag", None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("TAG", "VALUE", "CHILDREN", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            "HTMLNode(Tag: TAG Value: VALUE Children: CHILDREN Props: {'href': 'https://www.google.com', 'target': '_blank'})",
            repr(node)
        )


if __name__ == '__main__':
    unittest.main()
