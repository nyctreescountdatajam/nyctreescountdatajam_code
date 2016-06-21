## 00 

Welcome to my project on the NYC Street Tree Census   Data Jam Challenge

Here is a quick overview of the websit I created using some basic data analysis, the CartoDB platform, to create a mapping portal dropdowns for different thematic maps, and data download. 

All my code is on GitHub on how to create such a site and perform the analysis I did for the Data Jam. 

# 01

NYC Parks, Beta NYC, NYC Mayors Office of Tech + Innovation, NYC Open Data, Civic Hall, Microsoft and CartoDB sponsored the all-day Data Jam event on Sat. Jun. 4th.  

## 02 

I looked at Challenge number 1

1. How has NYC’s urban forest changed over time — comparing 1995, 2005, and 2015?

## 03

The 1995, 2005 and 2015 Street Tree Census data can be downloaded from the NYC OpenData portal

## 04

I scripted my p[roejct in python 

My _settings.py file has a bunch of the dependencies and directory settings for my code. 

I read and saved my data in pandas to explore the variables.

Then I imported the CSV files into CartoDB using the import API. 

Then I intersected the Street trees for each census with NYC Census Blocks 2010. Again, using the CartoDB python client. 

Then CartoDBifyied the tables and used the CartoDB SQL API to read the output right into a pandas dataframe. 

Next, I just quickly grabbed the NYC census block data clipped to shoreline to get shape area in square feet, for NYC's local state plane long island projection system, using dbfpy python module to convert the dbf to a csv adn then did soem data carpentry in pandas to join the data on the census block id, create some percent change metrics and street tree density per sq mile.

Next I imported a master table into cartodb using the import api again. 

THen I merged those fields to the NYC Census Block 2010 clipped to shoreline geometries using SQL. And cartodbified to use that table for mapping. 

## 05

Next I created some Maps in the CartoDB platform, using the Wizard, some CartoCSS and then set the info window to view all the street tree census variables across the census years. when a census block is clicked

## 06

I created several CartoDB maps, saving each of them by copying the Publish viz's json URL. 

## 07 

I pased those JSON .VIZ URL's into a Python script, along with some other information to generatl html and javascript files using python. 

I loop through lists and some html to generate the dropdown menu, the export buttons and a variety of other map elements. 


Please note, for this task, I probably should be using Jinja or some other python tool. 

I write these to a github jekyll template, I quickly created using jekyll ruby. 

# 08 




 

