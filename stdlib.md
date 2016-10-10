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

| Symbol | Name               | Arguments                  | Threading | Result | Notes |
| :----: | ------------------ | -------------------------- | --------- | ------ | ----- |
| `{`    | Left identity      | **a** (any)                | -1        | **a** |
|        |                    | **a** (any), **b** (any)   | -1, -1    | **a** |
| `}`    | Right identity     | **a** (any)                | -1        | **a** |
|        |                    | **a** (any), **b** (any)   | -1, -1    | **b** |
| `j`    | Read value         | **a** (any)                | -1        | Read STDIN and eval |
| `j`    | Eval/uneval        | **a** (atom), **b** (any)  |  0, -1    | If **a > 0**, evaluate string **b**, otherwise convert **b** to string | If **a > 0**, a multidimensional **b** is flattened before conversion
| `J`    | Read string        | **a** (any)                | -1        | Read STDIN as string |
| `J`    | Read chars         | **a** (any), **b** (atom)  | -1,  0    | Read **b** characters from STDIN | Stops if EOF is encountered, reads entire STDIN if **b < 0** |
| `p`    | Print              | **a** (any)                | -1        | Print **a** to STDOUT, return **a** |
| `P`    | Matrix print       | **a** (any)                | -1        | Print **a** to STDOUT in matrix format, return **a** |
| `+`    | Abs                | **a** (atom)               |  0        | **abs(a)** |
|        | Add                | **a** (atom), **b** (atom) |  0,  0    | **a + b** |
| `-`    | Negate             | **a** (atom)               |  0        | **-a** |
|        | Subtract           | **a** (atom), **b** (atom) |  0,  0    | **b - a** |
| `*`    | Signum             | **a** (atom)               |  0        | **sign(a)** |
|        | Multiply           | **a** (atom), **b** (atom) |  0,  0    | **a * b** |
| `%`    | Reciprocal         | **a** (atom)               |  0        | **1 / a** | Return **0** for **a = 0** |
|        | Divide             | **a** (atom), **b** (atom) |  0,  0    | **b / a** | Return **0** for **a = 0** |
| `|`    | Round              | **a** (atom)               |  0        | **round(a)** |
|        | Modulus            | **a** (atom), **b** (atom) |  0,  0    | **b mod a** | Return **0** for **a = 0** |
| `m`    | Floor              | **a** (atom)               |  0        | **floor(a)** |
|        | Minimum            | **a** (any), **b** (any)   | -1, -1    | **min(a, b)** |
| `M`    | Ceiling            | **a** (atom)               |  0        | **ceiling(a)** |
|        | Maximum            | **a** (any), **b** (any)   | -1, -1    | **max(a, b)** |
| `x`    | Cartesian product  | **a** (atom)               | -1        | **a** |
|        |                    | **a** (list)               | -1        | Cartesian product of items of **a** |
|        | XOR                | **a** (atom), **b** (atom) |  0,  0    | **a xor b** |
| `b`    | Base encode        | **a** (atom)               |  0        | Base-2 digits of **a** |
|        |                    | **a** (any), **b** (atom)  |  1,  0    | Base-**a** digits of **b** |
| `d`    | Base decode        | **a** (any)                |  1        | Digit(s) **a** as base-2 number |
|        |                    | **a** (any), **b** (any)   |  1,  1    | Digit(s) **b** as base-**a** number |
| `=`    | Equality           | **a** (any), **b** (any)   | -1, -1    | **1** if **a = b**, otherwise **0** |
| `<`    | Decrement          | **a** (atom)               | -1        | **a - 1** |
|        | Head               | **a** (list)               | -1        | **head(a)** |
|        | Less than          | **a** (any), **b** (any)   | -1, -1    | **1** if **a < b**, otherwise **0** |
| `>`    | Increment          | **a** (atom)               | -1        | **a + 1** |
|        | Tail               | **a** (list)               | -1        | **tail(a)** |
|        | Greater than       | **a** (any), **b** (any)   | -1, -1    | **1** if **a > b**, otherwise **0** |
| `!`    | Factorial          | **a** (atom)               | -1        | **a!** |
|        | Permutations       | **a** (list)               | -1        | Permutations of **a** |
|        | Falling factorial  | **a** (atom), **b** (atom) |  0, -1    | **b! / (b-a)!** |
|        | K-permutations     | **a** (atom), **b** (list) |  0, -1    | Length-**a** permutations of **b** |
| `c`    | Character          | **a** (atom)               |  0        | **char(a)** |
|        | Element            | **a** (any), **b'** (list) | -1, -1    | **1** if **a** occurs in **b**, otherwise **0** |
| `C`    | Power of two       | **a** (atom)               | -1        | **2<sup>a</sup>** |
|        | Subsequences       | **a** (list)               | -1        | Subsequences of **a** |
|        | Binomial           | **a** (atom), **b** (atom) |  0, -1    | **b! / a!\*(b-a)!** |
|        | K-subsequences     | **a** (atom), **b** (list) |  0, -1    | Length-**a** subsequences of **b** |
| `n`    | Number             | **a** (atom)               |  0        | **num(a)** |
|        | Intersection       | **a'** (list), **b'** (list)| -1, -1   | Intersection of **a** and **b** |
| `u`    | Uniques            | **a'** (list)              | -1        | **uniques(a)** |
|        | Union              | **a'** (list), **b'** (list)| -1, -1   | Union of **a** and **b** |
| `N`    | Logical negation   | **a** (any)                | -1        | **0** if **a** is truthy, **1** otherwise |
|        | List difference    | **a'** (list), **b'** (list)| -1, -1   | **a** with items of **b** removed |
| `#`    | Length             | **a** (atom)               | -1        | Number of base-10 digits in **a** |
|        |                    | **a** (list)               | -1        | Length of **a** |
|        | Repeat             |  **a** (atom), **b'** (list)| -1, -1    | Each item of **b** repeated **a** times |
|        | Repeat/filter      | **a** (list), **b'** (list)| -1, -1    | Each item of **b** repeated by the corresponding item of **a** |
| `R`    | Reverse            | **a** (atom)               | -1        | **a** |
|        |                    | **a** (list)               | -1        | **a** reversed |
|        | Rotate             | **a** (atom), **b** (atom) |  0, -1    | **b** |
|        |                    | **a** (atom), **b** (list) |  0, -1    | **b** rotated **a** steps to the left |
| `k`    | To indices         | **a'** (list)              |  1        | Convert bitmask **a** to list of indices |
| `K`    | To bitmask         | **a'** (list)              |  1        | Convert list of indices **a** to bitmask |
| `r`    | Range              | **a** (atom)               | -1        | Range from **0** to **a-1** | From **a+1** to **0** if **a < 0** |
|        |                    | **a** (list)               | -1        | Cartesian product of ranges for atoms in **a** |
|        |                    | **a** (any), **b** (any)   | -1, -1    | Range from **a** to **b-1**, or Cartesian product of ranges like above |
| `,`    | Flatten            | **a** (any)                | -1        | **flatten(a)** |
|        | Concatenate        | **a** (any), **b** (any)   | -1, -1    | **concatenate(a, b)** |
| `;`    | Singleton          | **a** (any)                | -1        | **[a]** |
|        | Pair               | **a** (any), **b** (any)   | -1, -1    | **[a, b]** |
| `$`    | Shape              | **a** (any)                | -1        | Shape vector of **a** |
|        | Reshape            | **a'** (list), **b** (any) |  1, -1    | **b** reshaped according to shape vector **a** |
| `@`    | Indices            | **a** (any)                | -1        | Indices of all atoms in **a** |
|        | Index into         | **a'** (list), **b** (any) | -2, -1    | Item of **b** at (multidimensional) index **a** |
| `?`    | Random             | **a** (atom)               | -1        | Random number between **0** and **a** | If **a = 0**, random float between **0** and **1** |
|        |                    | **a** (list)               | -1        | Random permutation of **a** |
|        |                    | **a** (atom), **b** (atom) |  1, -1    | **a** random elements between **0** and **b** in order |
|        |                    | **a** (atom), **b** (list) |  1, -1    | **a** random elements of **b** in order |
|        |                    | **a** (list), **b** (atom) |  1, -1    | Disjoint random subsequences of **range(b)**, lengths given by **a** |
|        |                    | **a** (list), **b** (list) |  1, -1    | Disjoint random subsequences of **b**, lengths given by **a** |

## Operators

In this table, threaded arguments are mentioned separately in the description.

| Symbol | Name       | Operator args              | Function args            | Result | Notes |
| :----: | ---------- | -------------------------- | ------------------------ | ------ | ----- |
| `_`    | Call       | **f** (func)               | **a** (any)              | **f(a)** |
|        |            |                            | **a** (any), **b** (any) | **f(a, b)** |
|        |            | **f** (func), **y** (val)  | **a (,b)** (any)         | **f(y)** |
|        |            | **x** (val), **g** (func)  | **a (,b)** (any)         | **g(x)** |
|        |            | **f** (func), **g** (func) | **a** (any)              | **f(a)** |
|        |            |                            | **a** (any), **b** (any) | **f(a, b)** |
| `~`    | Constant   | **x** (val)                | **a (, b)** (any)        | **x** |
|        | Flip       | **f** (func)               | **a** (any)              | **f(a)** |
|        |            |                            | **a** (any), **b** (any) | **f(b, a)** |
|        | Constant   | **x** (val), **y** (val)   | **a (,b)** (any)         | **[x, y]** |
|        | Curry      | **f** (func), **y** (val)  | **a (,b)** (any)         | **f(a, y)** |
|        |            | **x** (val), **g** (func)  | **a** (any)              | **g(x, a)** |
|        |            |                            | **a** (any), **b** (any) | **g(x, b)** |
|        | Compose    | **f** (func), **g** (func) | **a** (any)              | **f(g(a))** |
|        |            |                            | **a** (any), **b** (any) | **f(g(a), g(b))** |
| `&`    | Swap arity | **f** (func)               | **a** (any)              | **f(a, a)** |
|        |            |                            | **a** (any), **b** (any) | **f(b)** |
|        | Bi-compose | **f** (func), **y** (val)  | **a** (any)              | **f(f(y, a), y)** |
|        |            |                            | **a** (any), **b** (any) | **b → f(f(y, b), y)** iterated **a** times |
|        |            | **x** (val), **g** (func)  | **a** (any)              | **g(x, g(a, x))** |
|        |            |                            | **a** (any), **b** (any) | **b → g(x, g(b, x))** iterated **a** times |
|        | Compose    | **f** (func), **g** (func) | **a** (any)              | **f(g(a))** |
|        |            |                            | **a** (any), **b** (any) | **f(g(a, b))** |
| `(`    | Left hook  | **f** (func)               | **a** (any)              | **[f(a), a]** |
|        |            |                            | **a** (any), **b** (any) | **[f(a), b]** |
|        |            | **f** (func), **g** (func) | **a** (any)              | **g(f(a), a)** |
|        |            |                            | **a** (any), **b** (any) | **g(f(a), b)** |
| `)`    | Right hook | **f** (func)               | **a** (any)              | **[a, f(a)]** |
|        |            |                            | **a** (any), **b** (any) | **[a, f(b)]** |
|        |            | **f** (func), **g** (func) | **a** (any)              | **f(a, g(a))** |
|        |            |                            | **a** (any), **b** (any) | **f(a, g(b))** |
| `[`    | Left fork  | **f** (func)               | **a** (any)              | **[f(a), a]** |
|        |            |                            | **a** (any), **b** (any) | **[f(a, b), b]** |
|        |            | **f** (func), **g** (func) | **a** (any)              | **g(f(a), a)** |
|        |            |                            | **a** (any), **b** (any) | **g(f(a, b), b)** |
| `]`    | Right fork | **f** (func)               | **a** (any)              | **[a, f(a)]** |
|        |            |                            | **a** (any), **b** (any) | **[a, f(a, b)]** |
|        |            | **f** (func), **g** (func) | **a** (any)              | **f(a, g(a))** |
|        |            |                            | **a** (any), **b** (any) | **f(a, g(a, b))** |
| `` ` ``| Thread     | **x** (val)                | **a (,b)** (any)         | **~(x)** threaded to level **0** |
|        |            | **f** (func)               | **a (,b)** (any)         | **f** threaded to level **0** |
|        |            | **x** (val), **y** (val)   | **a (,b)** (any)         | **~(x)** threaded to level(s) **y** | **y** is reshaped to shape **[3]** |
|        |            | **f** (func), **y** (val)  | **a (,b)** (any)         | **f** threaded to level(s) **y** | **y** is reshaped to shape **[3]** |
|        |            | **x** (val), **g** (func)  | **a (,b)** (any)         | **g** threaded to level(s) **x** | **x** is reshaped to shape **[3]** |
|        |            | **f** (func), **g** (func) | **a** (any)              | **g(a)**, with **g** threaded to level(s) **f(a)** | **f(a)** is reshaped to shape **[3]** |
|        |            |                            | **a** (any), **b** (any) | **g(a, b)**, with **g** threaded to level(s) **f(a, b)** | **f(a, b)** is reshaped to shape **[3]** |
| `L`    | Levels     | **x** (val)                | **a** (any)              | Items of **a** of height **x** or greater |
|        |            |                            | **a** (any), **b** (any) | Items of **a** and **b** of height **x** or greater, paired together |
|        |            | **f** (func)               | **a** (any)              | **f** applied to atoms of **a** |
|        |            |                            | **a** (any), **b** (any) | **f** applied to atom-pairs of **a** and **b** |
|        |            | **x** (val), **y** (val)   | **a** (any)              | **~(y)** applied to items of **a** of height **x** or greater |
|        |            |                            | **a** (any), **b** (any) | **~(y)** applied to item-pairs of **a** and **b** of height **x** or greater |
|        |            | **f** (func), **y** (val)  | **a** (any)              | **~(y)** applied to items of **a** of height **f(a)** or greater |
|        |            |                            | **a** (any), **b** (any) | **~(y)** applied to item-pairs of **a** and **b** of height **f(a, b)** or greater |
|        |            | **x** (val), **g** (func)  | **a** (any)              | **g** applied to items of **a** of height **x** or greater |
|        |            |                            | **a** (any), **b** (any) | **g** applied to item-pairs of **a** and **b** of height **x** or greater |
|        |            | **f** (func), **g** (func) | **a** (any)              | **g** applied to items of **a** of height **f(a)** or greater |
|        |            |                            | **a** (any), **b** (any) | **g** applied to item-pairs of **a** and **b** of height **f(a, b)** or greater |
| `/`    | Join       | **x** (val)                | **a** (any)              | Join **a** **x** times | **x** threaded to level 0 |
|        |            |                            | **a** (any), **b** (any) | Insert copies of **a** between items of **b**, and join **x** times | **x** threaded to level 0 |
|        | Fold       | **f** (func)               | **a** (any)              | Fold **f** over **a** from the left |
|        |            |                            | **a** (any), **b** (any) | Fold **f** over **b** from the left with initial value **a** |
|        | If         | **x** (val), **y** (val)   | **a** (any)              | **x** if **a** is truthy, else **y** |
|        |            |                            | **a** (any), **b** (any) | **[x, b]** if **a** is truthy, else **[y, b]** |
|        |            | **f** (func), **y** (val)  | **a** (any)              | **f(y)** if **a** is truthy, else **y** |
|        |            |                            | **a** (any), **b** (any) | **f(b)** if **a** is truthy, else **y** |
|        |            | **x** (val), **g** (func)  | **a** (any)              | **g(a)** if **f** is truthy, else **a** |
|        |            |                            | **a** (any), **b** (any) | **g(b)** if **f** is truthy, else **g(a)** |
|        |            | **f** (func), **g** (func) | **a** (any)              | **g(a)** if **f(a)** is truthy, else **a** |
|        |            |                            | **a** (any), **b** (any) | **f(b)** if **a** is truthy, else **g(b)** |
| `\`    | Substrings | **x** (val)                | **a** (any)              | Substrings of **a** of length **x** | **x < 0** gives non-overapping substrings; **x** threaded to level 0 |
|        | Select     |                            | **a** (any), **b** (any) | Select item from **a** if **x** is even, from **b** if odd | Threaded to level -2 for **a** and **b**, level 0 for **x** |
|        | Prefixes   | **f** (func)               | **a** (any)              | **f(p)** for every prefix **p** of **a** |
|        | Substrings |                            | **a** (any), **b** (any) | **f(s)** for every length-**a** substring of **b** | **a** threaded to level 0 |
|        | Iterate    | **f** (func), **y** (val)  | **a** (any)              | Iterate **f** on **a** **y** times | **y** threaded to level 0 |
|        |            |                            | **a** (any), **b** (any) | Iterate **~(a, f)** on **b** **y** times | **y** threaded to level 0 |
|        |            | **x** (val), **g** (func)  | **a** (any)              | Iterate **g** on **a** until **x** occurs, return each step |
|        |            |                            | **a** (any), **b** (any) | Iterate **~(a, g)** on **b** until **x** occurs, return each step |
|        |            | **f** (func), **g** (func) | **a** (any)              | Iterate **f** on **a** until **g(a, f(a))** is truthy |
|        |            |                            | **a** (any), **b** (any) | Iterate **~(a, f)** on **b** until **g(b, f(a, b))** is truthy |
| `Z`    | Replace at | **x** (val), **y** (val)   | **a** (any)              | **a** with elements at indices **x** replaced by corresponding items of **y** |
|        |            |                            | **a** (any), **b** (any) | **b** with elements at indices **x** replaced by corresponding items of **y** |
|        |            | **f** (func), **y** (val)  | **a** (any)              | **a** with elements at indices **f(a)** replaced by corresponding items of **y** |
|        |            |                            | **a** (any), **b** (any) | **b** with elements at indices **f(a, b)** replaced by corresponding items of **y** |
|        |            | **x** (val), **g** (func)  | **a** (any)              | **a** with elements at indices **x** replaced by corresponding items of **g(a)** |
|        |            |                            | **a** (any), **b** (any) | **b** with elements at indices **x** replaced by corresponding items of **g(a, b)** |
|        |            | **f** (func), **g** (func) | **a** (any)              | **a** with elements at indices **f(a)** replaced by corresponding items of **g(a)** |
|        |            |                            | **a** (any), **b** (any) | **b** with elements at indices **f(a, b)** replaced by corresponding items of **g(a, b)** |
