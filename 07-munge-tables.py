from _settings import * 

df95 = pd.read_csv(wp+'intersect/nyctrees1995_int_cb2010.csv')
df05 = pd.read_csv(wp+'intersect/nyctrees2005_int_cb2010.csv')
df15 = pd.read_csv(wp+'intersect/nyctrees2015_int_cb2010.csv')

df95 = df95[['bctcb2010']]
df05 = df05[['bctcb2010']]
df15 = df15[['bctcb2010']]

df95['count1995'] = 1
df05['count2005'] = 1
df15['count2015'] = 1

print df95.head(10)
print '-------------------------------'
print df05.head(10)
print '-------------------------------'
print df15.head(10)
print '-------------------------------'

df95g = df95.groupby('bctcb2010',as_index=False).sum()
df05g = df05.groupby('bctcb2010',as_index=False).sum()
df15g = df15.groupby('bctcb2010',as_index=False).sum()

df = df95g.merge(df05g, on='bctcb2010', how='outer').merge(df15g, on='bctcb2010', how='outer')

df = df.fillna(0)

df['pctchange95_05'] = (df['count2005'] - df['count1995']) / df['count1995']
df['pctchange05_15'] = (df['count2015'] - df['count2005']) / df['count2005']
df['pctchange95_15'] = (df['count2015'] - df['count1995']) / df['count2015']

df = df.replace([np.inf, -np.inf], np.nan)
df = df.fillna(0)

dfcb = pd.read_csv(wi+'/census/nycb2010_11a_av/nycb2010.csv')

dfcb = dfcb.rename(columns=lambda x: x.lower())

dfcb['cbareasqft'] = dfcb['shape_area']
dfcb['cbareasqmi'] = dfcb['cbareasqft'] * 3.58700658032258e-08

dfcb = dfcb[['bctcb2010','cbareasqft','cbareasqmi']]

df = df.merge(dfcb, on='bctcb2010', how='outer')

df['treedensqmi1995'] = df['count1995'] / df['cbareasqmi']
df['treedensqmi2005'] = df['count2005'] / df['cbareasqmi']
df['treedensqmi2015'] = df['count2015'] / df['cbareasqmi']

df['pctchange95_05trdn'] = (df['treedensqmi2005'] - df['treedensqmi1995']) / df['treedensqmi1995']
df['pctchange05_15trdn'] = (df['treedensqmi2015'] - df['treedensqmi2005']) / df['treedensqmi2005']
df['pctchange95_15trdn'] = (df['treedensqmi2015'] - df['treedensqmi1995']) / df['treedensqmi1995']

df['bctcb2010'] = df['bctcb2010'].astype(int)

df = df.replace([np.inf, -np.inf], np.nan)
df = df.fillna(0)

print df.head(20)

print df.dtypes

df.to_csv(wo+'cb2010tree.csv',index=False)