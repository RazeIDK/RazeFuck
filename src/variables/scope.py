import ast

class ModuleVisitor(ast.NodeTransformer):
    def __init__(self):
        self.current_module = None

    def visit_Module(self, node):
        visitor = VariableVisitor()
        tree = visitor.visit(node)
        return tree

class VariableVisitor(ast.NodeTransformer):
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            print("STORE")
        elif isinstance(node.ctx, ast.Store):
            pass

        return self.generic_visit(node)