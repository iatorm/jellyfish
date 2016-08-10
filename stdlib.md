# Standard library

## Notation

In this document, the arguments of functions are **a** and **b** (with binary), function arguments of operators are **f** and **g** (with binary), and value arguments of operators are **x** and **y** (with binary).
The first argument is south, the second is east.
Monospace font is reserved for Jellyfish code, and **NI** stands for not implemented.
Lists are compared in lexicographical order, and atoms are strictly lower than lists.

## Functions

Threading levels are for unary **a**, binary **a** and binary **b**.
Level -1 means no threading.

<table>
<tr> <th> Symbol         </th> <th> Threading </th> <th> Unary </th> <th> Binary </th> </tr>
<tr> <td> <code>{</code> </td> <td> -1, -1, -1 </td> <td> <b>a</b> </td> <td> <b>a</b> </td> </tr>
<tr> <td> <code>}</code> </td> <td> -1, -1, -1 </td> <td> <b>a</b> </td> <td> <b>b</b> </td> </tr>
<tr> <td> <code>j</code> </td> <td> -1,  -,  - </td> <td> Read STDIN and eval </td> <td> <b>NI</b> </td> </tr>
<tr> <td> <code>J</code> </td> <td> -1,  -,  - </td> <td> Read STDIN as string </td> <td> <b>NI</b> </td> </tr>
<tr> <td> <code>p</code> </td> <td> -1,  -,  - </td> <td> Print <b>a</b> to STDOUT </td> <td> <b>NI</b> </td> </tr>
<tr> <td> <code>P</code> </td> <td> -1,  -,  - </td> <td> Print <b>a</b> to STDOUT in matrix format </td> <td> <b>NI</b> </td> </tr>
<tr> <td> <code>+</code> </td> <td>  0,  0,  0 </td> <td> <b>abs(a)</b> </td> <td> <b>a + b</b> </td> </tr>
<tr> <td> <code>-</code> </td> <td>  0,  0,  0 </td> <td> <b>-a</b> </td> <td> <b>b - a</b> </td> </tr>
<tr> <td> <code>*</code> </td> <td>  0,  0,  0 </td> <td> <b>sign(a)</b> </td> <td> <b>a * b</b> </td> </tr>
<tr> <td> <code>%</code> </td> <td>  0,  0,  0 </td> <td> <b>1 / a</b> </td> <td> <b>b / a</b> </td> </tr>
<tr> <td> <code>|</code> </td> <td>  0,  0,  0 </td> <td> <b>round(a)</b> </td> <td> <b>b mod a</b> </td> </tr>
<tr> <td> <code>m</code> </td> <td>  0, -1, -1 </td> <td> <b>floor(a)</b> </td> <td> <b>min(a, b)</b> </td> </tr>
<tr> <td> <code>M</code> </td> <td>  0, -1, -1 </td> <td> <b>ceiling(a)</b> </td> <td> <b>max(a, b)</b> </td> </tr>
<tr> <td> <code>x</code> </td> <td> -1,  0,  0 </td> <td> Cartesian product of items of <b>a</b> </td> <td> <b>a xor b</b> </td> </tr>
<tr> <td> <code>b</code> </td> <td>  0,  1,  0 </td> <td> Base-2 digits of <b>a</b> </td> <td> Base-<b>a</b> digits of <b>b</b> </td> </tr>
<tr> <td> <code>d</code> </td> <td>  1,  1,  1 </td> <td> Digits <b>a</b> to base-2 number </td> <td> Digits <b>b</b> to base-<b>a</b> number </td> </tr>
<tr> <td> <code>=</code> </td> <td>  -, -1, -1 </td> <td> <b>NI</b> </td> <td> <b>1</b> if <b>a = b</b>, otherwise <b>0</b> </td> </tr>
<tr> <td> <code>&lt;</code> </td> <td> -1, -1, -1 </td> <td> <ul> <li> Atom: <b>a - 1</b> </li> <li> Array: <b>head(a)</b> </li> </ul> </td> <td> <b>1</b> if <b>a &lt; b</b>, otherwise <b>0</b> </td> </tr>
<tr> <td> <code>&lt;</code> </td> <td> -1, -1, -1 </td> <td> <ul> <li> Atom: <b>a + 1</b> </li> <li> Array: <b>tail(a)</b> </li> </ul> </td> <td> <b>1</b> if <b>a &gt; b</b>, otherwise <b>0</b> </td> </tr>
<tr> <td> <code>!</code> </td> <td> -1,  0, -1 </td> <td> <ul> <li> Atom: <b>a!</b> </li> <li> Array: permutations of <b>a</b> </li> </ul> </td> <td> <ul> <li> Atom <b>b</b>: <b>b! / (b-a)!</b> </li> <li> Array <b>b</b>: length-<b>a</b> permutations of <b>b</b> </li> </ul> </td> </tr>
<tr> <td> <code>c</code> </td> <td>  0, -1, -1 </td> <td> <b>char(a)</b> </td> <td> <b>1</b> if <b>a</b> is a sub-multiset of <b>b</b>, otherwise <b>0</b> </td> </tr>
<tr> <td> <code>!</code> </td> <td> -1,  0, -1 </td> <td> <ul> <li> Atom: <b>2<sup>a</sup></b> </li> <li> Array: subsequences of <b>a</b> </li> </ul> </td> <td> <ul> <li> Atom <b>b</b>: <b>b! / a!*(b-a)!</b> </li> <li> Array <b>b</b>: length-<b>a</b> subsequences of <b>b</b> </li> </ul> </td> </tr>
<tr> <td> <code>n</code> </td> <td>  0, -1, -1 </td> <td> <b>num(a)</b> </td> <td> Intersection of <b>a</b> and <b>b</b> </td> </tr>
<tr> <td> <code>u</code> </td> <td>  0, -1, -1 </td> <td> <b>uniques(a)</b> </td> <td> Union of <b>a</b> and <b>b</b> </td> </tr>
<tr> <td> <code>N</code> </td> <td> -1, -1, -1 </td> <td> <b>0</b> if <b>a</b> is truthy, otherwise <b>1</b> </td> <td> List difference of <b>a</b> and <b>b</b> </td> </tr>
<tr> <td> <code>#</code> </td> <td> -1,  1, -1 </td> <td> <ul> <li> Atom: number of base-10 digits in <b>a</b> </li> <li> Array: length of <b>a</b> </li> </ul> </td> <td> Each item of <b>b</b> repeated by the corresponding item of <b>a</b> </td> </tr>
<tr> <td> <code>k</code> </td> <td>  1,  -,  - </td> <td> <ul> Convert bitmask <b>a</b> to list of indices </td> <td> <b>NI</b> </td> </tr>
<tr> <td> <code>K</code> </td> <td>  1,  -,  - </td> <td> <ul> Convert list of indices <b>a</b> to bitmask </td> <td> <b>NI</b> </td> </tr>
<tr> <td> <code>r</code> </td> <td> -1, -1, -1 </td> <td> Range from <b>0</b> to <b>a-1</b>, or from <b>a+1</b> to <b>0</b>, separately for each item </td> <td> Range from <b>a</b> to <b>b-1</b>, separately for each item </td> </tr>
<tr> <td> <code>,</code> </td> <td> -1, -1, -1 </td> <td> <b>flatten(a)</b> </td> <td> <b>concatenate(a, b)</b> </td> </tr>
<tr> <td> <code>;</code> </td> <td> -1, -1, -1 </td> <td> <b>[a]</b> </td> <td> <b>[a, b]</b> </td> </tr>
<tr> <td> <code>$</code> </td> <td> -1,  1, -1 </td> <td> Dimensions of array <b>a</b> (<b>[]</b> for atom) </td> <td> <b>b</b> reshaped according to the shape vector <b>a</b> </td> </tr>
<tr> <td> <code>@</code> </td> <td> -1,  1, -1 </td> <td> Index of every atom in <b>a</b> </td> <td> Item of <b>b</b> at index <b>a</b> </td> </tr>
</table>

## Operators

_TODO: finish these_

The expressions in the cells represent the results of applying the operators to some function(s) **f, g** and/or value(s) **x, y**, and then applying the resulting function to argument(s) **a, b**.
If one or two arguments makes a difference, they are listed separately in the same cell.
**{IT}** means that in the binary form, the unary form is iterated **a** times on **b**.

<table>
<tr> <th> Symbol         </th> <th> x </th> <th> f </th> <th> x, y </th> <th> f, y </th> <th> x, g </th> <th> f, g </th> </tr>
<tr> <td> <code>_</code> </td>
     <td> <b>NI</b> </td>
     <td> <ul> <li> <b>a</b>: <b>f(a)</b> </li> <li> <b>a, b</b>: <b>f(a, b)</b> </li> </ul> </td>
     <td> <b>NI</b> </td>
     <td> <b>f(y)</b> </td>
     <td> <b>g(x)</b> </td>
     <td> <ul> <li> <b>a</b>: <b>f(a)</b> </li> <li> <b>a, b</b>: <b>f(a, b)</b> </li> </ul> </td>
</tr>
<tr> <td> <code>~</code> </td>
     <td> <b>x</b> </td>
     <td> <ul> <li> <b>a</b>: <b>f(a)</b> </li> <li> <b>a, b</b>: <b>f(b, a)</b> </li> </ul> </td>
     <td> <b>[x, y]</b> </td>
     <td> <b>f(a, y)</b> </td>
     <td> <ul> <li> <b>a</b>: <b>g(x, a)</b> </li> <li> <b>a, b</b>: <b>g(x, b)</b> </li> </ul> </td>
     <td> <ul> <li> <b>a</b>: <b>f(g(a))</b> </li> <li> <b>a, b</b>: <b>f(g(a), g(b))</b> </li> </ul> </td> </tr>
<tr> <td> <code>&</code> </td>
     <td> <b>NI</b> </td>
     <td> <ul> <li> <b>a</b>: <b>f(a, a)</b> </li> <li> <b>a, b</b>: <b>f(b)</b> </li> </ul> </td>
     <td> <b>NI</b> </td>
     <td> <b>f(f(y, a), y) {IT}</b> </td>
     <td> <b>g(x, g(a, x)) {IT}</b> </td>
     <td> <ul> <li> <b>a</b>: <b>f(g(a))</b> </li> <li> <b>a, b</b>: <b>f(g(a, b))</b> </li> </ul> </td> </tr>
</table>