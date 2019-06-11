
import math
import io
from multiprocessing import Pool

from poolingHelpers import *

#Variables
xDim = 50
yDim = 50
nGenerations = 10000
nThreads = 16
workers = Pool(nThreads)
popSize = 500
parentsSize = 475
flipChance = 2/(xDim*yDim)
shiftChance = 1/xDim
initPopChance = 0.2
tournamentSize = 6

#Just in case they're needed
def writePop(id, pop):
    with open("population/"+str(id)+".txt","w") as f:
        for row in pop:
            for col in row:
                f.write(str(int(col)))
            f.write("\n")

def readPop(file):
    with open(file, "r") as f:
        lines = f.readlines()
    pop = list(map(lambda y: list(map(lambda x: bool(int(x)),y[:-1])), lines))
    return pop




population = workers.map(initialisationHelper, [(xDim, yDim, initPopChance)]*popSize)
for i in range(nGenerations):
    parents = [max(population, key=fst)]
    print("\rBest score after",i,"generations:", parents[0][0],end='')
    writePop(i, parents[0][1])
    parents += workers.map(tournament, [(population, tournamentSize)]*(parentsSize-1))
    children = workers.map(breedingHelper, [(parents, flipChance, shiftChance)]*(int((popSize-parentsSize)/2)))
    population = parents + sum(children,[])
