# Standard library

## Notation

In this document, the arguments of functions are **a** and **b** (with binary), function arguments of operators are **f** and **g** (with binary), and value arguments of operators are **x** and **y** (with binary).
The first argument is south, the second is east.
Monospace font is reserved for Jellyfish code, and **NI** stands for not implemented.

## Functions

| Symbol | Unary | Binary |
| --- | --- | --- |
| `{` | **a** | **a** |
| `}` | **a** | **b** |
| `j` | Read STDIN and eval | **NI** |
| `J` | Read string from STDIN | **NI** |
| `p` | Print to STDOUT | **NI** |
| `P` | Print to STDOUT in matrix format | **NI** |
| `+` | **abs(a)** | **a + b** |
| `-` | **-a** | **b - a** |
| `*` | **sign(a)** | **a * b** |
| `%` | **1 / a** | **b / a** |
| `|` | **round(a)** | **b % a** (modulus) |
| `m` | **floor(a)** | **min(a, b)** |
| `M` | **ceiling(a)** | **max(a, b)** |
| `x` | Cartesian product of items of **a** | **a XOR b** |
| `b` | Base-2 digits of **a** | Base-**a** digits of **b** |
| `d` | Digits **a** to base-2 number | Digits **b** to base-**a** number |
| `=` | **NI** | **a = b** |
| `<` | **a - 1** or **head(a)** | **a < b** |
| `>` | **a + 1** or **tail(a)** | **a > b** |
| `!` | **a!** or permutations of **a** | **b! / (b-a)!** or length-**a** sub-premutations of **b** |
| `c` | **char(a)** | Is **a** sub-multiset of **b**? |
| `C` | **2<sup>a</sup>** or subsequences of **a** | Binomial coefficient (**b** over **a**) or length-**a** subsequences of **b** |
| `n` | **num(a)** | Intersection of **a** and **b** |
| `u` | **uniques(a)** | Intersection of **a** and **b** |
| `N` | **not(a)** | List difference of **a** and **b** |
| `#` | **len(a)** or number of base-10 digits in **a** | Each element of **b** repeated by the corresponding element of **a** |
| `k` | Convert bitmask **a** to list of indices | **NI** |
| `K` | Convert list of indices **a** to bitmask | **NI** |
| `r` | Range from 0 to **a-1**, or from **a+1** to 0, separately for each element of **a** | Range from **a** to **b-1**, separately for each element |
| `,` | **flatten(a)** | **concatenate(a, b)** |
| `;` | **[a]** | **[a, b]** |
| `$` | Dimensions of array **a** | **b** reshaped to the shape vector **a** |
| `@` | Index of every atom in **a** | Item of **b** at index **a** |

## Operators

_TODO_