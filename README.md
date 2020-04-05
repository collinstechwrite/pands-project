#pands-project
Project 2020

## SUMMARY
##THE IRIS DATASET
##Linear Discriminant Analysis
Studying the Iris flower data set, is the ideal starting place to learn LDA (Linear Discriminant Analysis) and to develop data plotting and extraction skills with Python.  This is because the data set is small, it contains 3 classes of 50 instances each, where each class refers to a type of iris plant. Containing only 150 observations of petal length, petal width, sepal width, sepal length the data set is small but not trivial.
Teachers lover the Iris data set because most students can relate to what flowers are, and understand the end result of being able to identity and categorise into different types. Linear Discriminant Analysis is also extensively used by geneticists in determining which genes respond well to drug tests, it is also was the first statistical method used for Bankruptcy prediction, Face recognition, and widely used in Marketing. 
Rather than beginning to learn LDA through doing categorisation of a complex subject matter like genetics which could involve thousands of genes and variable factors, the Iris data set allows the beginner to be able to quickly see the result of LDA successfully with a small amount of data and a few simple commands in Python using some very powerful libraries such as Matplotlib, Pandas, Seaborn, Scikit Learn.
The Iris data set is used by students of computer programming and machine learning with the aim of LDA(Linear Discriminant Analysis),  to improve computer learning processes to be able to classify iris flowers among three species (setosa, versicolor or virginica) from measurements of length and width of sepals and petals.  Once understood this knowledge can then be applied to more advanced fields of computer science.

Image source: https://www.slideshare.net/BrittanyLasseigne/an-introduction-to-machine-learning-and-genomics


## SETTING PYTHON UP TO RUN ANALYSIS.PY
To view screens in action please watch video demo I have provided at https://youtu.be/tP9lVF4gXQs which demonstrates downloading the folder from my github https://github.com/g00387822/pands-project

To be able to run Analysis.py you will need to download the entire folder that contains the Analysis.py file, associated IRIS.csv file, and picture files used in the application.

If you don’t already have python installed you will need to download version 3.7 or later from https://www.python.org/downloads/
While installing Python it is very important to tick the option to add Python to PATH. 

##SETTING PYTHON UP TO RUN ANALYSIS.PY
Located at the top of the source code of most python programs are a list of modules that the application uses.

#imports required to run analysis.py
import pandas as pd #used for handling data
import numpy as np #used for handling data
import seaborn as sns #used for graphs
import matplotlib as mpl #used for graphs
import matplotlib.pyplot as plt #used for graph plotting
from colorama import init, Fore, Back, Style #used for colourful fonts
from PIL import Image # used for image display
import matplotlib.image as mpimg # used for being able to add background images to graphs
import keyboard  # using module keyboard
import os #for handling keyboard reactions and pausing

Before you run Analysis.py PIP INSTALLS may need to get the above modules to work. In the event of errors, check the source code to see which modules need to be installed.
Generally a PIP install has to be done for any module used in the application that isn’t installed on your computer / version of Python. If the Python application isn’t loading when double clicked or run from your python editor, you will need to do PIP installs from the command prompt.
Here are examples of pip installs that you will need to do for any module not found error for this application. Get the name of module from module not found error and pip install it from your command prompt on windows of mac terminal.
e.g. pip install colorama, pip install PIL, pip install pandas, pip install matplotlib, pip install seaborn

If Python has correctly been installed to PATH you should be able to initiate the PIP install command from any directory location.

With PIP installs all done, to activate Analysis.py you should simply be able to double click on the file and Python will run it automatically, alternatively you can run it from Python editor of your choice such as IDLE or Visual Studio Code.

https://en.wikipedia.org/wiki/Iris_flower_data_set
https://en.wikipedia.org/wiki/Linear_discriminant_analysis
