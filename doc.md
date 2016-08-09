# Documentation

**Please note**: this document is incomplete and possibly not up to date.

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

## Vocabulary

### Control characters

The following characters control the parsing process, mostly the way functions are operators take their arguments.

- `B` blocks all flow of data. Functions and operators cannot take any arguments through it.
- `V` blocks all values. Functions cannot take their arguments through it. Operators cannot take value arguments, but can take function arguments.
- `F` blocks all functions. An operator can still take an input through this character, but instead of a function, its output value will be considered.
- `A` blocks all arguments. An operator will not be evaluated on the arguments of an input obtained through it.
- `E` turns a southward argument-seeking process to the east.
- `S` turns an eastward argument-seeking process to the south.
- `X` is a combination of `E` and `S`.

### Functions

Jellyfish handles characters as numbers with a special flag.
All arithmetic operations work on characters too, and the output value gets its flag from the left (south) argument.
Some functions (notably the arithmetic ones) implement _threading_, which works as follows.
The _height_ of an array is the height of the tallest tower of nested arrays in it, and _atoms_ (numbers and characters) have height 0.
If a function is _threaded to level `n`_, and it's given an array of height more than `n`, it recurses on the items of that array.
A negative `n` means that the function recurses to the items exactly `-n-1` times.
This is generalized to binary functions too, but it's more complicated.

- `{` returns its left argument.
- `}` returns its right argument.
- Unary `j` and `J` ignore their arguments and read lines from STDIN. `j` parses the line, `J` returns it as a string.
- Unary `p` and `P` return their arguments and print them to STDOUT. `p` uses the input format, `P` the matrix format.
- Unary `+` is absolute value, binary is addition (threaded to level 0).
- Unary `-` is negation, binary is subtraction (threaded to level 0).
- Unary `*` is signum, binary is multiplication (threaded to level 0).
- Unary `%` is reciprocal, binary is division (threaded to level 0).
- Unary `|` is round, binary is modulus (threaded to level 0).
- Unary `m` is floor (threaded to level 0), binary is minimum.
- Unary `M` is ceiling (threaded to level 0), binary is maximum.
- Unary `x` is Cartesian product, binary is XOR (threaded to level 0).
- Unary `b` is conversion to base 2, binary to given base (threaded to levels 1 on the left and 0 on the right).
- Unary `d` is conversion from base 2, binary from given base (threaded to level 1 on both sides).
- Binary `=` is equality.
- Unary `<` is decrementation and head of array, binary is less-than.
- Unary `>` is incrementation and tail of array, binary is greater-than.
- Unary `!` is factorial or permutations, binary is truncated factorial or sub-permutations (threaded to level 0 on the left).
- Unary `c` is conversion to char (threaded to level 0), binary is subset check with multiplicities.
- Unary `C` is power-of-two or subsequences, binary is binomial coefficient or combinations (threaded to level 0 on the left).
- Unary `n` is conversion to num (threaded to level 0), binary is intersection.
- Unary `u` is uniques, binary is union.
- Unary `N` is negation, binary is list difference.
- Unary `#` is length of array and length of base-10 representation of number, binary is repetition.
- Unary `k` converts from bitmasks to lists of indices (threaded to level 1).
- Unary `K` converts from lists of indices to bitmasks (threaded to level 1).
- Unary `r` is range from 0, binary from left input to right. Arrays give multidimensional ranges.
- Unary `,` is flatten, binary is concatenation.
- Unary `;` wraps into a singleton array, binary gives a pair.
- Unary `$` gives the dimensions of an input array, binary reshapes right input to the shape in its left (threaded to level 1 on the left).
- Unary `@` lists the indices of all atoms in the input, binary indexes into right input using left (threaded to level 1 on the left).

### Operators

Not all input combinations are supported, and not all supported combinations are fully documented here.

- Binary `_`, if given two functions, returns the left (southern) one. Its main purpose is to give arguments to operators that only take values. If given a function and a value, the resulting function ignores its own arguments and returns the function applied to the value.
- Unary `~` on value gives a function that always returns that value, on function flips its arguments.
- Binary `~` on two values gives a function that always returns their pair, on function+value fixes the respective input (currying), on two functions gives their composition (using binary form of left function).
- Unary `&` swaps the arity of a function.
- Binary `&` on function+value curries the value from both sides, on two functions gives composition of functions (using binary form of right function).
- `(` and `)` are left and right hooks: `g(f(a), b)` and `f(a, g(b))` on input functions `f g` and argument values `a b`.
- `[` and `]` are left and right forks: `g(f(a, b), b)` and `f(a, g(a, b))` on input functions `f g` and argument values `a b`.
- Unary `` ` `` threads its argument to level 0; values are converted to constant functions.
- Binary `` ` `` threads its function argument to the levels (unary, left, right) given by its value argument. If both inputs are functions, the level is dynamic and given by the left function.
- Binary `L` applies its right argument to the level indicated by the left argument, and returns the results in a flat list. The unary version defaults to level 0.
- Unary `/` on value `f` is join. It concatenates its argument `f` times. If two arguments are given, it intersperses the left argument into the right, and then concatenates `f` times.
- Unary `/` on function is fold (aka reduce) from the left. If two arguments are given to the resulting function, the left is used as the initial value.
- Binary `/` is a generalized "if".
- Unary `\` applies the function to all prefixes, or substrings of given length. Given a value, it lists the substrings of that length. `0` means all substrings. With two arguments, it selects from them using the operator argument as a boolean mask.
- Binary `\` is iteration. Apply a function to argument given number of times, or until given value is found, or until a condition is met.