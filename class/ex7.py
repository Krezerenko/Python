import random
from matplotlib import pyplot as plt

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = (BLACK, WHITE)
RES = 8

seed = random.randint(1, 10000)

def get_pixel(x, y):
    return random.randint(0, 1)

random.seed(seed)
sprite = [[COLORS[get_pixel(x, y)] for x in range(RES // 2)] for y in range(RES)]
random.seed(seed)
for y in range(RES):
    sprite[y] += reversed([COLORS[get_pixel(x, y)] for x in range(RES // 2)])

# plt.imshow(sprite)
plt.rcParams["axes.facecolor"] = "black"
plt.plot()
plt.show()
