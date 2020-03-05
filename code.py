# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)

data=data.rename(columns={'Total':'Total_Medals'})
print(data.head(10))
#Code starts here



# --------------
#Code starts h
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both', data['Better_Event'])
#print(data['Total_Winter'].describe())
better_event=np.argmax(data['Better_Event'].value_counts())
better_event


# --------------
#Code starts here
top_countries=pd.DataFrame(data,columns=['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'])

top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(top_countries,columns):
    country_list=[]
    top=top_countries.nlargest(10,columns)
    country_list=list(top['Country_Name'])
    return country_list
top_10_summer=top_ten(top_countries, 'Total_Summer')
top_10_winter=top_ten(top_countries, 'Total_Winter')
top_10=top_ten(top_countries, 'Total_Medals')

common=[x for x in top_10_summer if x in top_10_winter and x in top_10 ]
common



# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

summer_df.plot(x='Country_Name',y='Total_Summer',kind='bar')
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_max_ratio]
summer_country_gold=list(summer_country_gold['Country_Name'])[0]


winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df[winter_df['Golden_Ratio']==winter_max_ratio]
winter_country_gold=list(winter_country_gold['Country_Name'])[0]

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df[top_df['Golden_Ratio']==top_max_ratio]
top_country_gold=list(top_country_gold['Country_Name'])[0]
top_country_gold


# --------------
#Code starts here
data.drop(data.tail(1).index, inplace=True)
data_1=data.copy()

data_1['Total_Points']=((data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']))
most_points=data_1['Total_Points'].max()
best_country=data_1[data_1['Total_Points']==most_points]
best_country=list(best_country['Country_Name'])[0]
best_country



# --------------
#Code starts here

best=data[data.Country_Name==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


