# Jellyfish

Jellyfish is a two-dimensional esoteric programming language inspired by J and written in Python 3.
It was inspired by a [challenge](http://codegolf.stackexchange.com/questions/65661/parse-a-two-dimensional-syntax) on PPCG.
The name was suggested in PPCG chat as a combination of [Jelly](https://github.com/DennisMitchell/jelly), a golfing language inspired by J, and [Fish](https://esolangs.org/wiki/Fish), a two-dimensional esoteric language.
There's a [syntax documentation file](https://github.com/iatorm/jellyfish/blob/master/doc.md), a [reference file](https://github.com/iatorm/jellyfish/blob/master/stdlib.md), and an [online interpreter](http://jellyfish.tryitonline.net/), courtesy of [Dennis from PPCG](http://codegolf.stackexchange.com/users/12012/dennis).

Development of Jellyfish is slow but ongoing, so things may freeze for a long time and then break without notice.
At the moment, there's a command-line interpreter and a rudimentary documentation file.
The interpreter can be invoked by the command

    python jellyfish.py <source_file>

Input is taken from STDIN, and output goes to STDOUT.
The standard file extension for Jellyfish source files is `jf`, but this is not enforced by the interpreter.