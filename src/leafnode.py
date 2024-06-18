from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == "" or self.value is None:
            raise ValueError("Node has no value! All leafs require a value")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(Tag: {self.tag}, Value: {self.value}, Props: {self.props})"

    def __eq__(self, other):
        return (
                self.tag == other.tag
                and self.value == other.value
                and self.props == other.props
        )