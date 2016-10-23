
# Jellyfish tutorial

This is a tutorial for the esoteric programming language Jellyfish.
It will cover those parts of the language that are not very likely to change radically in the future.
To try out the examples, you can use either the command line interpreter, or the [online interpreter](http://jellyfish.tryitonline.net/) provided by Dennis.
A function listing can be found [here](https://github.com/iatorm/jellyfish/blob/master/stdlib.md).

## First steps

Let's try our hand with the classic "Hello world" program:

    P "Hello, world!"

That's it: `P` is the Jellyfish function that prints its argument to STDOUT, and `"Hello, world!"` is a string literal.

Once you have this program up and running, let's analyze it a little.
In Jellyfish, most functions have a unary (one-argument) form and a binary (two-argument) form.
The print function `P` only has a unary form, but we'll encounter binary functions soon enough.
Jellyfish programs are parsed as grids.
In the above program, the function `P` lies at the coordinate **(0,0)**, while the string literal lies at the position of its left quote, or **(2,0)**.
A function will look for two arguments: one to the south, and one to the east, ignoring all empty coordinates in between.
If two arguments are found, the binary form of the function is used; if just one, the unary form.
In this case, the function `P` doesn't find an argument to the south, but finds the string literal in the east, and thus applies its unary form to that argument.

Now, let's try something a bit more complex: a program that adds 1 and 2, and prints the result:

    P + 1
      2

The function `+` in its binary form performs addition, in this case on the numeric literals `1` and `2`.
The function `P` finds the function `+`, and uses its result as its own argument.
The binary arithmetic functions `+-*%` all behave as expected (`%` is division), although the argument order may be surprising.
For example, `-` subtracts its south argument from its east argument.

## Input

The easiest way of getting user input in Jellyfish are the input literals `i` and `I`.
At the beginning of execution, every `i` in the source code is replaced by an evaluated value taken from STDIN, and every `I` is replaced by an unevaluated string taken from STDIN.
For example, here's a program for incrementing a given number:

    P + i
      1

Here's a program for adding two numbers, given on different lines:

    P + i
      i

The replacement is done in the normal English reading order, so the `i` on the first line is the first input, and the `i` on the second line is the second input.

The binary function `,` performs list and string concatenation, so the following program takes a name from STDIN and prints a greeting:

    P ,         , "!"
      "Hello, " I

There are two `,`s here, one for appending a `!` to the name, and one for prepending the `Hello`.

## Lists

There are only three datatypes in Jellyfish: numbers, characters (which are really a type of number), and lists.
Lists can be nested arbitrarily, and they can hold any type of data.
The syntax for lists, as they are taken from STDIN, is `[0 1 2 "hello" [2 4 'x']]`: a list begins with `[`, contains items that are separated by spaces, and ends with `]`.
The single-quoted `'x'` is a character, and the string syntax `"hello"` is really just a shorthand for  a list of characters `['h' 'e' 'l' 'l' 'o']`.
Note that there is no syntax for list literals in the source code, so you'll have to build lists manually using functions like `,` (flatten/concatenate) and `;` (singleton/pair).
For example, the list `[0 3 6 4]` would be represented by

    , , , 4
    0 3 6

The function `P` prints lists in a "matrix format".
This means that a nested list of numbers is printed as a beautiful grid: the program

    P i

with input

    [[10 2 7] [2 45 -4] [0 256 0]]

results in

    10   2  7
     2  45 -4
     0 256  0

However, if the lists are not as nicely nested, `P` will throw an error.
In that case, you should use the `p` function, which prints its argument in the input format.

There are a number of functions in Jellyfish that deal with lists.
Let's look at `#` (length/repeat) first.
The unary form simply computes the length of a given list.
For example, the program

    P # "Hello"

will print `5`.
The binary form takes two lists, and repeats each element of the east argument a number of times given by its south argument.
For example, the program

    P # "Hello"
      , , , , 1
      2 1 0 0

will print `HHeo`.
The last two rows construct the list `[2 1 0 0 1]`, which is paired with `"Hello"`, and the `H` is repeated twice, `e` and `o` once, and both `l`s zero times.
The binary form of `#` is mostly used as a "filter", where the south argument is a 0-1 list representing some property of the elements, and all elements without the property are removed.

Some other list-manipulating functions are `R` (reverse/rotate), `o` (order) and `r` (range).
You can find their descriptions in the reference file.

## Threading

*TODO*

## Redirection commands

*TODO*

## Operators

*TODO*