# Evolving Conway's Game of Life

This is a fun little project to use genetic algorithms to evolve boards for Conway's Game of Life. I have implemented a tournament selection based genetic algorithm with strict elitism. The reason for the strict elitism is that small changes to the board can make big changes to the results, so I didn't want to risk losing the best population member.

## Genetic Operators
I have implemented one point crossover of the rows in the game board as well as uniform crossover. I find one point crossover works better presumably because in Conway's Game Of Life clusters of points with relation to each other are more important than the position of the points with relation to the board.

As mutators there is a random chance for any off state to turn on and vice versa as well there is a chance for the entire board to shift either one row up or down or one column left or right.

## Execution
Running main.py will execute the evolutionary algorithms using the first few lines of the main.py file. The variables are as follows:
* xDim: width of the board
* yDim: height of the board
* nGenerations: number of generations to run the algorithm for
* nThreads: number of processes to multiprocess over
* popSize: number of individuals in the population
* parentsSize: number of individuals in the population which will survive to the next generation
* flipChance: chance of any one bit flipping during mutation
* shiftChance: chance of shifting row upwards or downwards or shifting columns left or right
* initPopChance: the proportion of board cells which will be filled in when generating the initial population
* tournamentSize: number of individuals in tournament selection

## Visualising results
Currently, the GA is set to write the best individual in each generation to population/GENERATION_NUMBER.txt To make a gif of the board state in this file use visualiser.py, editing the two variables to specify the name of the input file and the name of the output file.

If you have any questions or suggestions, let me know. Hope you enjoy flicking through/playing with this as much as I did when making it.