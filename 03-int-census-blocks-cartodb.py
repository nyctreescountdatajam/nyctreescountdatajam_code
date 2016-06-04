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

for i in treeYears:
	inLayer  = i
	outTable = inLayer+"_int_cb2010"

	sql_statement = "CREATE TABLE "+outTable+" AS SELECT nycb2010wi.bctcb2010, "+inLayer+".uid FROM nycb2010wi, "+inLayer+" WHERE ST_INTERSECTS(nycb2010wi.the_geom,"+inLayer+".the_geom)"
	print sql_statement
	cdbRunSQL(sql_statement)