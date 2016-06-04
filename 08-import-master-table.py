from _settings import * 
from cartodb import CartoDBAPIKey, CartoDBException, FileImport

# gitignored secret info 
from _secret_info import cartodb_domain, API_KEY

cl = CartoDBAPIKey(API_KEY, cartodb_domain)

inFile = wo+'/cb2010tree.csv'

fi = FileImport(inFile, cl, create_vis='true', privacy='public') # Import csv file, set privacy as 'link' and create a default viz
fi.run() #https://github.com/CartoDB/cartodb-python

