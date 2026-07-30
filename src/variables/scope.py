import ast


class ScopeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.scope = {}
        self.depth = 0

    def update_scope_node(self, update_node):
        if not self.scope.get(self.depth, False):
            self.scope[self.depth] = []

        cleaned_node = update_node.copy()

        for i in update_node.body:
            if isinstance(i, (
                ast.FunctionDef,
                ast.Module,
                ast.ClassDef
                )):
                cleaned_node.remove(i)
        self.scope[self.depth].append(update_node)

    def get_scope(self):
        return self.scope


    def visit_FunctionDef(self, node):
        self.update_scope_node(node)
        self.depth += 1
        
        for child in node.body:
            self.visit(child)

        self.depth -= 1

    def visit_Module(self, node):
        self.update_scope_node(node)
        self.depth += 1
        
        for child in node.body:
            self.visit(child)

        self.depth -= 1

    def visit_ClassDef(self, node):
        self.update_scope_node(node)
        self.depth += 1

        for child in node.body:
            self.visit(child)

        self.depth -= 1