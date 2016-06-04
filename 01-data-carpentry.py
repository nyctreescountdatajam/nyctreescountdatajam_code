from _settings import * 

df95 = pd.read_csv(wi+'street_tree_census/1995/1995_Street_Tree_Census.csv')
df05 = pd.read_csv(wi+'street_tree_census/2005/NewYorkCity_StreetTreeCensus_2005.csv')
df15 = pd.read_csv(wi+'street_tree_census/2015/TreesCount2015Trees.csv')

print df95.head(10)
print '-------------------------------'
print df05.head(10)
print '-------------------------------'
print df15.head(10)
print '-------------------------------'

df95['uid'] = df95.index 
df05['uid'] = df05.index
df15['uid'] = df15.index

df95.to_csv(wp+'/to_cartodb/nyctrees1995.csv', index=False)
df05.to_csv(wp+'/to_cartodb/nyctrees2005.csv', index=False)
df15.to_csv(wp+'/to_cartodb/nyctrees2015.csv', index=False)

