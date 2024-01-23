import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tools import P

df = pd.read_csv(
    'data/btc-eth-prices-outliers.csv',
    index_col=0,
    parse_dates=True
)

P(df.head(), 'green')
df_na = df.loc['2017-12': '2017-12-15']
df.plot(figsize=(16, 9))
df_na[['Bitcoin', 'Ether']].plot(figsize=(16, 9))
plt.savefig('./plots/problem_solve.png')
P(df_na['Ether'].isna().values.any(), 'purple')
P(df_na.loc[df_na['Ether'].isna()], 'purple')

df.fillna(method='bfill', inplace=True)
df.plot(figsize=(16, 9))
plt.savefig('./plots/problem_solve2.png')

df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))

df_cleaned.plot(figsize=(16, 9))
plt.savefig('./plots/problem_solve3.png')

df_cleaned.plot(kind='hist', y='Ether', bins=150)
plt.savefig('./plots/problem_solve4.png')




fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Ether'], ax=ax)
plt.savefig('./plots/problem_solve5.png')

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], rug=True, ax=ax)
plt.savefig('./plots/problem_solve6.png')




fig, ax = plt.subplots(figsize=(15, 7))
sns.kdeplot(df_cleaned['Ether'], shade=True, cut=0, ax=ax)
sns.rugplot(df_cleaned['Ether'], ax=ax)

plt.savefig('./plots/problem_solve7.png')




fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))


plt.savefig('./plots/problem_solve8.png')



fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))


plt.savefig('./plots/problem_solve9.png')



sns.jointplot(x="Bitcoin", y="Ether", data=df_cleaned, size=9)

plt.savefig('./plots/problem_solve10.png')

fig, ax = plt.subplots(figsize=(15, 7))
sns.regplot(x="Bitcoin", y="Ether", data=df_cleaned, ax=ax)

plt.savefig('./plots/problem_solve11.png')




df_cleaned['Bitcoin'].quantile(.2)




fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.2, color='red')
ax.axvline(df_cleaned['Bitcoin'].quantile(.2), color='red')

plt.savefig('./plots/problem_solve12.png')

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(df_cleaned['Bitcoin'].quantile(.5), color='red')

plt.savefig('./plots/problem_solve13.png')



fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(df_cleaned['Bitcoin'].median(), color='red')


plt.savefig('./plots/problem_solve14.png')