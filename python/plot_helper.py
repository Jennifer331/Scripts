import matplotlib.pyplot as plt


def plot_dict(d, ax):
    lists = sorted(d.items())
    x, y = zip(*lists)
    ax.plot(x, y)
