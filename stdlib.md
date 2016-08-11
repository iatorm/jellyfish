# Standard library

## Notation

In this document, the arguments of functions are **a** and **b** (with binary), function arguments of operators are **f** and **g** (with binary), and value arguments of operators are **x** and **y** (with binary).
The first argument is south, the second is east.
Monospace font is reserved for Jellyfish code.
Lists are compared in lexicographical order, and atoms are strictly lower than lists.
Any input combination not listed here is unimplemented, and for 0-threaded functions, list inputs are not listed either.

## Functions

Threading levels are for unary **a**, binary **a** and binary **b**.
Level -1 means no threading.
A **'** after an argument means that atomic arguments are converted to singleton lists.

| Symbol | Arguments                  | Threading | Result | Notes |
| :----: | -------------------------- | --------- | ------ | ----- |
| `{`    | **a** (any)                | -1        | **a** |
|        | **a** (any), **b** (any)   | -1, -1    | **a** |
| `}`    | **a** (any)                | -1        | **a** |
|        | **a** (any), **b** (any)   | -1, -1    | **b** |
| `j`    | **a** (any)                | -1        | Read STDIN and eval |
| `J`    | **a** (any)                | -1        | Read STDIN as string |
| `p`    | **a** (any)                | -1        | Print **a** to STDOUT, return **a** |
| `P`    | **a** (any)                | -1        | Print **a** to STDOUT in matrix format, return **a** |
| `+`    | **a** (atom)               |  0        | **abs(a)** |
|        | **a** (atom), **b** (atom) |  0,  0    | **a + b** |
| `-`    | **a** (atom)               |  0        | **-a** |
|        | **a** (atom), **b** (atom) |  0,  0    | **b - a** |
| `*`    | **a** (atom)               |  0        | **sign(a)** |
|        | **a** (atom), **b** (atom) |  0,  0    | **a * b** |
| `%`    | **a** (atom)               |  0        | **1 / a** | Return **0** for **a = 0** |
|        | **a** (atom), **b** (atom) |  0,  0    | **b / a** | Return **0** for **a = 0** |
| `|`    | **a** (atom)               |  0        | **round(a)** |
|        | **a** (atom), **b** (atom) |  0,  0    | **b mod a** | Return **0** for **a = 0** |
| `m`    | **a** (atom)               |  0        | **floor(a)** |
|        | **a** (any), **b** (any)   | -1, -1    | **min(a, b)** |
| `M`    | **a** (atom)               |  0        | **ceiling(a)** |
|        | **a** (any), **b** (any)   | -1, -1    | **max(a, b)** |
| `x`    | **a** (atom)               | -1        | **a** |
|        | **a** (list)               | -1        | Cartesian product of items of **a** |
|        | **a** (atom), **b** (atom) |  0,  0    | **a xor b** |
| `b`    | **a** (atom)               |  0        | Base-2 digits of **a** |
|        | **a** (any), **b** (atom)  |  1,  0    | Base-**a** digits of **b** |
| `d`    | **a** (any)                |  1        | Digit(s) **a** as base-2 number |
|        | **a** (any), **b** (any)   |  1,  1    | Digit(s) **b** as base-**a** number |
| `<`    | **a** (atom)               | -1        | **a - 1** |
|        | **a** (list)               | -1        | **head(a)** |
|        | **a** (any), **b** (any)   | -1, -1    | **1** if **a < b**, otherwise **0** |
| `>`    | **a** (atom)               | -1        | **a + 1** |
|        | **a** (list)               | -1        | **tail(a)** |
|        | **a** (any), **b** (any)   | -1, -1    | **1** if **a > b**, otherwise **0** |
| `!`    | **a** (atom)               | -1        | **a!** |
|        | **a** (list)               | -1        | Permutations of **a** |
|        | **a** (atom), **b** (atom) |  0, -1    | **b! / (b-a)!** |
|        | **a** (atom), **b** (list) |  0, -1    | Length-**a** permutations of **b** |
| `c`    | **a** (atom)               |  0        | **char(a)** |
|        | **a'** (list), **b'** (list)| -1, -1   | **1** if **a** is a sub-multiset of **b**, otherwise **0** |
| `C`    | **a** (atom)               | -1        | **2<sup>a</sup>** |
|        | **a** (list)               | -1        | Subsequences of **a** |
|        | **a** (atom), **b** (atom) |  0, -1    | **b! / a!\*(b-a)!** |
|        | **a** (atom), **b** (list) |  0, -1    | Length-**a** subsequences of **b** |
| `n`    | **a** (atom)               |  0        | **num(a)** |
|        | **a'** (list), **b'** (list)| -1, -1   | Intersection of **a** and **b** |
| `u`    | **a'** (list)              | -1        | **uniques(a)** |
|        | **a'** (list), **b'** (list)| -1, -1   | Union of **a** and **b** |
| `N`    | **a** (any)                | -1        | **0** if **a** is truthy, **1** otherwise |
|        | **a'** (list), **b'** (list)| -1, -1   | **a** with items of **b** removed |
| `#`    | **a** (atom)               | -1        | Number of base-10 digits in **a** |
|        | **a** (list)               | -1        | Length of **a** |
|        | **a** (atom), **b'** (list)| -1, -1    | Each item of **b** repeated **a** times |
|        | **a** (list), **b'** (list)| -1, -1    | Each item of **b** repeated by the corresponding item of **a** |
| `R`    | **a** (atom)               | -1        | **a** |
|        | **a** (list)               | -1        | **a** reversed |
|        | **a** (atom), **b** (atom) |  0, -1    | **b** |
|        | **a** (atom), **b** (list) |  0, -1    | **b** rotated **a** steps to the left |
| `k`    | **a'** (list)              |  1        | Convert bitmask **a** to list of indices |
| `K`    | **a'** (list)              |  1        | Convert list of indices **a** to bitmask |
| `r`    | **a** (atom)               | -1        | Range from **0** to **a-1** | From **a+1** to **0** if **a < 0** |
|        | **a** (list)               | -1        | Cartesian product of ranges for atoms in **a** |
|        | **a** (any), **b** (any)   | -1, -1    | Range from **a** to **b-1**, or Cartesian product of ranges like above |
| `,`    | **a** (any)                | -1        | **flatten(a)** |
|        | **a** (any), **b** (any)   | -1, -1    | **concatenate(a, b)** |
| `;`    | **a** (any)                | -1        | **[a]** |
|        | **a** (any), **b** (any)   | -1, -1    | **[a, b]** |
| `$`    | **a** (any)                | -1        | Shape vector of **a** |
|        | **a'** (list), **b** (any) |  1, -1    | **b** reshaped according to shape vector **a** |
| `@`    | **a** (any)                | -1        | Indices of all atoms in **a** |
|        | **a'** (list), **b** (any) | -2, -1    | Item of **b** at (multidimensional) index **a** |

## Operators

In this table, threaded arguments are mentioned separately in the description.

| Symbol | Operator args              | Function args            | Result | Notes |
| :----: | -------------------------- | ------------------------ | ------ | ----- |
| `_`    | **f** (func)               | **a** (any)              | **f(a)** |
|        |                            | **a** (any), **b** (any) | **f(a, b)** |
|        | **f** (func), **y** (val)  | **a (,b)** (any)         | **f(y)** |
|        | **x** (val), **g** (func)  | **a (,b)** (any)         | **g(x)** |
|        | **f** (func), **g** (func) | **a** (any)              | **f(a)** |
|        |                            | **a** (any), **b** (any) | **f(a, b)** |
| `~`    | **x** (val)                | **a (, b)** (any)        | **x** |
|        | **f** (func)               | **a** (any)              | **f(a)** |
|        |                            | **a** (any), **b** (any) | **f(b, a)** |
|        | **x** (val), **y** (val)   | **a (,b)** (any)         | **[x, y]** |
|        | **f** (func), **y** (val)  | **a (,b)** (any)         | **f(a, y)** |
|        | **x** (val), **g** (func)  | **a** (any)              | **g(x, a)** |
|        |                            | **a** (any), **b** (any) | **g(x, b)** |
|        | **f** (func), **g** (func) | **a** (any)              | **f(g(a))** |
|        |                            | **a** (any), **b** (any) | **f(g(a), g(b))** |
| `&`    | **f** (func)               | **a** (any)              | **f(a, a)** |
|        |                            | **a** (any), **b** (any) | **f(b)** |
|        | **f** (func), **y** (val)  | **a** (any)              | **f(f(y, a), y)** |
|        |                            | **a** (any), **b** (any) | **b → f(f(y, b), y)** iterated **a** times |
|        | **x** (val), **g** (func)  | **a** (any)              | **g(x, g(a, x))** |
|        |                            | **a** (any), **b** (any) | **b → g(x, g(b, x))** iterated **a** times |
|        | **f** (func), **g** (func) | **a** (any)              | **f(g(a))** |
|        |                            | **a** (any), **b** (any) | **f(g(a, b))** |
| `(`    | **f** (func)               | **a** (any)              | **[f(a), a]** |
|        |                            | **a** (any), **b** (any) | **[f(a), b]** |
|        | **f** (func), **g** (func) | **a** (any)              | **g(f(a), a)** |
|        |                            | **a** (any), **b** (any) | **g(f(a), b)** |
| `)`    | **f** (func)               | **a** (any)              | **[a, f(a)]** |
|        |                            | **a** (any), **b** (any) | **[a, f(b)]** |
|        | **f** (func), **g** (func) | **a** (any)              | **f(a, g(a))** |
|        |                            | **a** (any), **b** (any) | **f(a, g(b))** |
| `[`    | **f** (func)               | **a** (any)              | **[f(a), a]** |
|        |                            | **a** (any), **b** (any) | **[f(a, b), b]** |
|        | **f** (func), **g** (func) | **a** (any)              | **g(f(a), a)** |
|        |                            | **a** (any), **b** (any) | **g(f(a, b), b)** |
| `]`    | **f** (func)               | **a** (any)              | **[a, f(a)]** |
|        |                            | **a** (any), **b** (any) | **[a, f(a, b)]** |
|        | **f** (func), **g** (func) | **a** (any)              | **f(a, g(a))** |
|        |                            | **a** (any), **b** (any) | **f(a, g(a, b))** |
| `` ` ``| **x** (val)                | **a (,b)** (any)         | **~(x)** threaded to level **0** |
|        | **f** (func)               | **a (,b)** (any)         | **f** threaded to level **0** |
|        | **x** (val), **y** (val)   | **a (,b)** (any)         | **~(x)** threaded to level(s) **y** | **y** is reshaped to shape **[3]** |
|        | **f** (func), **y** (val)  | **a (,b)** (any)         | **f** threaded to level(s) **y** | **y** is reshaped to shape **[3]** |
|        | **x** (val), **g** (func)  | **a (,b)** (any)         | **g** threaded to level(s) **x** | **x** is reshaped to shape **[3]** |
|        | **f** (func), **g** (func) | **a** (any)              | **g(a)**, with **g** threaded to level(s) **f(a)** | **f(a)** is reshaped to shape **[3]** |
|        |                            | **a** (any), **b** (any) | **g(a, b)**, with **g** threaded to level(s) **f(a, b)** | **f(a, b)** is reshaped to shape **[3]** |
| `L`    | **x** (val)                | **a** (any)              | Items of **a** of height **x** or greater |
|        |                            | **a** (any), **b** (any) | Items of **a** and **b** of height **x** or greater, paired together |
|        | **f** (func)               | **a** (any)              | **f** applied to atoms of **a** |
|        |                            | **a** (any), **b** (any) | **f** applied to atom-pairs of **a** and **b** |
|        | **x** (val), **y** (val)   | **a** (any)              | **~(y)** applied to items of **a** of height **x** or greater |
|        |                            | **a** (any), **b** (any) | **~(y)** applied to item-pairs of **a** and **b** of height **x** or greater |
|        | **f** (func), **y** (val)  | **a** (any)              | **~(y)** applied to items of **a** of height **f(a)** or greater |
|        |                            | **a** (any), **b** (any) | **~(y)** applied to item-pairs of **a** and **b** of height **f(a, b)** or greater |
|        | **x** (val), **g** (func)  | **a** (any)              | **g** applied to items of **a** of height **x** or greater |
|        |                            | **a** (any), **b** (any) | **g** applied to item-pairs of **a** and **b** of height **x** or greater |
|        | **f** (func), **g** (func) | **a** (any)              | **g** applied to items of **a** of height **f(a)** or greater |
|        |                            | **a** (any), **b** (any) | **g** applied to item-pairs of **a** and **b** of height **f(a, b)** or greater |
| `/`    | **x** (val)                | **a** (any)              | Join **a** **x** times | **x** threaded to level 0 |
|        |                            | **a** (any), **b** (any) | Insert copies of **a** between items of **b**, and join **x** times | **x** threaded to level 0 |
|        | **f** (func)               | **a** (any)              | Fold **f** over **a** from the left |
|        |                            | **a** (any), **b** (any) | Fold **f** over **b** from the left with initial value **a** |
|        | **x** (val), **y** (val)   | **a** (any)              | **x** if **a** is truthy, else **y** |
|        |                            | **a** (any), **b** (any) | **[x, b]** if **a** is truthy, else **[y, b]** |
|        | **f** (func), **y** (val)  | **a** (any)              | **f(y)** if **a** is truthy, else **y** |
|        |                            | **a** (any), **b** (any) | **f(b)** if **a** is truthy, else **y** |
|        | **x** (val), **g** (func)  | **a** (any)              | **g(a)** if **f** is truthy, else **a** |
|        |                            | **a** (any), **b** (any) | **g(b)** if **f** is truthy, else **g(a)** |
|        | **f** (func), **g** (func) | **a** (any)              | **g(a)** if **f(a)** is truthy, else **a** |
|        |                            | **a** (any), **b** (any) | **f(b)** if **a** is truthy, else **g(b)** |
| `\`    | **x** (val)                | **a** (any)              | Substrings of **a** of length **x** | **x < 0** gives non-overapping substrings; **x** threaded to level 0 |
|        |                            | **a** (any), **b** (any) | Select item from **a** if **x** is even, from **b** if odd | Threaded to level -2 for **a** and **b**, level 0 for **x** |
|        | **f** (func)               | **a** (any)              | **f(p)** for every prefix **p** of **a** |
|        |                            | **a** (any), **b** (any) | **f(s)** for every length-**a** substring of **b** | **a** threaded to level 0 |
|        | **f** (func), **y** (val)  | **a** (any)              | Iterate **f** on **a** **y** times | **y** threaded to level 0 |
|        |                            | **a** (any), **b** (any) | Iterate **~(a, f)** on **b** **y** times | **y** threaded to level 0 |
|        | **x** (val), **g** (func)  | **a** (any)              | Iterate **g** on **a** until **x** occurs, return each step |
|        |                            | **a** (any), **b** (any) | Iterate **~(a, g)** on **b** until **x** occurs, return each step |
|        | **f** (func), **g** (func) | **a** (any)              | Iterate **f** on **a** until **g(a, f(a))** is truthy |
|        |                            | **a** (any), **b** (any) | Iterate **~(a, f)** on **b** until **g(b, f(a, b))** is truthy |
