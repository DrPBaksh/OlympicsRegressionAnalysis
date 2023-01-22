import pandas as pd
import numpy as np
df = pd.read_csv('athlete_events.csv') #  load in 'athlete_events.csv' using pandas csv read method. Call this dataframe df
noc = pd.read_csv('noc_regions.csv') #  load in noc_regions.csv using pandas csv read method. Call this dataframe noc
df.drop_duplicates(inplace = True)
noc.drop(columns = ['notes'], inplace = True) #  use the drop method in pandas . rember to use inpace kewyword
data = pd.merge(df,noc,how='left',on='NOC')
data['Medal'].replace(to_replace = np.NaN , value = 'DNW', inplace = True) # use the replace method to replace Null values in medal

data['region'] = np.where(data['NOC']=='SGP', 'Singapore', data['region'])
data['region'] = np.where(data['NOC']=='ROT', 'Refugee Olympic Athletes', data['region'])
data['region'] = np.where(data['NOC']=='TUV', 'Tuvalu', data['region'])
data['region'] = np.where(data['NOC']=='UNK', 'Unknown', data['region'])

data.drop(columns = 'Team', inplace = True) # drop team name

country_dict = {'Athina':'Greece',pyth
                'Paris':'France',
                'St. Louis':'USA',
                'London':'UK',
                'Stockholm':"Sweden",
                'Antwerpen':'Belgium',
                'Amsterdam':'Netherlands',
                'Los Angeles':'USA',
               'Berlin':'Germany',
                'Helsinki':'Finland',
                'Melbourne':'Australia',
                'Roma':'Italy',
                'Tokyo':'Japan',
                'Mexico City':'Mexico',
                'Munich':'Germany',
                'Montreal':'Canada',
                'Moskva':'Russia',
                'Seoul':'South Korea',
               'Barcelona':'Spain',
               'Atlanta':'USA',
               'Sydney':'Australia',
               'Beijing':'China',
               'Rio de Janeiro':'Brazil'}

data['Host_Country']=data['City'].map(country_dict)
data.rename(columns = {'region':'Country'}, inplace = True)
winter = data[data['Season'] == "Winter"] # create dataframe called winter that filters the data by season to winter
summer = data[data['Season'] == "Summer"] # repeat for summer

# summer_frame = summer.groupby(by  = 'Year').nunique()# group the data by year for both winter and summer . call it summer_frame
# winter_frame = winter.groupby(by  = 'Year').nunique()# group the data by year for both winter and summer . call it winter_frame
# summer_frame = summer_frame.reset_index() # reset the index
# winter_frame = winter_frame.reset_index() #  reset the index


# summer_m = summer.loc[summer['Sex']=='M'].groupby('Year')['ID'].nunique()
# summer_f = summer.loc[summer['Sex']=='F'].groupby('Year')['ID'].nunique()

most_participation = summer.groupby(by = 'Country').nunique()  # group summer by country under number of unique values
most_participation.reset_index(inplace=True) # reset the index to make country a column again
most_participation = most_participation[['Year', 'Country']] # select year and country columns
most_participation = most_participation.sort_values('Year', ascending = False).head(60) # sort the data via year ascending true. Limit to top 60

medals = summer[summer['Medal'] != 'DNW'] #  create a new frame that only contains the records where athletes won medals
medals['Medal_Won'] = 1 # create a new column in medals called 'Medal_Won'
team_events = pd.pivot_table(medals,index = ['Country', 'Year', 'Event'], columns = 'Medal', values = 'Medal_Won', aggfunc = 'sum')
team_events.reset_index(inplace  = True) # reset the index of your pivot table
team_events.fillna(0) # use fillna to convert na values to 0

list_team_events = list(team_events[team_events['Gold'] > 1]['Event'].unique()) # create a list of team events. filter by gold greater than 1 then select unique events

medals['Team_Event'] = np.where(medals.Event.map(lambda x: x in list_team_events),1,0)
medals['Individual_Event'] = np.where(medals.Team_Event,0,1)

medals_tally = medals.groupby(['Year', 'NOC', 'Country','Sport','Event', 'Medal', 'Sex']).agg('sum').reset_index()

medals_tally['Medal_Count'] = medals_tally['Medal_Won']/(medals_tally['Team_Event']+medals_tally['Individual_Event'])

medals_tally.groupby(by = 'Country').sum()[['Medal_Count']].reset_index().sort_values(by = 'Medal_Count', ascending = False)