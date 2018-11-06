import pandas as pd


df = pd.read_csv("C:/Users/Rosie/Documents/HDip/Year2/survey_results.csv", usecols=['Respondent', 'FormalEducation'],encoding='latin-1', low_memory=False)
#df[df.FormalEducation != 'NA']
#df=df.drop(df[df.FormalEducation=='NA'].index,inplace=True)
# Preview the first 5 lines of the loaded data
#data.head()


#print(df)

df.to_csv('out.csv', sep=',')