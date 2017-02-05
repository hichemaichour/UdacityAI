# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Once a naked-twins are found, additional constrains are added to the other boxes along the unit to which the naked-twins belong. The two possible values for the naked-twins is eliminated from all the other boxes along the same unit causing the board to converge to a solution.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We do that by adding two things. Firstly, two units (one for each diagonal) are added to the list of units. This will add more constraints that should be addressed along each of these two units (Ex: these two units are subjected to only_choice and naked_twins which results the removal of more possibilities per box along the diagonals) Secondly, a box that lies along the diagonal has extra peers which are the boxes the belong to that diagonal. This will add more constraints to those boxes (Ex: once a solution for a box along the diagonal is achieved, that solution is eliminated from all its newly-added peers along the diagonal of Sudoku).

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.