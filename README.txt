This code has functions for converting arabic numbers to roman notation and vice versa.
For numbers greater than 3999, it uses a notation with parenthesis, where at the start of the roman number a parenthesis is open
for every potency of 1000 appart from the first and a parenthesisis closed after every potency of 1000. For example 900900900 would be "((CM)CM)CM".
it accepts romans in that notation, the opening parenthesis can be omitted and any extras where they dont belong will give an error.
currentAndNext for a given roman number and position returns an array containing the symbol in that position and the next. IV, IX, XL, XC, CD and CM are always considered as a single symbol.
validate roman accepts the empty string, and it will be treated as 0.
