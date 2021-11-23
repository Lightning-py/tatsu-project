from codecs import open
from pprint import pprint
from typing import Optional

import tatsu

from symbols import greek_letters


class AlTeXSemantics(object):
    def symbol(self, ast):

        if ast in greek_letters:
            return "\\" + ast
        else:
            return ast

    def term(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "*":
            return f"{ast.left} {ast.right}"
        elif ast.op == "/":
            return f"\\frac{{{ast.left}}}{{{ast.right}}}"
        elif ast.op == "**":
            return f"{ast.left} ^ {ast.right}"
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


def parse_with_basic_semantics(filename: str, output: Optional[str] = None):
    with open(filename, "r") as file:
        with open("altex.ebnf") as gram:
            grammar = gram.read()

            parser = tatsu.compile(grammar, name="AlTeX", semantics=AlTeXSemantics)

            for line in file.readlines():
                result = parser.parse(line, semantics=AlTeXSemantics())
                print(result)


if __name__ == "__main__":
    with open("test_file.atex") as src:
        print("Source:", f"{src.read()}\n", sep="\n")
    parse_with_basic_semantics("test_file.atex")
