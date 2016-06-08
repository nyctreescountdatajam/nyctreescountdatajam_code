from _settings import * 
from cartodb import CartoDBAPIKey, CartoDBException, FileImport

# gitignored secret info 
from _secret_info import cartodb_domain, API_KEY

cl = CartoDBAPIKey(API_KEY, cartodb_domain)

def cdbRunSQL(sqlStatement): #https://github.com/CartoDB/cartodb-python
	try:
		print(cl.sql(sqlStatement))
	except CartoDBException as e:
		print("some error ocurred", e)

outTable = 'nycb2010_treesdata'

sql_statement = "CREATE TABLE "+outTable+""" AS SELECT nycb2010.the_geom, nycb2010.bctcb2010, cb2010tree.count1995,
cb2010tree.count2005,
cb2010tree.count2015,
cb2010tree.pctchange9505cnt,
cb2010tree.pctchange0515cnt,
cb2010tree.pctchange9515cnt,
cb2010tree.cbareasqft,
cb2010tree.cbareasqmi,
cb2010tree.treedensqmi1995,
cb2010tree.treedensqmi2005,
cb2010tree.treedensqmi2015,
cb2010tree.pctchange9505den,
cb2010tree.pctchange0515den,
cb2010tree.pctchange9515den
FROM nycb2010, cb2010tree
WHERE nycb2010.bctcb2010 = cb2010tree.bctcb2010"""

print sql_statement
cdbRunSQL(sql_statement)


