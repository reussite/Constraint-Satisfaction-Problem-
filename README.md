# Constraint-Satisfaction-Problem-
## __solving CSP exercises with or-tools in python_

To use the solver or tools to run a csp program, you must first install it.
First check that you have python and the pip module installed.
if so, you can install or-tools with the command line:
```sh
python -m pip install --upgrade --user ortools
```
After the installation is complete, you are ready to get started with OR-Tools for Python.
Above all, do not import the required libraries at the start of your program:
```sh
from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit
```
you can also go to [OR-Tools](https://developers.google.com/optimization/) for more information on this solver
***
here are the 3 examples of constraint satisfaction problem solved using the OR-tools solver. The code is implemented in python

# exercise 1:
A small steel mill (steel manufacturing plant) must decide on the allocation for the
next week (40 hours in total) of his rolling mill (machine used for
reduce the thickness of the materials). This deals with unfinished steel plates and
can produce two kinds of semi-finished products, tapes and rolls. the
rolling mill can produce 200 strips or 140 rolls per hour, knowing that a strip
earns $ 25 and a roll $ 30. Finally, do not produce more than the total
programmed orders, namely 6000 strips and 4000 rolls.
- Determine the respective quantities to be produced to maximize profit.

# exercise 2:
A farmer sends his son to the market with $ 100. With this $ 100, the son must buy a hundred
 animals. He has to come back to the farm with the 100 animals and he has to spend the full $ 100. A chick costs $ 0.50, a pig $ 5, and an ox $ 10. The son must buy at minus one animal of each species. 
 - How many chicks, pigs, and oxen will the son have?

# exercise 3:

We are interested in a vending machine for drinks. The user inserts coins for a total of T fcfa, then he selects a drink, the price of which is P fcfa. It is necessary to calculate the change to be given, knowing that the distributor has in reserve E2 pieces of 200f, E1 pieces of 100f, C50 pieces of 50f, C25 25f coins and C10 10f coins.
- What should be added if we want to minimize the number of parts to be returned.

