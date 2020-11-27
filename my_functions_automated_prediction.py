#!/usr/bin/env python
# coding: utf-8

### Create Main Dataframe

import pandas as pd
import os
import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot as plt




### Name/ Sector Label Function

def get_name_sectors(csv, directory, stock_dictionary):

    if f"{csv}".startswith("BATS"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[5:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("BITFINEX"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[9:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("BITMEX"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[7:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("BITSTAMP"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[9:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("EURONEXT"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[13:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("FWB"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[8:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("HKEX"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[9:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("LSE"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[8:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("MIL"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[8:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("OANDA"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[6:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("OMXCOP"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[11:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("OTC"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[8:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("TSE"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[8:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("TVC"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[4:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]

    elif f"{csv}".startswith("XETR"):

        df_stock = pd.read_csv(directory + f"{csv}")
        csv_name = csv
        stock_short = csv_name[9:csv_name.find(",")]
        df_stock = df_stock.tail(1)
        df_stock["name"] = stock_dictionary[stock_short][0]
        df_stock["sector"] = stock_dictionary[stock_short][1]



    return df_stock




### Datetime Function

def get_datetime_format(df):
    df["time"] = pd.to_datetime(df["time"])

    return df




### BullishPB Function

def find_bullishPB(df):

    diffOC = (df["open"] - df["close"])
    diffCO = (df["close"] - df["open"])
    diffCM = (df["close"] - df["low"])
    diffOM = (df["open"] - df["low"])
    diffHC = (df["high"] - df["close"])
    diffOL = (df["open"] - df["low"])
    diffHO = (df["high"] - df["open"])
    diffCL = (df["close"] - df["low"])

    bullishPB = (diffOC <= (diffCM * 0.9)) & (df["close"] < df["open"]) & (diffHO < diffCL) & (diffHO < (diffCL*0.7)) | (diffCO <= (diffOM * 0.9)) & (df["open"] < df["close"]) & (diffHC < diffOL) & (diffHC < (diffOL*0.65))
    bullishPB = pd.DataFrame(bullishPB)
    bullishPB = bullishPB[0].tolist()
    df["bullishPB"] = bullishPB
    df_bullishPB = df[df["bullishPB"] == True]

    return df_bullishPB




### Creating Main DF (Final function)

def create_main_df(directory, stock_dictionary):
    df_list = []
    starters = ("BATS", "BITFINEX", "BITMEX", "BITSTAMP", "EURONEXT", "FWB", "HKEX", "LSE", "MIL", "OANDA", "OMXCOP", "OTC", "TSE", "TVC", "XETR")
    for csv in os.listdir(directory):

        if csv.startswith(starters):

            df_stock = get_name_sectors(csv, directory, stock_dictionary)

            df_stock = get_datetime_format(df_stock)

            df_bullishPB = find_bullishPB(df_stock)

            df_list.append(df_bullishPB)

        else:
            continue

    result = pd.concat(df_list)

    return result





### Feature Engineering

### Removing Missing Values

def remove_missing_values(df):
    df = df.dropna()

    return df




### Creating Relation Features

def creating_relation_features(df):
    df["relation_upper"] = ""
    df["relation_basis"] = ""
    df["relation_lower"] = ""
    df["relation_200MA"] = ""
    for i, row in df.iterrows():

        df.at[i, "relation_upper"] = (df.at[i, "Upper"] - df.at[i, "close"]) / (df.at[i, "Upper"] / 100)
        df.at[i, "relation_basis"] = (df.at[i, "Basis"] - df.at[i, "close"]) / (df.at[i, "Basis"] / 100)
        df.at[i, "relation_lower"] = (df.at[i, "Lower"] - df.at[i, "close"]) / (df.at[i, "Lower"] / 100)
        df.at[i, "relation_200MA"] = (df.at[i, "close"] - df.at[i, "MA"]) / (df.at[i, "close"] / 100)

    return df





### Selecting only relevant features

def relevant_features(df):
    df = df[["Volume", "Volume MA", "MACD", "Signal", "RSI", "relation_upper", "relation_basis", "relation_lower", "relation_200MA"]]
    #df = df[["RSI","MACD", "Signal"]]
    return df






### Final Feature Engineering Functions

def feature_engineering(df):

    #df = remove_missing_values(df)

    df = creating_relation_features(df)

    df = relevant_features(df)

    return df



