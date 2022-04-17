import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from scipy import stats

stocks = pd.read_csv('stocks.csv')
from secrets import IEX_CLOUD_API_TOKEN

symbol = ''
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/stats?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
data['year1ChangePercent']
