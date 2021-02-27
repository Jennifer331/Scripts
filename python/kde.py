import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np


def make_data(N, f=0.3, rseed=1):
    rand = np.random.RandomState(rseed)
    x = rand.randn(N)
    x[int(f * N):] += 5
    return x


x = make_data(1000)
##
hist = plt.hist(x, bins=30, density=True)
density, bins, patches = hist
widths = bins[1:] - bins[:-1]
(density * widths).sum()
plt.show()
