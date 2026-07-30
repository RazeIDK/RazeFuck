import ast
import os
import variables


def main():
	path_to_file = input("Path to file: ")
	path_to_file = "src/tests/vars.py"

	with open(path_to_file, "r") as file:
		lines = "".join(file.readlines())

	tree = ast.parse(lines)

	visitor = variables.ModuleVisitor()
	visitor.visit(tree)

	print(ast.dump(tree, indent=2))


if __name__ == "__main__":
	main()