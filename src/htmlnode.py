

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("method to_html not implemented yet")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_text = ""
        for key, value in self.props.items():
            props_text += f' {key}="{value}"'
        return props_text

    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props})"

    def __eq__(self, other):
        return (
                self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props
        )
