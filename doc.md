# Documentation

For a list of built-in functions and operators, see [here](https://github.com/iatorm/jellyfish/blob/master/stdlib.md).

## Source syntax

Jellyfish is a two-dimensional language, and the source code should be thought of as a 2D grid.
Each position of the grid may contain an _item_, which is one of the following:

- A _value_, which is further classified as one of the following:
  - A _numeric literal_, visually a horizontal run of digits. It is placed at the position of the leftmost digit.
  - A _character literal_, visually a single quote `'` followed by said character. It is placed at the position of the quote.
  - A _string literal_, visually a horizontal run of characters surrounded by double quotes `"`. A closing quote is inferred at the end of a line. The item is placed at the left quote.
  - An _input value_, denoted by the letter `i` for evaluated input and `I` for raw string input. These are parsed from STDIN in the normal English reading order before the program is executed.
- A _function_, which transforms one or two input values into a single output value.
- An _operator_, which transforms one or two input values or functions into a new function.
- A _control character_, which affects the parsing process.

The following _control characters_ modify the parsing process, mostly the way functions are operators take their arguments.

- `B` blocks all flow of data. Functions and operators cannot take any arguments through it.
- `V` blocks all values. Functions cannot take their arguments through it. Operators cannot take value arguments, but can take function arguments.
- `F` blocks all functions. An operator can still take an input through this character, but instead of a function, its output value will be considered.
- `A` blocks all arguments. An operator will not be evaluated on the arguments of an input obtained through it.
- `E` turns a southward argument-seeking process to the east.
- `S` turns an eastward argument-seeking process to the south.
- `X` is a combination of `E` and `S`.

Whitespace is ignored, and all but the leftmost characters of literals are regarded as whitespace.

Most functions and operators have _unary_ and _binary_ forms.
A function on the grid takes as its inputs the nearest values to its south and east; if both are present, the binary form is used, and if only one is present, the unary form is used.
An operator also takes its inputs from the south and east, but they are functions instead of values.
Only if a value is encountered instead of a function, it is used as the input to an operator.
The operator evaluates its argument(s) and produces a new function, and this function is evaluated on the argument(s) of its east input (or, if the east input has no arguments, its south input).
Every value (a literal or input value) on the grid is counted as having one argument, namely itself.
A program is run by evaluating the top left item, and all other items required for that, in an unspecified order (except that function calls are always evaluated after their arguments).
Unnecessary function calls are not evaluated, even when the function and its arguments are used in an operator call.

## Input and output format

Input and output values have the same format.
A number is a string of digits, possibly prefixed by `-`, and possibly containing the decimal point `.` and/or the exponent marker `e`.
Characters are surrounded in single quotes `'`, and strings in double quotes `"`, from both sides.
Arrays are wrapped in `[]`, and their items are separated by spaces when necessary.
The arrays can be nested in an arbitrary way, and strings are simply arrays of characters.
