import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


def fake_data():
    x = np.arange(10)
    y = np.empty(shape=[0, 0])
    for i in range(10):
        y = np.append(y, 3*x + 0.5*np.random.rand(len(x)))
    y = np.append(y, 3*x + 10*np.random.rand(len(x)))
    y = np.append(y, 3*x + 10*np.random.rand(len(x)))

    return {'x': np.tile(x, 12), 'y': y}


def clean(data_frame):
    grouped = data_frame.groupby('x')
    x = []
    y = []
    for name, group in grouped:
        x.append(name)
        density = scipy.stats.gaussian_kde(group['y'])
        ind = np.linspace(group['y'].min(), group['y'].max(), 200)
        y.append(ind[np.argsort(density(ind))[-1]])
    d = {'x': x, 'y': y}
    return pd.DataFrame(data=d)


if __name__ == '__main__':
    d = fake_data()
    df = pd.DataFrame(data=d)
    plt.subplot(211)
    plt.scatter(df['x'], df['y'], s=2)

    clean_df = clean(df)
    print(clean_df)
    plt.subplot(212)
    plt.scatter(clean_df['x'], clean_df['y'], s=2)
    plt.show()
