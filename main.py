from codecs import open
from pprint import pprint

from math import factorial, sin, cos, pi, e, radians

import tatsu


class CalcBasicSemantics(object):
    def math_pi(self, ast):
        return pi

    def math_e(self, ast):
        return e

    def number_float(self, ast):
        return float(ast)

    def number_int(self, ast):
        return int(ast)

    def term(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "*":
            return ast.left * ast.right
        elif ast.op == "/":
            return ast.left / ast.right
        elif ast.op == "**":
            return ast.left ** ast.right
        else:
            raise Exception("я такого оператора не знаю", ast.op)

    def root(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "root(":
            return ast.right ** (1 / ast.left)
        else:
            raise Exception("я такого оператора не знаю", ast.op)

    def math_factorial(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "!":
            return factorial(ast.middle)
        else:
            raise Exception("я такого оператора не знаю", ast.op)

    def math_sin(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "sin(":
            return sin(radians(ast.middle))
        else:
            raise Exception("я такого оператора не знаю", ast.op)

    def math_cos(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "cos(":
            return cos(radians(ast.middle))
        else:
            raise Exception("я такого оператора не знаю", ast.op)

    def expression(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "+":
            return ast.left + ast.right
        elif ast.op == "-":
            return ast.left - ast.right
        else:
            raise Exception("Unknown operator", ast.op)


def parse_with_basic_semantics():
    grammar = open("calc.ebnf").read()

    parser = tatsu.compile(grammar)
    ast = parser.parse(input("ваше выражение: "), semantics=CalcBasicSemantics())

    pprint(ast, width=20, indent=4)


if __name__ == "__main__":
    parse_with_basic_semantics()
