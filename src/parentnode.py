from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Node has no tag provided")
        if self.children is None:
            raise ValueError("No children provided")
        node_children_html = ""
        for node in self.children:
            node_children_html += node.to_html()
        return f"<{self.tag}>{node_children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(Tag: {self.tag}, Children: {self.children}, Props: {self.props})"