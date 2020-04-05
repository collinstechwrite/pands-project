#pands-project
Project 2020

## SUMMARY

An understanding of the Iris flower data set, is  the ideal starting place to learn LDA (Linear Discriminant Analysis). Linear Discriminant Analysis was the first statistical method used for Bankruptcy prediction, Face recognition, and widely used in Marketing. These modern day LDA technologies have roots in the work of Sir Ronald Alymer Fisher, a British statistician and geneticist, who is acclaimed for his work in statistics. In 1936 Fisher introduced the Iris flower data set as an example of discriminant analysis. 
The iris data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. Containing only 150 observations of petal length, petal width, sepal width, sepal length the data set is small but not trivial.  The Iris dataset is deservedly widely used throughout statistical science, especially for illustrating various problems in statistical graphics, multivariate statistics and machine learning.
The Iris data set is such a popular data set for teaching computer science and machine learning, so it is inbuilt and accessible in machine learning module libraries used with Python such as scikit learn and R.
A cursory observation of the data set, shows two clusters with rather obvious separation. One of the clusters (illustrated in blue) contains Iris setosa, while the other cluster contains both Iris virginica and Iris versicolor (illustrated in orange and green). Analysis of the second cluster would not be separable without the species information Fisher used.
Only on further analysis where proportions of sepal length, sepal width, petal length and petal width size, does it become easier to classify characteristics of the Iris virginica and Iris versicolor species.

## DEMO

Watch video demo https://youtu.be/tP9lVF4gXQs

For more comprehensive advice on how to use Analysis.py please refer to the README.docx which has screenshots.

To be able to run Analysis.py you will need to download the Analysis.py file and the IRIScsv.csv file from my github https://github.com/g00387822/pands-project

Both the Analysis.py file and the IRIS.csv file will need to be saved in the same directory.
If you don’t already have python installed you will need to download version 3.7 or later from https://www.python.org/downloads/
While installing Python it is very important to tick the option to add Python to PATH. 


## SETTING PYTHON UP TO RUN ANALYSIS.PY
Located at the top of the source code of most python programs are a list of modules that the application uses.

Before you run Analysis.py PIP INSTALLS may need to get the above modules to work. In the event of errors, check the source code to see which modules need to be installed.
Generally a PIP install has to be done for any module used in the application that isn’t installed on your computer / version of Python. If the Python application isn’t loading when double clicked or run from your python editor, you will need to do PIP installs from the command prompt.
Here are examples of pip installs that you will need to do for any module not found error for this application. Get the name of module from module not found error and pip install it from your command prompt on windows of mac terminal.
e.g. pip install colorama, pip install PIL, pip install pandas, pip install matplotlib, pip install seaborn

With PIP installs all done, to activate Analysis.py you should simply be able to double click on the file and Python will run it automatically, alternatively you can run it from Python editor of your choice such as IDLE or Visual Studio Code.
