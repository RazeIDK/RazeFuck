import ast
import os
import variables


def main():
	path_to_file = input("Path to file: ")
	tree = ast.parse(path_to_file)


if __name__ == "__main__":
	main()