from gameOfLife import evaluate, Image
#Variables:
popFile = "population/500.txt"
outputFile = "output5.gif"


def readPop(file):
    with open(file, "r") as f:
        lines = f.readlines()
    pop = list(map(lambda y: list(map(lambda x: bool(int(x)),y[:-1])), lines))
    return pop

pop = readPop(popFile)

count, frames = evaluate(pop, visualise= True)
frames[0].save(outputFile, format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)
