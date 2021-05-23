# ChoateStudentHelp
## python module with 6 functions for Choate students


This module includes 6 distinct functions that I thought would be useful in my life as a student of Choate Rosemary Hall.


## Functions

- Math: infinite_limit, substitution_limit, quadratic_formula, Pascal_triangle, sequences, and series 
- standardizedTest: SAT, ACT
- stocks
- fortune_teller
- walking_time
- visual_design

These are functions that I thought would be helpful in my life.


## Installation

Python 3 is required to download this module.

Install choateStudentHelper via PIP in the command prompt.

```sh
py -m pip install choateStudentHelper
```

For macOS...

```sh
python3 -m pip install choateStudentHelper
```

## Libraries Used

These modules, that do not come pre-installed with Python, are used in various functions of choateStudentHelper.

| module | function |
| ------ | ------ |
| sympy | Math |
| yfinance | stocks |
| stockquotes | stocks |
| matplotlib | stocks |
| geopy | walking_time |
| Pillow | visual_design |


## License

MIT

## Documentation
Here, the functions will be briefly described and the parameters, in terms of their syntax and what they do, will be explained.

Function #1: Math

This class performs 6 distinct math operations that would be helpful to a high school student. 

	Sub-Function #1: infinite_limit

This sub-function evaluates limits to infinity using the rules of the limit equalling 0 when the highest power is in the denominator, infinity or negative infinity when the highest power is in the numerator, and the ratio of the coefficients when the highest powers in the numerator and denominator are equal.

Parameter #1: numerator 
- This is the numerator of the fraction whose limit to infinity is being solved. 
- This is inputted as a string with spaces between all the terms. The variable is x, exponents are written with **, and coefficients are expressed as constants with a * sign and the variable following it. 
- Example: “-1 * x**3 + 3 * x**2 - 4”

Parameter #2: denominator 
- This is the denominator of the fraction whose limit to infinity is being solved. Constants can also be inputted instead of expressions; for example, the denominator can just be “1” for a non-rational expression
- The syntax for this parameter is the same as for the numerator.

<ins>Sub-Function #2: substitution_limit</ins>
	

This sub-function evaluates limits with direct substitution. However, the function will not compute limits that cannot be solved with this method.

Parameter #1: numerator 
- This is the numerator of the fraction whose limit to infinity is being solved. 
- This is inputted as a string with spaces between all the terms. The variable is x, exponents are written with **, and coefficients are expressed as constants with a * sign and the variable following it.  
- Example: “-1 * x**3 + 3 * x**2 - 4”
 
Parameter #2: denominator 
- This is the denominator of the fraction whose limit to infinity is being solved. Constants can also be inputted instead of expressions; for example, the denominator can just be “1” for a non-rational expression
- The syntax for this parameter is the same as for the numerator.

Parameter #3: x_val
- This is the x value to which the limit approaches. It will be substituted in for “x” in the numerator and denominator expressions.
- This parameter is a string for the x value desired, so something like “3” would work.

	Sub-Function #3: quadratic_formula
	
This sub-function finds the roots of a quadratic equation by using the quadratic formula (-b ± √(b2-4ac))/2a. Real and imaginary zeros can be computed.

Parameter #1: a
- This is the coefficient of the squared term in the quadratic equation, such as the 3 in 3x2. 
- This parameter is inputted as an integer.

Parameter #2: b
- This is the coefficient of the term with x to the first power in the quadratic equation. 
- This parameter is inputted as an integer.

Parameter #3: c
- This is the constant term in the quadratic equation.
- This parameter is inputted as an integer.

	Sub-Function #4: Pascal_triangle

This sub-function returns an expanded binomial that is raised to a given power by using the binomial theorem.

Parameter #1: power
- This is the exponent to which the binomial is raised.
- This parameter is given as an integer.

Parameter #2: expression
- This is the binomial that will be expanded via Pascal’s triangle.
- Being a binomial, only two terms are given in the expression: an x term and a constant. They are formatted like the expressions in infinite_limit, with exponents marked by **, spaces between all the terms, and constants written out as multiplication (7 * x). The parameter overall is a string.

	Sub-Function #5: sequences

This sub-function returns the nth term of an arithmetic or geometric sequence by using the formulas t1 + d(n-1) and t1 * rn-1, respectively.

Parameter #1: t1
- This is the first term of the sequence.
- This is given as an integer.

Parameter #2: r
- This is the common difference or ratio of the sequence.
- This is given as an integer.

Parameter #3: n
- This parameter is the number (position) of the term being found.
- This is given as an integer.

Parameter #4: arithmetic 
- This expresses whether or not the sequence is arithmetic, with True meaning it is.
- This parameter is inputted as a boolean, so either True or False.

	Sub-Function #6: series

This sub-function returns the sum of an arithmetic, geometric, or infinite geometric series by using the formulas n(t1 + tn)/2, t1(1-rn)/(1-r), and t1/(1-r), respectively.

Parameter #1: t1
- This is the first term of the series.
- This is given as an integer.

Parameter #2: tn
- This is the nth term of the series.
- This is given as an integer.

Parameter #3: r
- This is the common difference or ratio of the series.
- This is given as an integer.

Parameter #4: n
- This parameter is the number (position) of the term being found.
- This is given as an integer.

Parameter #5: arithmetic 
- This expresses whether or not the series is arithmetic, with True meaning it is.
- This parameter is inputted as a boolean, so either True or False.

Parameter #6: infinite 
- This expresses whether or not the series is infinite (|r| < 1) and only applies for geometric series.
- This parameter is inputted as a boolean, so either True or False.

Function #2: standardizedTest

This class performs simulations to return the average score by guessing every question on either the SAT or the ACT.

	Sub-Function #1: SAT

This sub-function returns the score one would get by guessing every question on the SAT, either by randomizing their answers or choosing the same one every time. 10,000 trials are performed.
Parameter #1: same_answer
This parameter expresses whether or not the same answer is to be chosen for every question in the simulation. True indicates that the same answer will be chosen every time.
This is inputted as a boolean, so either True or False.
Parameter #2: answer
This parameter is the answer that is to be chosen in the case that same_answer is true.
This is inputted as an integer from 1 to 4, representing A, B, C, and D, respectively.

	Sub-Function #2: ACT

This sub-function returns the score one would get by guessing every question on the ACT, either by randomizing their answers or choosing the same one every time. 10,000 trials are performed. The math section of this exam has 5 answer questions, so modifications were made from the SAT function.
Parameter #1: same_answer
This parameter expresses whether or not the same answer is to be chosen for every question in the simulation. True indicates that the same answer will be chosen every time.
This is inputted as a boolean, so either True or False.
Parameter #2: math_answer
This parameter is the answer that is to be chosen for all the math questions in the case that same_answer is true.
This is inputted as an integer from 1 to 5, representing A, B, C, D, and E, respectively. 
Parameter #3: other_answer
This parameter is the answer that is to be chosen on all sections except math in the case that same_answer is true.
This is inputted as an integer from 1 to 4, representing A, B, C, and D, respectively. 

Function #3: stocks

This function returns the current price and displays a graph of the price over a time interval for a given stock.

Parameter #1: ticker
This is the ticker symbol for the stock. 
It is inputted as a string, such as “AMZN”.
Parameter #2: start
This is the start date for the interval over which the stock’s price will be graphed.
This parameter is given as a string of the year, month, and day that are separated by dashes. Zeroes are added for single digit months or days, and no spaces are included.
Example: “2016-04-26”  (April 26th, 2016)
Parameter #3: end
This is the end date for the interval over which the stock’s price will be graphed.
This parameter is given as a string of the year, month, and day that are separated by dashes. Zeroes are added for single digit months or days, and no spaces are included.

Function #4: fortune_teller

This function is a game that is designed to be similar to the paper origami fortune tellers where the user picks several options one after the other. These inputs are given in the command prompt as numbers, either 1 or 2, depending on which option the user desires. However, errors such as giving letters or a number outside of {1, 2} are handled. No parameters are needed for this function.

Function #5: walking_time

This function returns how long it would take to walk, on average, between two buildings on the Choate campus. A fairly comprehensive list of buildings is available, and the result can be a decimal or separated into minutes and seconds.

Parameter #1: building1
This parameter is the first building in the pair used for calculating the walking time. 
This is inputted as a string with the building name typed exactly as it is in the dictionary.
Available buildings: 
Memorial House
Hill House
Squire Stanley
Sally Hart Lodge
Chapel
WJAC
Colony Hall
PMAC
Steele Hall
Lanphier Center
Carl Icahn Science Center
Humanities Building
Andrew Mellon Library
St. John Hall
Tenney/Bernhard
Archbold
CK/McCook
Pratt Health Center
Pierce
Woodhouse/Combination
Logan Munroe
Hunt Tennis Center
Atwater/Mead
Spencer
Parameter #2: building2
This parameter is the second building in the pair used for calculating the walking time. 
This is inputted as a string with the building name typed exactly as it is in the dictionary. 
Parameter #3: seconds
This parameter determines if the output will be given as an integer of minutes with a decimal (2.25) or a string of minutes and seconds (2 minutes and 15 seconds). True will run the second option of a string with minutes and seconds separated.
This is inputted as a boolean, so either True or False.

Function #6: visual_design

This function displays an interesting, randomized visual design using the PIL library. There are 3 options for the image design to be created: a spiraling shape, a glut of circles, or 4 colored sections separated in a unique way.

Parameter #1: vertices
This is the number of vertices of the regular polygon that would be used only for option #1. For example, 4 would create a spiral of squares.
This parameter is given as a whole number larger than 3.
Parameter #2: layers
This parameter is used in different ways for the various options to elaborate the image. In the spiral design, the color is changed every time the iteration is divisible by layers. For option #2, the number of circles drawn equals layers. Option #3 uses layers to determine how many rectangles are drawn; it is the same for the horizontal and vertical directions. The actual number of rectangles is given by 1000/layers. 
This is given as an integer that divides evenly into 1000.
Parameter #3: colors
This is all the possible colors that could be used in the image. Depending on the option, one or many of these colors may be used.
This parameter is inputted as a list of all the colors, which can be represented as RGB tuples or strings like “red”. 
Parameter #4: option
This parameter determines which of the 3 visual designs will be displayed.
This is given as an integer from 1 to 3, representing the 3 options.

