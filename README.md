# 3u-menu

Fraction Calculator.
---

Create the below functions according to the specifications, complete with docstrings.

---------

Create a new file in this repo called **fractions_calculator.py**. Within it, create 6 functions: **get_option()**, **get_input()**, **add(a, b, c, d)**, **subtract(a, b, c, d)**, **multiply(a, b, c, d)**, **divide(a, b, c, d)**.

There should be a menu that asks whether the user wants to add two fractions, subtract two fractions, multiply two fractions or divide two fractions. All output that cannot be written as integers will be in the form **a, b** where **a** and **b** represent the numerator an denominator of the resulting fraction in simplified form. To represent a negative fraction - make the numerator negative and the denominator positive. There should also be an option for the user to enter in order to quit the program.

### Input Specification for add

The function takes 4 integers: **a** and **b** represent the numerator and denominator of the first fraction. **c** and **d** represent the numerator an denominator of the second fraction. **b** and **d** will not be zero.

### Output Specification for add

A fraction is the form **x, y** that represents the simplified result of the sum of the two fractions.

**Sample Calls**
```
>>> add(4, 3, -3, 5)
11, 15
>>> add(1, -4, 2, 3)
5, 12
```
---------

### Input Specification for subtract

The function takes 4 integers: **a** and **b** represent the numerator and denominator of the first fraction. **c** and **d** represent the numerator an denominator of the second fraction. **b** and **d** will not be zero.

### Output Specification for subtract

A fraction is the form **x, y** that represents the simplified result of the difference of the two fractions.

**Sample Calls**
```
>>> subtract(4, 3, -3, 5)
29, 15
>>> subtract(1, -4, 2, 3)
-1, 12
```
---------


### Input Specification for multiply

The function takes 4 integers: **a** and **b** represent the numerator and denominator of the first fraction. **c** and **d** represent the numerator an denominator of the second fraction. **b** and **d** will not be zero.

### Output Specification for multiply

A fraction is the form **x, y** that represents the simplified result of the product of the two fractions.

**Sample Calls**
```
>>> multiply(4, 3, -3, 5)
-4, 5
>>> multiply(1, -4, 2, 3)
-1, 6
```

---------

### Input Specification for divide

The function takes 4 integers: **a** and **b** represent the numerator and denominator of the first fraction. **c** and **d** represent the numerator an denominator of the second fraction. **b** and **d** will not be zero.

### Output Specification for divide

A fraction is the form **x, y** that represents the simplified result of the quotient of the two fractions.

**Sample Calls**
```
>>> divide(4, 3, -3, 5)
-20, 9
>>> divide(1, -4, 2, 3)
-3, 8
```

---------
