from interpreter import interpret
import sys

with open(sys.argv[1], 'r') as source_file:
    program = source_file.read().splitlines()
    interpret(program)
