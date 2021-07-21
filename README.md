# Python-Utility-Tools
A set of utility classes and functions in Python.

## Requirements

- Python>=3.9

## Install

source install:
  - copy put_main.py in your root folder and add _from put_main.py import *_ in .py source file.

pip install:
  - from dist folder: pip install put_main-1.0-py3-none-any.whl and add _from put_main import *_ in .py source file.
  
## Constatns

- **SI_phy_dims**: SI base units are introduced in a tuple as string type. Moles are represented as _Mol_ and not _mol_ to ease strings handling. https://en.wikipedia.org/wiki/SI_base_unit
- **letters**: Lower and upper latin alphabet case letters in a tuple as string type.
- **digits**: decimal system digits (0-9) in a tuple as int type.

## Variable types

Two new variable types are introduced:

- **Numerical**: any int, float or complex is considered a numerical type.

- **Physical**: any list or dictionary with two elements in order, a formatted string and a numerical. Physical variable types strings use the following format convention.
For n numerator dimensions and m denominators dimensions:
  - dim_1dim_2...dim_n/dim_1dim_2...dim_m

  using powers the notation becomes:
  - dim_1^pow_1dim_2^pow_2...dim_n^pow_n/dim_1^pow_1dim_2^pow_2...dim_m^pow_m

  examples:
  - m/s
  - kg/m^2
  - Mol^4kg^3/m^2s

## Identifiers

Identifiers returns True if the argument is the same type of the function
name, false otherwise. Identifiers can identify eventual substructures
with ascending positive integers.

- **is_digit**: check if the argument is a digit.
- **is_number**: check if the argument is numerical.
- **is_letter**: check if the argument is a letter.
- **is_phy_dim**: check if the argument is a SI physical dimension.
- **is_phy**: check if the argument is physical.

## Converters

Converters return an item which is of the same type of 
the calling function name.

- **number**: Convert any argument, when possible, to numerical type or python math library infinity _math.inf_ or
  approximated trascendental _math.pi_, _math.e_, _math.tau_.
  
## Operators

Operators acts on two equal type arguments to return a variable 
of the same type.

- **dim_mult**: Multiply physical dimensions.
- **phy_sum**: Sum physical variables.
- **phy_mult** Multiply physical variables.

## Discretizers

Discretizers returns a finite countable version of an uncountable item.

- **discrete_range** Returns a list which is a representation of finite countable real range. Takes in three arguments: _start_, _end_ and _bins_ (the number of times the interval has to be split into).

## Iterators

Iterators repeat a certain task multiple times.
- **repeat**: Repeat a function a predefined number of times.
- **clock**: An object instanced with fps as argument. Any instance can be called with arguments a function and its
              arguments. It will try to repeat that function on loop 'fps' times each second.
- **run**: Run a multivariable function at fixed fps on same length discrete ranges.

## Contacts

Please report any bug at robiamado@gmail.com
