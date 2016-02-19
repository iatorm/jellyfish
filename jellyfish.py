from interpreter import interpret
from print_parse import prettyprint, matrix_print
import sys

with open(sys.argv[1], 'r') as file:
    program = file.read().splitlines()
    if program[0] == " ":
        interpret(program[1:])
    elif program[0]:
        print(prettyprint(interpret(program)))
    else:
        print(matrix_print(interpret(program[1:])))
