from interpreter import interpret
import sys

with open(sys.argv[1], 'r') as file:
    program = file.read().splitlines()
    print(interpret(program))
