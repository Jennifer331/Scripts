import matplotlib.pyplot as plt
import pandas as pd

df_unwrap = pd.read_csv('D:\\Atom\\python\\data\\cleaned\\open\\open_oil2_2d_cus_unwrap.csv').groupby('CHANNEL').get_group(902.75)
df_wrap = pd.read_csv('D:\\Atom\\python\\data\\cleaned\\open\\open_oil2_kde.csv').groupby('CHANNEL').get_group(902.75)


plt.scatter(df_wrap['DISTANCE'], df_wrap['PHASE'], s=20)
plt.scatter(df_unwrap['DISTANCE'], df_unwrap['PHASE'])
plt.show()