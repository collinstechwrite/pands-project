"""
1. Research the data set online and write a summary about it in your README.
2. Download the data set and add it to your repository.
3. Write a program called analysis.py that: • outputs a summary of each variable to a single text ﬁle,
• saves a histogram of each variable to png ﬁles, and • outputs a scatter plot of each pair of variables.
"""

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
IrisData = pd.read_csv('IRIScsv.csv')

print(IrisData)

# sum over the column axis.
averageofdata = IrisData.mean(axis = 0, skipna = True)
print(averageofdata)


Iris_setosa = IrisData.loc[IrisData['variety'] == 'Setosa']
Iris_versicolor = IrisData.loc[IrisData['variety'] == 'Versicolor']
Iris_virginica = IrisData.loc[IrisData['variety'] == 'Virginica']



print("Average of Setosa")
average_of_Setosa = Iris_setosa.mean(axis = 0, skipna = True)
print(average_of_Setosa)


print("Average of Versicolor")
average_of_Versicolor = Iris_versicolor.mean(axis = 0, skipna = True)
print(average_of_Versicolor)

print("Average of Virginica")
average_of_Virginica = Iris_virginica.mean(axis = 0, skipna = True)
print(average_of_Virginica)



print(Iris_setosa)





"""
species
Iris-setosa
Iris-versicolor
Iris-virginica


sepal_length
sepal_width
petal_length
petal_width
"""
