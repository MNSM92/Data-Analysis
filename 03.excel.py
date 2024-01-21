import numpy as np
import matplotlib.pyplot as plt
from tools import P, show_ii, show_nav, show_cav, show_corr
import requests
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook





# create 
x = np.linspace(0, 10, 500)
y = np.cumsum(np.random.randn(500, 6), 0)

plt.figure(figsize=(12, 6))
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.savefig('./plots/excel.png')


def get_historic_price(symbol, after='2018-09-01'):
    
    url = 'https://api.kraken.com/0/public/OHLC'
    pair = f"{symbol.upper()}USD" # XBTUSD when symbol='xbt' for example
    
    resp = requests.get(url, params={
        "pair": pair,
        'interval': 60,
        'since': str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()
    
    data = resp.json()
    
    results_key = [k for k in data['result'].keys() if k != 'last'][0]
    results = [
        (close_time, float(open), float(high), float(low), float(close), float(volume))
        for (close_time, open, high, low, close, vwap, volume, count)
        in data['result'][results_key]
    ]
    df = pd.DataFrame(results, columns=[
        'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df


last_week = (pd.Timestamp.now() - pd.offsets.Day(7))
btc = get_historic_price('btc', after=last_week)
eth = get_historic_price('eth', after=last_week)

writer = pd.ExcelWriter('data/cryptos.xlsx')



btc.to_excel(writer, sheet_name='Bitcoin')
eth.to_excel(writer, sheet_name='Ether')
writer.save()



show_ii(eth)
show_ii(btc)



