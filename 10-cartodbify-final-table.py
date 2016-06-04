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
tablename = outTable

sql_statement = """SELECT cdb_cartodbfytable( '"""+tablename+"""');"""
cdbRunSQL(sql_statement)