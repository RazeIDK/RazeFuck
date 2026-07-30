import ast

scope = {}
depth = 0

class ScopeVisitor(ast.NodeVisitor):
    def update_scope_node(self, update_node):
        global scope, depth
        if not scope.get(depth, False):
            scope[depth] = []

        scope[depth] = update_node

    def visit_FunctionDef(self, node):
        

    def visit_Module(self, node):
        pass

    def visit_ClassDef(self, node):
        pass