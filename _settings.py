import pandas as pd
from nyc_geoclient import Geoclient
import csv
import time
import urllib, urllib2, json
import re

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200
pd.set_option('display.width', 250) #http://stackoverflow.com/questions/11707586/python-pandas-widen-output-display
pd.set_option('display.max_rows', 500) #http://stackoverflow.com/questions/11707586/python-pandas-widen-output-display

#REPLACE TREES dir
wd = '/Users/danielmsheehan/Dropbox/Projects/treescount/data/' 
wi = wd+'input/'
wo = wd+'output/'
wp = wd+'processing/'

def getBoroCode(bName):
	try:
		bName = bName.lower().replace('the','').replace(' ','')
		if bName.isdigit():
			return bName
		elif bName == 'manhattan':
			return '1'
		elif bName == 'newyork':
			return '1'
		elif bName == 'bronx':
			return '2'
		elif bName == 'kings':
			return '3'
		elif bName == 'brooklyn':
			return '3'
		elif bName == 'statenisland':
			return '5'
		elif bName == 'richmond':
			return '5'
		else:
			return '4'
	except:
		return bName
