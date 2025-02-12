# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:18:37 2024

@author: IITM
"""

import pandas

#%% Read file
filename = r"D:\Benisha\Skill set\Ecology\Mini Projects\Species_Abundance_Dataset\BioTIMEQuery_24_06_2021.csv"
data = pandas.read_csv(filename)


#%% checking what the dataset contains
print(data.columns)

sampleOfLargeDataset = data.head(1000)


#%% Visualize the data distribution

data.hist() # plots a histogram plot of all the columns with numerical values

#%%

mostRecordedSpeciesID = data['ID_SPECIES'].mode()[0]
print ('Most recorded species: %s (%s count)' % (mostRecordedSpeciesID, len(data[data['ID_SPECIES']==mostRecordedSpeciesID])))

#%% Separate the abundant species

abundantSpeciesData = data[data['ID_SPECIES']==mostRecordedSpeciesID]

abundantSpeciesData.hist()

#%% Separate according to the site latitude and longitude
# They have calculated abundance and biomass using some formula. find it.

grouped = data.groupby(by=['LATITUDE', 'LONGITUDE'])
dfs = [g[1] for g in grouped]