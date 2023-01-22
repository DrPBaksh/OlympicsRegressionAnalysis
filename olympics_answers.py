import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
sns.set()

class Answers:
    
    def q1_check_answer(answer):
        correct_answer = 21
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q1_get_answer():
        correct_answer = 21
        return correct_answer 

    def q2_check_answer(answer):
        correct_answer = 15
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q2_get_answer():
        correct_answer = 15
        return correct_answer 
            
    def q3_check_answer(answer):
        correct_answer = 97
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q3_get_answer():
        correct_answer = 97
        return correct_answer 
    
    
    def q4_check_answer(answer):
        correct_answer = "Art Competitions"
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again") 

    def q4_get_answer():
        correct_answer = " Art Competitions"
        return correct_answer 
    
    def q5_check_answer(answer):
        correct_answer = 230
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q5_get_answer():
        correct_answer = 230
        return correct_answer 
    
    def q6_check_answer(answer):
        correct_answer = 206
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q6_get_answer():
        correct_answer = 206
        return correct_answer 
    
    def q7_get_answer():
        correct_answer = "Throughout time one geographic region has had different names often depending on political factors"
        return correct_answer 
    
    def q8_check_answer(answer):
        correct_answer = 1385
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q8_get_answer():
        correct_answer = 1385
        return correct_answer 
    
    def q9_check_answer(answer):
        correct_answer = 269731
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q9_get_answer():
        correct_answer = 269731
        return correct_answer 
    
    def q10_check_answer(answer):
        correct_answer = 'NOC'
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q10_get_answer():
        correct_answer = 'NOC'
        return correct_answer 
    
    def q11_check_answer(answer):
        correct_answer = 58814
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q11_get_answer():
        correct_answer = 58814
        return correct_answer 
    
    def q12_check_answer(answer):
        correct_answer = 160
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q12_get_answer():
        correct_answer = 160
        return correct_answer 
    
    def q13_check_answer(answer):
        correct_answer = 4
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q13_get_answer():
        correct_answer = 4
        return correct_answer 
    
    def q14_get_answer(data):
        df = data[data['Season'] == "Winter"].groupby(by  = 'Year').nunique().reset_index() #  reset the index
        plt.plot(df.Year, df.ID, '.-', linewidth = 2, marker = 10)
        plt.xlabel('Year')
        plt.ylabel('No Competitors')

        # Assign the penultimate line of the last dataframe to df
        df = data[data['Season'] == "Summer"].groupby(by  = 'Year').nunique().reset_index() #  reset the index
        plt.plot(df.Year, df.ID, '.-', linewidth = 2, marker = 10)
        plt.xlabel('Year')
        plt.ylabel('No Competitors')
        plt.legend(['Winter', 'Summer'])
        fig = plt.gcf()
        fig.set_size_inches(10, 6)
        plt.show()
        
        return_string = '''      df = data[data['Season'] == "Winter"].groupby(by  = 'Year').nunique().reset_index() #  reset the index
                plt.plot(df.Year, df.ID, '.-', linewidth = 2, marker = 10)
                plt.xlabel('Year')
                plt.ylabel('No Competitors')

                # Assign the penultimate line of the last dataframe to df
                df = data[data['Season'] == "Summer"].groupby(by  = 'Year').nunique().reset_index() #  reset the index
                plt.plot(df.Year, df.ID, '.-', linewidth = 2, marker = 10)
                plt.xlabel('Year')
                plt.ylabel('No Competitors')
                plt.legend(['Winter', 'Summer'])
                fig = plt.gcf()
                fig.set_size_inches(10, 6)'''
        return return_string
    
    def q15_check_answer(answer):
        correct_answer = 835
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q15_get_answer():
        correct_answer = 835
        return correct_answer
    
    def q16_check_answer(data):
        df = data[(data['Season'] == "Summer") & (data['Sex'] == 'M')].groupby(by  = 'Year').nunique().reset_index()[['Year' ,'ID']].rename(columns = {'ID':'participants'}) 
        plt.plot(df.Year, df.participants , color='b',marker='o',label='Male Athletes')

        # create a temporary dataframe for the partipation by year of female athletes ( copy the last line of code from 2 cells above)
        df = data[(data['Season'] == "Summer") & (data['Sex'] == 'F')].groupby(by  = 'Year').nunique().reset_index()[['Year' ,'ID']].rename(columns = {'ID':'participants'}) 
        plt.plot(df.Year, df.participants, color='r',marker='o',label='Female Athletes')

        plt.ylabel("Number of Athletes")
        plt.legend(loc='upper left')
        plt.title("Athletes at the Summer Olympic Games by Sex")
        plt.show()
        
        return_string = ''' df = data[(data['Season'] == "Summer") & (data['Sex'] == 'M')].groupby(by  = 'Year').nunique().reset_index()[['Year' ,'ID']].rename(columns = {'ID':'participants'}) 
plt.plot(df.Year, df.participants , color='b',marker='o',label='Male Athletes')

# create a temporary dataframe for the partipation by year of female athletes ( copy the last line of code from 2 cells above)
df = data[(data['Season'] == "Summer") & (data['Sex'] == 'F')].groupby(by  = 'Year').nunique().reset_index()[['Year' ,'ID']].rename(columns = {'ID':'participants'}) 
plt.plot(df.Year, df.participants, color='r',marker='o',label='Female Athletes')

plt.ylabel("Number of Athletes")
plt.legend(loc='upper left')
plt.title("Athletes at the Summer Olympic Games by Sex") '''
        return return_string
    
    def q17_check_answer(data):
        df = data[data['Season'] == "Summer"].groupby(by = 'Country').nunique().reset_index() \
        [['Year', 'Country']].sort_values('Year', ascending = False).rename(columns ={'Year' : 'Num_Countries'}).head(60)

        fig = plt.figure(figsize = (15, 10))
        plt.bar(df.Country, df.Num_Countries,color=sns.cubehelix_palette(60,start=4,rot=-.005,reverse=True))
        plt.gca().invert_yaxis()
        plt.xticks(rotation=90)
        plt.xlabel('Country')
        plt.ylabel('Number of Editions')
        plt.title('Countries with Most Participation')
        plt.gca().invert_yaxis()


        
        return_string = '''    df = data[data['Season'] == "Summer"].groupby(by = 'Country').nunique().reset_index() \
[['Year', 'Country']].sort_values('Year', ascending = False).rename(columns ={'Year' : 'Num_Countries'}).head(60)

fig = plt.figure(figsize = (15, 10))
plt.bar(df.Country, df.Num_Countries,color=sns.cubehelix_palette(60,start=4,rot=-.005,reverse=True))
plt.gca().invert_yaxis()
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Number of Editions')
plt.title('Countries with Most Participation')
plt.gca().invert_yaxis() '''
        return return_string
    
    

    def q18_check_answer(data):
        df = data[data['Season'] == "Summer"][['Year','Host_Country']].drop_duplicates()  # 
        # use a countplot set y to the Host_country, the data to hosts and the order to hosts['Host_Country'].value_counts().index
        sns.countplot(y='Host_Country',data=df,order = df['Host_Country'].value_counts().index,
                      palette=sns.cubehelix_palette(20,start=5,rot=-.25,reverse=True))
        plt.xlabel('Frequency of hosting')

        
        return_string = '''df = data[data['Season'] == "Summer"][['Year','Host_Country']].drop_duplicates()  # 
# use a countplot set y to the Host_country, the data to hosts and the order to hosts['Host_Country'].value_counts().index
sns.countplot(y='Host_Country',data=df,order = df['Host_Country'].value_counts().index,
              palette=sns.cubehelix_palette(20,start=5,rot=-.25,reverse=True))
plt.xlabel('Frequency of hosting')'''
        return return_string
    
    def q19_check_answer(answer):
        correct_answer = 15
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q19_get_answer():
        correct_answer = 15
        return correct_answer

    def q20_get_answer(answer):
        correct_answer = "Afghanistan"
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")


    def q20_check_answer():
        correct_answer = "Afghanistan"
        return correct_answer
        
    def q21_check_answer(answer):
        correct_answer =203
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q21_get_answer():
        correct_answer = 203
        return correct_answer
    
    def q22_check_answer(answer):
        correct_answer ='USA'
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q22_get_answer():
        correct_answer = 'USA'
        correct_code = """medals_tally = medals.groupby(['Year', 'NOC', 'Country','Sport','Event', 'Medal', 'Sex']).agg('sum').reset_index() \n medals_tally['Medal_Count'] = medals_tally['Medal_Won']/(medals_tally['Team_Event']+medals_tally['Individual_Event']) \n medals_tally.groupby(by = 'Country').sum()[['Medal_Count']].reset_index().sort_values(by = 'Medal_Count', ascending = False)"""
        return correct_answer, correct_code
    
    def q23_check_answer(most_participation):
        top_countries = medals_tally.groupby(by = 'Country').sum()[['Medal_Count']].reset_index().sort_values(by = 'Medal_Count', ascending = False).head(10)
        top_countries.head(10).plot(kind='bar',y='Medal_Count',x='Country',legend=None,figsize=(10,6),color=sns.cubehelix_palette(10,reverse=True))
        plt.xticks(rotation=60)
        plt.xlabel('Country')
        plt.ylabel('Medals')
        plt.title('Medals by Country')

        
        return_string = ''' top_countries = medals_tally.groupby(by = 'Country').sum()[['Medal_Count']].reset_index().sort_values(by = 'Medal_Count', ascending = False).head(10)
top_countries.head(10).plot(kind='bar',y='Medal_Count',x='Country',legend=None,figsize=(10,6),color=sns.cubehelix_palette(10,reverse=True))
plt.xticks(rotation=60)
plt.xlabel('Country')
plt.ylabel('Medals')
plt.title('Medals by Country') '''
        return return_string
  
    def q24_get_answer():
        correct_answer = 198
        return correct_answer
    
    def q24_check_answer(answer):
        correct_answer = 198
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q25_check_answer(answer):
        correct_answer =123
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q25_get_answer():
        correct_answer = 123
        return correct_answer
    
    def q26_get_answer(team_size):
        team_size.plot(kind = 'scatter', x = 'Team_Size', c = 'Team_Size', y = 'Medal_Count', cmap = 'winter', alpha = 0.3)


        
        return_string = '''team_size.plot(kind = 'scatter', x = 'Team_Size', c = 'Team_Size', y = 'Medal_Count', cmap = 'winter', alpha = 0.3) '''
        return return_string
    
        


class OlympicToolKit:
    
    def get_boundingbox_country(country, output_as='center'):
        """
        get the bounding box of a country in EPSG4326 given a country name

        Parameters
        ----------
        country : str
            name of the country in english and lowercase
        output_as : 'str
            chose from 'boundingbox' or 'center'. 
             - 'boundingbox' for [latmin, latmax, lonmin, lonmax]
             - 'center' for [latcenter, loncenter]

        Returns
        -------
        output : list
            list with coordinates as str
        """
        # create url
        url = '{0}{1}{2}'.format('http://nominatim.openstreetmap.org/search?country=',
                                 country,
                                 '&format=json&polygon=0')
        response = requests.get(url).json()[0]

        # parse response to list
        if output_as == 'boundingbox':
            lst = response[output_as]
            output = [float(i) for i in lst]
        if output_as == 'center':
            lst = [response.get(key) for key in ['lat','lon']]
            output = [float(i) for i in lst]
        return output

class RegressionAnswers:
    
    def q1_check_answer(answer):
        correct_answer = 2
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q1_get_answer():
        correct_answer = 2
        return correct_answer 
    
    def q2_check_answer(answer):
        correct_answer = 130
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q2_get_answer():
        correct_answer = 130
        return correct_answer 
    
    def q3_check_answer(answer):
        correct_answer = 5
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q3_get_answer():
        correct_answer = 5
        return correct_answer 
    
    def q4_check_answer(answer):
        correct_answer = 160
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q4_get_answer():
        correct_answer = 160
        return correct_answer 
    
    def q5_check_answer(answer):
        correct_answer = 0.87
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q5_get_answer():
        correct_answer = 0.87
        return correct_answer 
    
    def q6_check_answer(answer):
        correct_answer = 2
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q6_get_answer():
        correct_answer = 2
        return correct_answer 

    def q7_check_answer(answer):
        correct_answer = 4
        if correct_answer == answer:
            print("Correct Well Done")
        else:
            print("Incorrect - Try again")
            
    def q7_get_answer():
        correct_answer = 4
        return correct_answer 
       
    
    
    
    
    
    
            
            
        
        