# – Species should be one of the following values: setosa, versicolor or virginica.
import numpy as np
def checkSpecies(data):
  arr1=np.array(data['Species'].value_counts().index)
  count=0
  for i in arr1:
    if i not in ['setosa','versicolor','virginica']:
       count+=1
  return count,'ruleset 1'

# – All measured numerical properties of an iris should be positive.
def check_num(data):
    count=0
    for i in data.columns:
        if data[i].dtypes == "float64":
            if data[data[i]<0].shape[0]>0:
                count=count+1
    return count, "ruleset 2"
# – The petal length of an iris is at least 2 times its petal width.
def checkPetalLength(data):
    count=0
    for i in range(len(data)):
     if(data.loc[i]['Petal.Length']< 2*(data.loc[i]['Petal.Width'])):
      count+=1
    return count,'ruleset 3'

# – The sepal length of an iris cannot exceed 30 cm.
def checkSepalLength(data):
 count=(data['Sepal.Length']>30).sum()
 return count,'ruleset 4'

# – The sepals of an iris are longer than its petals.
def checkSepals(data):
    count=((data['Sepal.Length']+data['Sepal.Width'])<(data['Petal.Length']+data['Petal.Width'])).sum()
    return count,'ruleset 5'
