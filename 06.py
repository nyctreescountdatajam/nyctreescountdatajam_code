from _settings import * 

df95 = pd.read_csv(wp+'intersect/nyctrees1995_int_cb2010.csv')
df05 = pd.read_csv(wp+'intersect/nyctrees2005_int_cb2010.csv')
df15 = pd.read_csv(wp+'intersect/nyctrees2015_int_cb2010.csv')



print df95.head(10)
print '-------------------------------'
print df05.head(10)
print '-------------------------------'
print df15.head(10)
print '-------------------------------'
