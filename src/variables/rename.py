import ast
import random


def generate_word():
	ru_symbol = "О"
	en_symbol = "O"
	symbols = ru_symbol + en_symbol
	
	gen = []
	for i in range(14):
		gen.append(random.choice(symbols))

	return en_symbol * 10 + "".join(gen)

for i in range(10):
	print(generate_word())

class RenameTransformer(ast.NodeTransformer):
	def visit_Name(self, node):
		if isinstance(node.ctx, ast.Store):
			print("create")
		return node