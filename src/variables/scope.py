import ast

class ScopeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.scope = {}
        self.depth = 0

    def visit_FunctionDef(self, node):
        print(True)
        self.generic_visit(node)

    def visit_Module(self, node):
        print(True)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        print(True)
        self.generic_visit(node)