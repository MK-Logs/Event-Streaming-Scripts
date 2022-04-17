import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from scipy import stats

final_dataframe.sort_values('One-Year Price Return', ascending = False, inplace = True)
final_dataframe = final_dataframe[:51]
final_dataframe.reset_index(drop = True, inplace = True)
final_dataframe

def portfolio_input():
    global portfolio_size
    portfolio_size = input("Enter the value of your portfolio:")

    try:
        val = float(portfolio_size)
    except ValueError:
        portfolio_size = input("Enter the value of your portfolio:")

portfolio_input()

position_size = float(portfolio_size) / len(final_dataframe.index)
for i in range(0, len(final_dataframe['Ticker'])):
    final_dataframe.loc[i, 'Number of Shares to Buy'] = math.floor(position_size / final_dataframe['Price'][i])
final_dataframe
