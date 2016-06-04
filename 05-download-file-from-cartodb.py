from _settings import * 
from cartodb import CartoDBAPIKey, CartoDBException, FileImport

# gitignored secret info 
from _secret_info import cartodb_domain, API_KEY

for i in treeYears:
	inLayer  = i
	outTable = inLayer+"_int_cb2010"
	tablename = outTable
	print tablename

	url = "http://"+cartodb_domain+".cartodb.com/api/v2/sql?q=SELECT%20*%20FROM%20"+tablename+"&format=csv&api_key="+API_KEY
	df = pd.read_csv(url)

	df.to_csv(wp+'intersect/'+tablename+".csv", index=False)