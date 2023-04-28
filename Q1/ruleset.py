# import pandas as pd
import numpy as np
def check_age(df):
    count=0
    for i in df.Age.values:
        if(i not in range(0,150)):
            count+=1
    return count,"Ruleset 1."

# age should be greater than yearsmarried
def check_agemarried(df):
   count=0
   for i in range(len(df)):
    if(df['Age'][i]<df['yearsmarried'][i]):
        count+=1
    return count,"Ruleset 2."

# the status should be married or single or widowed
def check_status(df):
    count=0
    if(np.unique(df.status.values) != ['married','single','widowed']):
        count+=1
    return count,"Ruleset 3."

# If age is less than 18 the agegroup should be child, if age is between 18 and 65 the agegroup should be
# adult, if age is more than 65 the agegroup should be elderly.

def check_ageGroup(df):
    count=0
    for i in range(len(df)):
        if df['Age'][i]<18 and df['agegroup'][i]!='child':
         count+=1
        elif df['Age'][i]>18 and df['Age'][i] <=65 and df['agegroup'][i]!='adult':
         count+=1
        elif df['Age'][i]>65 and df['agegroup'][i]!='elderly':
         count+=1
        
    return count,"Ruleset 4."
            
            