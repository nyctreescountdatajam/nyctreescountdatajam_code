import pandas as pd
import numpy  as np
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

treeYears = ['nyctrees1995','nyctrees2005','nyctrees2015']
