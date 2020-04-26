#pands-project
Project 2020

## SUMMARY
## THE IRIS DATASET
## Linear Discriminant Analysis

[![Watch the video](https://github.com/g00387822/pands-project/blob/master/video1.png)](https://youtu.be/tP9lVF4gXQs)

Studying the Iris flower data set, is the ideal starting place to learn LDA (Linear Discriminant Analysis) and to develop data plotting and extraction skills with Python.  This is because the data set is small, it contains 3 classes of 50 instances each, where each class refers to a type of iris plant. Containing only 150 observations of petal length, petal width, sepal width, sepal length the data set is small but not trivial.
Teachers lover the Iris data set because most students can relate to what flowers are, and understand the end result of being able to identity and categorise into different types. Linear Discriminant Analysis is also extensively used by geneticists in determining which genes respond well to drug tests, it is also was the first statistical method used for Bankruptcy prediction, Face recognition, and widely used in Marketing. 
Rather than beginning to learn LDA through doing categorisation of a complex subject matter like genetics which could involve thousands of genes and variable factors, the Iris data set allows the beginner to be able to quickly see the result of LDA successfully with a small amount of data and a few simple commands in Python using some very powerful libraries such as Matplotlib, Pandas, Seaborn, Scikit Learn.
The Iris data set is used by students of computer programming and machine learning with the aim of LDA(Linear Discriminant Analysis),  to improve computer learning processes to be able to classify iris flowers among three species (setosa, versicolor or virginica) from measurements of length and width of sepals and petals.  Once understood this knowledge can then be applied to more advanced fields of computer science.


Iris Flower Types: 
![alt text][logo]

[logo]: https://github.com/g00387822/pands-project/blob/master/iris-species.png "Types Of Iris Flower"



Image source: https://www.slideshare.net/BrittanyLasseigne/an-introduction-to-machine-learning-and-genomics

Modern day LDA technologies have roots in the work of Sir Ronald Alymer Fisher, a British statistician and geneticist, who is acclaimed for his work in statistics. In 1936 Fisher introduced the Iris flower data set as an example of discriminant analysis. 
The Iris dataset is deservedly widely used throughout statistical science, especially for illustrating various problems in statistical graphics, multivariate statistics and machine learning.
The Iris data set is such a popular data set for teaching Linear Discriminant Analysis to students of computer science and machine learning, that the data set is inbuilt and accessible in machine learning module libraries used with Python such as scikit learn and R.
What is Linear Discriminant Analysis? In lay persons terms, it is being able to analyse data in such a way, that ‘When we plot the features, we can see that data is linearly separable. We can draw a line to separate the two groups. The problem is to find the line and to rotate the features in such a way to maximise the distance between the groups and to minimise the distance within the group.’
This is where Python comes extremely useful to visualising the categories of the Iris DataSet Quickly.

## SETTING PYTHON UP TO RUN ANALYSIS.PY
To view screens in action please watch video demo I have provided at https://youtu.be/tP9lVF4gXQs which demonstrates downloading the folder from my github https://github.com/g00387822/pands-project

To be able to run Analysis.py you will need to download the entire folder that contains the Analysis.py file, associated IRIS.csv file, and picture files used in the application.

If you don’t already have python installed you will need to download version 3.7 or later from https://www.python.org/downloads/
While installing Python it is very important to tick the option to add Python to PATH. 


# MENU ITEMS OF ANALYSIS.PY 

# 1 – Introduction To Iris Data Set
•	This section is simple print summary about the Iris Data Set
•	It is followed by a very simple description about the Python application.
# 2 - View Image Of Iris Varieties
•	This section is a simple demonstration that Python can load images
•	It shows the user the code for how this can be done.

e.g. CODE USED TO DISPLAY AN IMAGE WITH PYTHON


```from PIL import Image
image = Image.open('test.png')
image.show()
```

https://stackoverflow.com/questions/35286540/display-an-image-with-python

Python, just like Excel, has the full range of inbuilt aggregate commands. In this Python Application I provide a cursory demonstration of how these aggregate functions when combined with Pandas library are coded to get results straight from the CSV file. These are demonstrated in menu items 3,4,5.

# 3 – View Average Sizes Iris
•	This section is a simple demonstration that the library Pandas is very effective in extracting the Average / Mean of the data.
•	It shows the user the code for how this can be done
•	e.g. CODE USED TO GET THE MINIMUM SIZE OF SETOSA

```import pandas as pd
iris = pd.read_csv('IRIS.csv')
iris_setosa = iris.loc[iris['type'] == 'Setosa']
minimum_of_Setosa = iris_setosa.min(axis = 0, skipna = True)
print("Minimum of Setosa")
print(pd.DataFrame(minimum_of_Setosa))
```


Pandas Dataframe
https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
https://cmdlinetips.com/2019/10/pandas-groupby-13-functions-to-aggregate/
https://www.geeksforgeeks.org/python-pandas-dataframe-mean/

# 4 – View Minimum Sizes Iris
•	This section is a simple demonstration that the library Pandas is very effective in extracting the Minimum of the data.
•	It shows the user the code for how this can be done
•	e.g. CODE USED TO GET THE MINIMUM SIZE OF SETOSA

```import pandas as pd
iris = pd.read_csv('IRIS.csv')
iris_setosa = iris.loc[iris['type'] == 'Setosa']
minimum_of_Setosa = iris_setosa.min(axis = 0, skipna = True)
print("Minimum of Setosa")
print(pd.DataFrame(minimum_of_Setosa))
```

Pandas Dataframe
https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
https://cmdlinetips.com/2019/10/pandas-groupby-13-functions-to-aggregate/
https://www.geeksforgeeks.org/python-pandas-dataframe-mean/

# 5 – View Maximum Sizes Iris
•	This section is a simple demonstration that the library Pandas is very effective in extracting the Maximum of the data.
•	It shows the user the code for how this can be done
•	e.g. CODE USED TO GET THE MAXIMUM SIZE OF ALL IRIS

``` import pandas as pd
iris = pd.read_csv('IRIS.csv')
maximum_of_data = iris.max(axis = 0, skipna = True)
print("Maximum Sizes of All Iris Data")
print(maximum_of_data)
```

Pandas Dataframe
https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
https://cmdlinetips.com/2019/10/pandas-groupby-13-functions-to-aggregate/
https://www.geeksforgeeks.org/python-pandas-dataframe-mean/

-----------------------------------

# 6 – Save Summary Data To Text File

•	This saves the data from the Pandas dataframe summaries of Average, Minimum and Maximum sizes to a text file.

https://stackoverflow.com/questions/5214578/print-string-to-text-file
 -----------------------------------

# 7 – View Paired Graph Plots

•	This demonstrates to the user, the functionality from Seaborne / Matplotlib Paired Plots

# 8 – View Scatter Plots

•	This demonstrates to the user, the functionality from Seaborne / Matplotlib Scatter Plots
 
# 9 – View Histograms

•	This demonstrates to the user, the functionality from Seaborne / Matplotlib Histograms

Seaborn and Matplotlib Plots

•	https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029
•	https://seaborn.pydata.org/generated/seaborn.scatterplot.html
•	https://stackoverflow.com/questions/50091591/plotting-seaborn-heatmap-on-top-of-a-background-picture
•	https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
•	https://stackoverflow.com/questions/51400076/change-seaborn-pair-plot-figure-size
-----------------------------------
# 10 – Save Paired Graph Plots 

•	This saves a Paired Plot graph for the user
•	It also uses the os module to show the user the current working directory of where the file is saved to

https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029
https://seaborn.pydata.org/generated/seaborn.pairplot.html

# 11 – Save Scatter Plots   

•	This saves all variations of scatter plots for the user
•	It also uses the os module to show the user the current working directory of where the files are saved to

# 12 – Save Histograms

•	This saves all variations of histograms for the user
•	It also uses the os module to show the user the current working directory of where the files are saved to

# Saving graph plots

•	https://web.microsoftstream.com/video/737a2b0f-5e2e-4831-a020-5e5d3f8a05e9

 -----------------------------------

# x – Exit application
 

## SETTING PYTHON UP TO RUN ANALYSIS.PY
Located at the top of the source code of most python programs are a list of modules that the application uses.


## imports required to run analysis.py

```import pandas as pd #used for handling data
import numpy as np #used for handling data
import seaborn as sns #used for graphs
import matplotlib as mpl #used for graphs
import matplotlib.pyplot as plt #used for graph plotting
from colorama import init, Fore, Back, Style #used for colourful fonts
from PIL import Image # used for image display
import matplotlib.image as mpimg # used for being able to add background images to graphs
import keyboard  # using module keyboard
import os #for handling keyboard reactions and pausing
```

Before you run Analysis.py PIP INSTALLS may need to get the above modules to work. In the event of errors, check the source code to see which modules need to be installed.
Generally a PIP install has to be done for any module used in the application that isn’t installed on your computer / version of Python. If the Python application isn’t loading when double clicked or run from your python editor, you will need to do PIP installs from the command prompt.
Here are examples of pip installs that you will need to do for any module not found error for this application. Get the name of module from module not found error and pip install it from your command prompt on windows of mac terminal.
e.g. pip install colorama, pip install PIL, pip install pandas, pip install matplotlib, pip install seaborn

If Python has correctly been installed to PATH you should be able to initiate the PIP install command from any directory location.

With PIP installs all done, to activate Analysis.py you should simply be able to double click on the file and Python will run it automatically, alternatively you can run it from Python editor of your choice such as IDLE or Visual Studio Code.

https://en.wikipedia.org/wiki/Iris_flower_data_set
https://en.wikipedia.org/wiki/Linear_discriminant_analysis
