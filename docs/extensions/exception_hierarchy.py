from docutils import nodes
from docutils.parsers.rst import Directive


class ExceptionHierarchy(nodes.General, nodes.Element):
    pass


def visit_exception_hierarchy_node(self, node):
    self.body.append(self.starttag(node, "div", CLASS="exception-hierarchy-content"))


def depart_exception_hierarchy_node(self, node):
    self.body.append("</div>\n")


class ExceptionHierarchyDirective(Directive):
    has_content = True

    def run(self):
        self.assert_has_content()
        node = ExceptionHierarchy("\n".join(self.content))
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app):
    app.add_node(
        ExceptionHierarchy,
        html=(visit_exception_hierarchy_node, depart_exception_hierarchy_node),
    )
    app.add_directive("exception_hierarchy", ExceptionHierarchyDirective)
