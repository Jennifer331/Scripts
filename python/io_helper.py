import os
import pandas as pd


def to_csv(df, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)

    df.to_csv(os.path.join(folder, filename), index=False)
