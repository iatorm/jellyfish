from interpreter import interpret, prettyprint
import sys

with open(sys.argv[1], 'r') as file:
    program = file.read().splitlines()
    print(prettyprint(interpret(program)))
