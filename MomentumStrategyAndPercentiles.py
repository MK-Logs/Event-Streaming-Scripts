import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from scipy import stats

hqm_columns = [
                'Ticker', 
                'Price', 
                'Number of Shares to Buy', 
                'One-Year Price Return', 
                'One-Year Return Percentile',
                'Six-Month Price Return',
                'Six-Month Return Percentile',
                'Three-Month Price Return',
                'Three-Month Return Percentile',
                'One-Month Price Return',
                'One-Month Return Percentile',
                'HQM Score'
                ]

hqm_dataframe = pd.DataFrame(columns = hqm_columns)

for symbol_string in symbol_strings:
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch/?types=stats,quote&symbols={symbol_string}&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()

for symbol in symbol_string.split(','):
    hqm_dataframe = hqm_dataframe.append(
                                    pd.Series([symbol, 
                                                data[symbol]['quote']['latestPrice'],
                                                'N/A',
                                                data[symbol]['stats']['year1ChangePercent'],
                                                'N/A',
                                                data[symbol]['stats']['month6ChangePercent'],
                                                'N/A',
                                                data[symbol]['stats']['month3ChangePercent'],
                                                'N/A',
                                                data[symbol]['stats']['month1ChangePercent'],
                                                'N/A',
                                                'N/A'
                                                ], 
                                                index = hqm_columns), 
                                    ignore_index = True)
        
hqm_dataframe.columns

time_periods = [
                'One-Year',
                'Six-Month',
                'Three-Month',
                'One-Month'
                ]

for row in hqm_dataframe.index:
    for time_period in time_periods:
        hqm_dataframe.loc[row, f'{time_period} Return Percentile'] = stats.percentileofscore(hqm_dataframe[f'{time_period} Price Return'], hqm_dataframe.loc[row, f'{time_period} Price Return'])/100
 
hqm_dataframe
