from _settings import * 
from cartodb import CartoDBAPIKey, CartoDBException, FileImport

# gitignored secret info 
from _secret_info import cartodb_domain, API_KEY

cl = CartoDBAPIKey(API_KEY, cartodb_domain)

tr95 = wp+'/to_cartodb/nyctrees1995.csv'
tr05 = wp+'/to_cartodb/nyctrees2005.csv'
tr15 = wp+'/to_cartodb/nyctrees2015.csv'

fi = FileImport(tr95, cl, create_vis='true', privacy='public') # Import csv file, set privacy as 'link' and create a default viz
fi.run() #https://github.com/CartoDB/cartodb-python

fi = FileImport(tr05, cl, create_vis='true', privacy='public') # Import csv file, set privacy as 'link' and create a default viz
fi.run() #https://github.com/CartoDB/cartodb-python

fi = FileImport(tr15, cl, create_vis='true', privacy='public') # Import csv file, set privacy as 'link' and create a default viz
fi.run() #https://github.com/CartoDB/cartodb-python
