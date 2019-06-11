import random
def onePointCrossover(p1, p2):
    row = random.randint(0,len(p1)-1)
    c1 = p1[row:]+p2[:row]
    c2 = p2[row:]+p1[:row]
    return c1, c2

def crossover(p1, p2):
    c1 = []
    c2 = []
    for i in range(len(p1)):
        c1Row = []
        c2Row = []
        for j in range(len(p1[i])):
            if random.random() >0.5:
                c1Row.append(p1[i][j])
                c2Row.append(p2[i][j])
            else:
                c2Row.append(p1[i][j])
                c1Row.append(p2[i][j])
        c1.append(c1Row)
        c2.append(c2Row)
    return c1, c2

def mutate(pop, flipChance, shiftChance):
    newPop = []
    for i, r in enumerate(pop):
        row = []
        for j in r:
            if random.random() < flipChance:
                row.append(not pop[i][j])
            else:
                row.append(pop[i][j])
        newPop.append(row)
    def helper(ls):
        x = ls.pop(0)
        ls.append(x)
        return ls
    def helper2(ls):
        x = ls.pop(-1)
        return [x]+ls
    if random.random() <shiftChance:
        newPop = helper(newPop)
    elif random.random() <shiftChance:
        newPop = helper2(newPop)
    if random.random() <shiftChance:
        newPop = list(map(helper, newPop))
    elif random.random() <shiftChance:
        newPop = list(map(helper2, newPop))
    return newPop

def initialisePop(xDim, yDim, initPopChance):
    pop = []
    for i in range(xDim):
        row = []
        for j in range(yDim):
            row.append(random.random() <initPopChance)
        pop.append(row)
    return pop
