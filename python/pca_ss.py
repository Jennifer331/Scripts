import pandas as pd
from sklearn.decomposition import PCA

import data_manager as dm

df = dm.import_test_data()
df = df.drop(columns=['RSSI'])
pca = PCA(n_components=3)
pca.fit(df)