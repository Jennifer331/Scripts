import pandas as pd
import matplotlib.pyplot as plt


def import_data():
    epc = "E280 1160 6000 0207 A652 516D"
    filename = "d:\\Atom\\exp\\20210202\\exp_0202_0045cm_d1.csv"
    df = pd.read_csv(filename)
    df_filtered = df.loc[df['EPC'] == epc]
    df_filtered = df_filtered.drop(columns=['A'])
    return df_filtered


def clean(df):
    return df.groupby('CHANNEL').mean()


if __name__ == '__main__':
    data_frame = import_data()
    cleaned = clean(data_frame)
    plt.plot(cleaned['CHANNEL'], )