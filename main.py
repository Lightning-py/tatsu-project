from codecs import open
from pprint import pprint

import tatsu

from symbols import greek_letters


class AlTeXSemantics(object):
    def temporary_string(self, ast):
        return ast

    def symbol(self, ast):

        print(ast)

        if ast in greek_letters:
            return ast
        else:
            return ast

    def term(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "*":
            return f"{ast.left} {ast.right}"
        elif ast.op == "/":
            return f"frac{{{ast.left}}}{{{ast.right}}}"
        elif ast.op == "**":
            return f"{ast.left} ^ {ast.right}"
        elif ast.op == "=":
            return f"nice bro, variable with name: {ast.variable_name} and value: {ast.variable_value} and type: {type(ast.variable_value)}"
        else:
            raise Exception("Operator does not exist", ast.op)

    def expression(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "+":
            return f"({ast.left} + {ast.right})"
        elif ast.op == "-":
            return f"({ast.left} - {ast.right})"
        else:
            raise Exception("Operator does not exist", ast.op)


def parse_with_basic_semantics(filename: str):
    with open(filename, "r") as file:
        with open("altex.ebnf") as gram:
            grammar = gram.read()

            parser = tatsu.compile(grammar)

            for line in file.readlines():
                ast = parser.parse(line, semantics=AlTeXSemantics())
                pprint(ast)  # , width=20, indent=4)
                print()


if __name__ == "__main__":
    with open("test_file.atex") as src:
        print("Source:", f"{src.read()}\n", sep="\n")
    parse_with_basic_semantics("test_file.atex")
