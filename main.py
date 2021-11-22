from codecs import open
from pprint import pprint

from math import factorial, sin, cos, pi, e, radians


import tatsu

''' 
я придумал небольшой костыль, теперь вместо того чтобы создавать python переменные мы будем просто создавать словарь,
в котором будем хранить все переменные вместе с именами
'''

variables_dict = {}

class CalcBasicSemantics(object):

    def temporary_string(self, ast):
        return ast


    def element(self, ast):
        if ast == 'alpha':
            return '⍺'
        elif ast == 'betta':
            return 'β'
        elif ast[0] == '/':
            return ast[1 : ]

    def term(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "*":
            return f'{ast.left} * {ast.right}'
        elif ast.op == "/":
            return f'{ast.left} / {ast.right}'
        elif ast.op == "**":
            return f'{ast.left} ** {ast.right}'
        elif ast.op == '=':
            variables_dict[ast.variable_name] = ast.variable_value
            return f'nice bro, variable with name: {ast.variable_name} and value: {ast.variable_value} and type: {type(ast.variable_value)}'
        else:
            raise Exception("я такого оператора не знаю", ast.op)


    def expression(self, ast):
        if not isinstance(ast, tatsu.ast.AST):
            return ast
        elif ast.op == "+":
            return f'({ast.left} + {ast.right})'
        elif ast.op == "-":
            return f'({ast.left} - {ast.right})'

        else:
            raise Exception("Unknown operator", ast.op)


def parse_with_basic_semantics(input_file: str):
    with open(input_file) as file:
        grammar = open("calc.ebnf").read()

        parser = tatsu.compile(grammar)

        #### вот тут выполнение кода из файла, оно по умолчанию идет
        for line in file.readlines():
            ast = parser.parse(line.replace('\n', ''), semantics=CalcBasicSemantics())
            pprint(ast, width=20, indent=4)
            print()
        ####
        
        #### вот тут если надо выполнение кода из консольки, ну мало ли там, отлаживать что-то надо будет
            # ast = parser.parse(input("ваше выражение: "), semantics=CalcBasicSemantics())
            # pprint(ast, width=20, indent=4)
        ####

        


if __name__ == "__main__":
    parse_with_basic_semantics(input('input filename: '))
    print(f'variables dictionary:\n{variables_dict}')
