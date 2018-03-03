import pandas as pd
import numpy as np
import urllib.request


def process_EV(dataframe):
    # Select only EVs
    df_a = dataframe.loc[dataframe['atvType'] == 'EV']

    df = df_a[['year', 'make', 'model', 'drive', 'VClass', 'combE', 'range']]

    df.columns = ['Year', 'Make', 'Model', 'Drive', 'Class', 'Efficiency', 'Range']

    # All this data comes from one place
    df['DataSource'] = "fueleconomy.gov"

    # Convert efficiency from kWh/100mi to mi/kWh.
    df['Efficiency'] = 1 / (df['Efficiency'] / 100)

    df.to_csv("data/EV/government_data.csv.gz", sep=',', compression='gzip')

def process_PHEV(dataframe):

    df_a = dataframe.loc[dataframe['atvType'] == 'Plug-in Hybrid']

    df_a = df_a[['year', 'make', 'model', 'drive', 'VClass', 'CombE', 'rangeA']]

    phev_df = df_a.loc[df_a['phevBlended'] != 'Y']


    df = df_a[['year', 'make', 'model', 'drive', 'VClass', 'combE', 'range']]







def run():

    urllib.request.urlretrieve("https://www.fueleconomy.gov/feg/epadata/vehicles.csv.zip", "data/vehicles.csv.zip")

    df = pd.read_csv("data/vehicles.csv.zip", sep=',', quotechar='"')

    process_EV(df)
