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

# CensusTract_2010
 