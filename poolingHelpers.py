from gameOfLife import evaluate
import random
from geneticOperators import onePointCrossover, mutate, initialisePop
#Helpers for pooling
def fst(xs): return xs[0]
def initialisationHelper(p):
    xDim, yDim, initPopChance = p
    pop = initialisePop(xDim, yDim, initPopChance)
    return (evaluate(pop), pop)
def breedingHelper(parents):
    parents, flipChance, shiftChance = parents
    p1 = random.choice(parents)
    p2 = random.choice(parents)
    #c1, c2 = crossover(p1[1],p2[1])
    c1, c2 = onePointCrossover(p1[1], p2[1])
    c1 = mutate(c1, flipChance, shiftChance)
    c2 = mutate(c2, flipChance, shiftChance)
    return [(evaluate(c1), c1), (evaluate(c2),c2)]

def tournament(p):
    population, tournamentSize = p
    tournement = []
    for i in range(tournamentSize):
        tournement.append(random.choice(population))
    return max(tournement, key=fst)
