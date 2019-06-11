from gameOfLife import evaluate, Image
#Variables:
popFile = "population/342.txt"
outputFile = "output4.gif"


def readPop(file):
    with open(file, "r") as f:
        lines = f.readlines()
    pop = list(map(lambda y: list(map(lambda x: bool(int(x)),y[:-1])), lines))
    return pop

pop = readPop("population/7.txt")

count, frames = evaluate(pop, visualise= True)
frames[0].save('output3.gif', format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)
