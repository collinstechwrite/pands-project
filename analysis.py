"""
Author Christopher Collins
"""

#imports required to run analysis.py
import pandas as pd
import seaborn as sns
import numpy as np
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style
from PIL import Image
import matplotlib.image as mpimg 

# Creating the dataframe 
iris = pd.read_csv('IRIS.csv')


#Used for filtering type column
iris_setosa = iris.loc[iris['type'] == 'Setosa']
iris_versicolor = iris.loc[iris['type'] == 'Versicolor']
iris_virginica = iris.loc[iris['type'] == 'Virginica']


#Used for calculating averages
average_of_data = iris.mean(axis = 0,skipna = True)
average_of_Setosa = iris_setosa.mean(axis = 0, skipna = True)
average_of_Versicolor = iris_versicolor.mean(axis = 0, skipna = True)
average_of_Virginica = iris_virginica.mean(axis = 0, skipna = True)


#Used for calculating maximum
maximum_of_data = iris.max(axis = 0, skipna = True)
maximum_of_Setosa = iris_setosa.max(axis = 0, skipna = True)
maximum_of_Versicolor = iris_versicolor.max(axis = 0, skipna = True)
maximum_of_Virginica = iris_virginica.max(axis = 0, skipna = True)


#Used for calculating minimum
minimum_of_data = iris.min(axis = 0, skipna = True)
minimum_of_Setosa = iris_setosa.min(axis = 0, skipna = True)
minimum_of_Versicolor = iris_versicolor.min(axis = 0, skipna = True)
minimum_of_Virginica = iris_virginica.min(axis = 0, skipna = True)


#for handling keyboard reactions and pausing
import keyboard  # using module keyboard
import os

def clear_screen():
    os.system("cls")


# Main function , code was repurposed from lecture menu
def main():
    # Initialise array
    array = []

    display_menu()


    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            clear_screen()
            Introduction_To_Iris_Data_Set()
            display_menu()
        elif (choice == "2"):
            clear_screen()
            View_Image_Of_Iris_Varieties()
            display_menu()
        elif (choice == "3"):
            clear_screen()
            View_Average_Sizes_Iris()
            View_Average_of_Setosa()
            View_Average_of_Versicolor()
            View_Average_of_Virginica()
            display_menu()
        elif (choice == "4"):
            clear_screen()
            View_Minimum_Sizes_Iris()
            View_Minimum_Sizes_Setosa()
            View_Minimum_Sizes_Versicolor()
            View_Minimum_Sizes_Virginica()
            display_menu()
        elif (choice == "5"):
            clear_screen()
            View_Maximum_Sizes_Iris()
            View_Maximum_Sizes_Setosa()
            View_Maximum_Sizes_Versicolor()
            View_Maximum_Sizes_Virginica()
            display_menu()
        elif (choice == "6"):
            clear_screen()
            Save_Summary_Of_Average_Iris_Sizes_To_Text_File()
            display_menu()
        elif (choice == "7"):
            clear_screen()
            View_Data_As_Graph()
            display_menu()
        elif (choice == "8"):
            clear_screen()
            View_Data_As_Scatter_Plot()
            display_menu()
        elif (choice == "9"):
            clear_screen()
            View_Data_As_Histogram()
            display_menu()

        elif (choice == "x"):
            break;
        else:
            display_menu()


def pause_or_quit(): #used for handling scrolling through the program
    print("\n\n")
    os.system("""bash -c 'read -s -n 1 -p "Press any key to continue or q to quit..."'""")
    clear_screen()
 
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print('returning to menu!')
        main()


def Introduction_To_Iris_Data_Set():
    print(Fore.GREEN + """

INTRODUCTION TO THE IRIS DATASET

An understanding of the Iris flower data set, is  the ideal starting place to learn LDA (Linear Discriminant Analysis). Linear Discriminant Analysis was the first statistical method used for Bankruptcy prediction, Face recognition, and widely used in Marketing. These modern day LDA technologies have roots in the work of Sir Ronald Alymer Fisher, a British statistician and geneticist, who is acclaimed for his work in statistics. In 1936 Fisher introduced the Iris flower data set as an example of discriminant analysis. 
The iris data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. Containing only 150 observations of petal length, petal width, sepal width, sepal length the data set is small but not trivial.  The Iris dataset is deservedly widely used throughout statistical science, especially for illustrating various problems in statistical graphics, multivariate statistics and machine learning.
The Iris data set is such a popular data set for teaching computer science and machine learning, so it is inbuilt and accessible in machine learning module libraries used with Python such as scikit learn and R.
""")

    

    pause_or_quit()

    print(Fore.GREEN + """


This python application is used to access the Iris Dataset

This python application creates a text summary of the

Mean sizes
Minimum sizes
Maximum sizes

of the setosa, versicolor and virginica species of Iris.

This python application also imports the pandas, matplotlib, seaborn, sklearn modules to provide graphical plot analysis
in form of scatter plots and histograms.

Comparing the species sepal length, sepal width, petal length, petal width.


""")
    pause_or_quit()


def View_Image_Of_Iris_Varieties():

    print(Fore.GREEN + """This simple line of code can be used to load images

from PIL import Image
image = Image.open('test.png')
image.show()

source: https://stackoverflow.com/questions/35286540/display-an-image-with-python

Press key to see image load.
""")
 

    pause_or_quit() 

    image = Image.open('iris-species.png')
    image.show()


def View_Average_Sizes_Iris():
    print(Fore.GREEN + """
CODE USED TO GET THE AVERAGE SIZE OF ALL IRIS

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
iris = pd.read_csv('IRIS.csv')

# sum over the column axis.
averageofdata = iris.mean(axis = 0, skipna = True)

print("Average Sizes of All Iris Data")
print(averageofdata)


RESULTS OF CODE
""")

   

    # sum over the column axis.
    
    print(Fore.WHITE + "Average Sizes of All Iris Data")
    print(pd.DataFrame(average_of_data))




    pause_or_quit()


def View_Average_of_Setosa():

    print(Fore.GREEN +"""
CODE USED TO GET THE AVERAGE SIZE OF SETOSA

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
iris = pd.read_csv('IRIS.csv')

#Used for filtering type column
iris_setosa = iris.loc[iris['type'] == 'Setosa']

#Used for calculating averages
average_of_Setosa = iris_setosa.mean(axis = 0, skipna = True)

print("Average of Setosa")
print(pd.DataFrame(average_of_Setosa))


RESULTS OF CODE
""")
    
    print(Fore.WHITE +"Average of Setosa")
    print(pd.DataFrame(average_of_Setosa))
    pause_or_quit()
    clear_screen()
         

def View_Average_of_Versicolor():
    print("Average of Versicolor")
    print(pd.DataFrame(average_of_Versicolor))
    pause_or_quit()
    clear_screen()
        

def View_Average_of_Virginica():
    print("Average of Virginica")
    print(pd.DataFrame(average_of_Virginica))
    pause_or_quit()
    clear_screen()       

def View_Minimum_Sizes_Iris():
    print(Fore.GREEN + """
CODE USED TO GET THE MINIMUM SIZE OF ALL IRIS

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
iris = pd.read_csv('IRIS.csv')

# sum over the column axis.
minimum_of_data = iris.min(axis = 0, skipna = True)

print("Minimum Sizes of All Iris Data")
print(minimum_of_data)


RESULTS OF CODE
""")

#https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/   

    # sum over the column axis.




  
    print(Fore.WHITE + "Minium Sizes of All Iris Data")
    print(pd.DataFrame(minimum_of_data))
    pause_or_quit()
    clear_screen()


def View_Minimum_Sizes_Setosa():

    print(Fore.GREEN +"""
CODE USED TO GET THE MINIMUM SIZE OF SETOSA

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
iris = pd.read_csv('IRIS.csv')

#Used for filtering type column
iris_setosa = iris.loc[iris['type'] == 'Setosa']

#Used for calculating averages
minimum_of_Setosa = iris_setosa.min(axis = 0, skipna = True)

print("Minimum of Setosa")
print(pd.DataFrame(minimum_of_Setosa))


RESULTS OF CODE
""")
    
    print(Fore.WHITE +"Minimum of Setosa")
    print(pd.DataFrame(minimum_of_Setosa))
    pause_or_quit()
    clear_screen()
        

def View_Minimum_Sizes_Versicolor():
    print("Minimum of Versicolor")
    print(pd.DataFrame(minimum_of_Versicolor))
    pause_or_quit()
    clear_screen()
        

def View_Minimum_Sizes_Virginica():
    print("Minimum of Virginica")
    print(pd.DataFrame(minimum_of_Virginica))
    pause_or_quit()
    clear_screen()


def View_Maximum_Sizes_Iris():
    print(Fore.GREEN + """
CODE USED TO GET THE MAXIMUM SIZE OF ALL IRIS

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
iris = pd.read_csv('IRIS.csv')

# sum over the column axis.
maximum_of_data = iris.max(axis = 0, skipna = True)

print("Maximum Sizes of All Iris Data")
print(maximum_of_data)


RESULTS OF CODE
""")

   

    # sum over the column axis.
    
    print(Fore.WHITE + "Maximum Sizes of All Iris Data")
    print(pd.DataFrame(maximum_of_data))
    pause_or_quit()
    clear_screen()


def View_Maximum_Sizes_Setosa():

    print(Fore.GREEN +"""
CODE USED TO GET THE MAXIMUM SIZE OF SETOSA

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
iris = pd.read_csv('IRIS.csv')

#Used for filtering type column
iris_setosa = iris.loc[iris['type'] == 'Setosa']

#Used for calculating averages
maximum_of_Setosa = iris_setosa.max(axis = 0, skipna = True)

print("Maximum of Setosa")
print(pd.DataFrame(maximum_of_Setosa))


RESULTS OF CODE
""")

    
    print(Fore.WHITE+"Maximum of Setosa")
    print(pd.DataFrame(maximum_of_Setosa))
    pause_or_quit()
    clear_screen()
        

def View_Maximum_Sizes_Versicolor():
    print("Maximum of Versicolor")
    print(pd.DataFrame(maximum_of_Versicolor))
    pause_or_quit()
    clear_screen()
        

def View_Maximum_Sizes_Virginica():
    print("Maximum of Virginica")
    print(pd.DataFrame(maximum_of_Virginica))
    pause_or_quit()
    clear_screen()
        

def Save_Summary_Of_Average_Iris_Sizes_To_Text_File():
    print("Save Summary Of Average Iris Sizes To Text File")

    myfile = input("Write a file name ending with .txt , this is where average, minimum, maximum data summarys will be saved  ...")
    fileforappending = open(myfile, "w")
    print(myfile + " has been created")
    fileforappending.close()
    print(myfile + " has been created and is ready for appending data.")
    print("You will find your file here: ", os.getcwd(), "\\" , myfile)

    print("Average Of All Iris", file=open(myfile, 'a'))
    print(pd.DataFrame(averageofdata), file=open(myfile, 'a'))
    print("Average Of Setosa", file=open(myfile, 'a'))
    print(pd.DataFrame(average_of_Setosa), file=open(myfile, 'a'))
    print("Average Of Versicolor", file=open(myfile, 'a'))
    print(pd.DataFrame(average_of_Versicolor), file=open(myfile, 'a'))
    print("Average Of Virginica", file=open(myfile, 'a'))    
    print(pd.DataFrame(average_of_Virginica), file=open(myfile, 'a'))




    print("Minimum Of All Iris", file=open(myfile, 'a'))
    print(pd.DataFrame(minimum_of_data), file=open(myfile, 'a'))
    print("Minimum Of Setosa", file=open(myfile, 'a'))
    print(pd.DataFrame(minimum_of_Setosa), file=open(myfile, 'a'))
    print("Minimum Of Versicolor", file=open(myfile, 'a'))
    print(pd.DataFrame(minimum_of_Versicolor), file=open(myfile, 'a'))
    print("Minimum Of Virginica", file=open(myfile, 'a'))
    print(pd.DataFrame(minimum_of_Virginica), file=open(myfile, 'a'))



    print("Maximum Of All Iris", file=open(myfile, 'a'))
    print(pd.DataFrame(maximum_of_data), file=open(myfile, 'a'))
    print("Maximum Of All Setosa", file=open(myfile, 'a'))
    print(pd.DataFrame(maximum_of_Setosa), file=open(myfile, 'a'))
    print("Maximum Of All Versicolor", file=open(myfile, 'a'))
    print(pd.DataFrame(maximum_of_Versicolor), file=open(myfile, 'a'))
    print("Maximum Of All Virginica", file=open(myfile, 'a'))    
    print(pd.DataFrame(maximum_of_Virginica), file=open(myfile, 'a'))


def View_Data_As_Graph():

    print(Fore.GREEN +"""CODE USED TO GET GRAPH PAIRS OF ALL IRIS DATA


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IRIS.csv")
sns.pairplot(df, hue="type")
plt.show()

Source: https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029

PRESS KEY TO CONTINUE TO SEE RESULTS OF CODE
""")

    pause_or_quit()
    
    df = pd.read_csv("IRIS.csv")
    sns.pairplot(df, kind='scatter',hue='type')
    plt.show()
    


def View_Data_As_Scatter_Plot():


    #https://seaborn.pydata.org/generated/seaborn.scatterplot.html
    mydata = pd.read_csv('IRIS.csv')

    #petal_length
    #https://stackoverflow.com/questions/50091591/plotting-seaborn-heatmap-on-top-of-a-background-picture
    map_img = mpimg.imread('Iris_setosa_image_wikimdia_commons.jpg')
    ax = sns.scatterplot(x="petal_length", y="petal_width", hue="type", data=mydata)
    plt.imshow(map_img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
    plt.title("Petal Length & Petal Width Comparison cm")
    plt.show()


    ax = sns.scatterplot(x="petal_length", y="sepal_width", hue="type", data=mydata)
    plt.title("Petal Length & Sepal Width Comparison cm")
    plt.show()


    ax = sns.scatterplot(x="petal_length", y="sepal_length", hue="type", data=mydata)
    plt.title("Petal Length & Sepal Width Comparison cm")
    plt.show()


    #petal_width

    ax = sns.scatterplot(x="petal_width", y="petal_length", hue="type", data=mydata)
    plt.title("Petal Width & Petal Length Comparison cm")
    plt.show()


    ax = sns.scatterplot(x="petal_width", y="sepal_width", hue="type", data=mydata)
    plt.title("Petal Width & Sepal Width Comparison cm")
    plt.show()


    ax = sns.scatterplot(x="petal_width", y="sepal_length", hue="type", data=mydata)
    plt.title("Petal Width & Sepal Length Comparison cm")
    plt.show()


    #sepal_length

    ax = sns.scatterplot(x="sepal_length", y="petal_length", hue="type", data=mydata)
    plt.title("Sepal Length & Petal Length Comparison cm")
    plt.show()


    ax = sns.scatterplot(x="sepal_length", y="petal_width", hue="type", data=mydata)
    plt.title("Sepal Length & Petal Width Comparison cm")
    plt.show()

    #Iris_virginica_sepal_wikimdia_commons.jpg
    #https://stackoverflow.com/questions/50091591/plotting-seaborn-heatmap-on-top-of-a-background-picture
    map_img = mpimg.imread('Iris_virginica_sepal_wikimdia_commons.jpg')
    ax = sns.scatterplot(x="sepal_length", y="sepal_width", hue="type", data=mydata)
    plt.imshow(map_img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
    plt.title("Sepal Length & Sepal Width Comparison cm")
    plt.show()


    #sepal_width

    ax = sns.scatterplot(x="sepal_width", y="petal_length", hue="type", data=mydata)
    plt.title("Sepal Width & Petal Length Comparison cm")
    plt.show()


    ax = sns.scatterplot(x="sepal_width", y="petal_width", hue="type", data=mydata)
    plt.title("Sepal Width & Petal Width Comparison cm")
    plt.show()


    ax = sns.scatterplot(x="sepal_width", y="sepal_length", hue="type", data=mydata)
    plt.title("Sepal Width & Sepal Length Comparison cm")
    plt.show()


    """--------------------------------------------------------------------------"""
    #SAVING THE SCATTER GRAPH FILES

    #petal_length
    #https://stackoverflow.com/questions/50091591/plotting-seaborn-heatmap-on-top-of-a-background-picture
    map_img = mpimg.imread('Iris_setosa_image_wikimdia_commons.jpg')
    ax = sns.scatterplot(x="petal_length", y="petal_width", hue="type", data=mydata)
    plt.imshow(map_img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
    plt.title("Petal Length & Petal Width Comparison cm")
    plt.savefig("Petal Length & Petal Width Comparison.png")
    plt.clf()


    ax = sns.scatterplot(x="petal_length", y="sepal_width", hue="type", data=mydata)
    plt.title("Petal Length & Sepal Width Comparison cm")
    plt.savefig("Petal Length & Sepal Width Comparison.png")
    plt.clf()


    ax = sns.scatterplot(x="petal_length", y="sepal_length", hue="type", data=mydata)
    plt.title("Petal Length & Sepal Width Comparison cm")
    plt.savefig("Petal Length & Sepal Width Comparison.png")
    plt.clf()


    #petal_width

    ax = sns.scatterplot(x="petal_width", y="petal_length", hue="type", data=mydata)
    plt.title("Petal Width & Petal Length Comparison cm")
    plt.savefig("Petal Width & Petal Length Comparison.png")
    plt.clf()


    ax = sns.scatterplot(x="petal_width", y="sepal_width", hue="type", data=mydata)
    plt.title("Petal Width & Sepal Width Comparison cm")
    plt.savefig("Petal Width & Sepal Width Comparison.png")
    plt.clf()


    ax = sns.scatterplot(x="petal_width", y="sepal_length", hue="type", data=mydata)
    plt.title("Petal Width & Sepal Length Comparison cm")
    plt.savefig("Petal Width & Sepal Length Comparison.png")
    plt.clf()


    #sepal_length

    ax = sns.scatterplot(x="sepal_length", y="petal_length", hue="type", data=mydata)
    plt.title("Sepal Length & Petal Length Comparison cm")
    plt.savefig("Sepal Length & Petal Length Comparison.png")
    plt.clf()


    ax = sns.scatterplot(x="sepal_length", y="petal_width", hue="type", data=mydata)
    plt.title("Sepal Length & Petal Width Comparison cm")
    plt.savefig("Sepal Length & Petal Width Comparison.png")
    plt.clf()

    #Iris_virginica_sepal_wikimdia_commons.jpg
    #https://stackoverflow.com/questions/50091591/plotting-seaborn-heatmap-on-top-of-a-background-picture
    map_img = mpimg.imread('Iris_virginica_sepal_wikimdia_commons.jpg')
    ax = sns.scatterplot(x="sepal_length", y="sepal_width", hue="type", data=mydata)
    plt.imshow(map_img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
    plt.title("Sepal Length & Sepal Width Comparison cm")
    plt.savefig("Sepal Length & Sepal Width Comparison.png")
    plt.clf()


    #sepal_width

    ax = sns.scatterplot(x="sepal_width", y="petal_length", hue="type", data=mydata)
    plt.title("Sepal Width & Petal Length Comparison cm")
    plt.savefig("Sepal Width & Petal Length Comparison.png")
    plt.clf()


    ax = sns.scatterplot(x="sepal_width", y="petal_width", hue="type", data=mydata)
    plt.title("Sepal Width & Petal Width Comparison cm")
    plt.savefig("Sepal Width & Petal Width Comparison.png")
    plt.clf()


    ax = sns.scatterplot(x="sepal_width", y="sepal_length", hue="type", data=mydata)
    plt.title("Sepal Width & Sepal Length Comparison cm")
    plt.savefig("Sepal Width & Sepal Length Comparison.png")
    plt.clf()

    
    print(Fore.GREEN +"""CODE NEEDED TO SAVE SCATTER PLOT

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IRIS.csv")

plt.scatter(df['sepal_length'], df['sepal_width'])
plt.title("Sepal length versus sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.savefig("scatter.png")
plt.clf()""")


    pause_or_quit()



    print(Fore.GREEN +"""
CODE NEEDED TO DISPLAY SCATTER PLOT

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IRIS.csv")

plt.scatter(df['sepal_length'], df['sepal_width'])
plt.title("Sepal length versus sepal width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()


""")

    pause_or_quit()

    df = pd.read_csv("IRIS.csv")

    plt.scatter(df['sepal_length'], df['sepal_width'])
    plt.title("Sepal length versus sepal width")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.savefig("scatter.png")
    plt.clf()


    plt.scatter(df['sepal_length'], df['sepal_width'])
    plt.title("Sepal length versus sepal width")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.show()




def View_Data_As_Histogram():

    print(Fore.GREEN +"""
    CODE NEEDED TO DISPLAY HISTOGRAM

    import numpy as np
    import pandas as pd
    from numpy.random import randn
    from scipy import stats
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Creating the dataframe 
    iris = pd.read_csv('IRIS.csv')

    #Used for filtering type column into the separate varieties of flower
    iris_setosa = iris.loc[iris['type'] == 'Setosa']
    iris_versicolor = iris.loc[iris['type'] == 'Versicolor']
    iris_virginica = iris.loc[iris['type'] == 'Virginica']

    #Used for filtering the separate varieties of flower and just referencing one column e.g. sepal length or sepal width
    Setosa_Sepal_Length = iris_setosa.filter(items=['sepal_length'])
    Versicolor_Sepal_Length = iris_versicolor.filter(items=['sepal_length'])
    Virginica_Sepal_Length = iris_virginica.filter(items=['sepal_length'])


    #extracting dataset for histogram
    dataset1 = pd.DataFrame(Setosa_Sepal_Length)
    dataset2 = pd.DataFrame(Versicolor_Sepal_Length)
    dataset3 = pd.DataFrame(Virginica_Sepal_Length)

    #converts the dataframes to arrays to be used in histogram
    dataset1 = dataset1.to_numpy()
    dataset2 = dataset2.to_numpy()
    dataset3 = dataset3.to_numpy()

    plt.hist(dataset1, color='blue', label='Setosa', alpha=0.5,bins=50, )
    plt.hist(dataset2, color='orange', label='Versicolor', alpha=0.5,bins=50)
    plt.hist(dataset3, color='green',label='Virginica', alpha=0.5,bins=50)
    plt.xlabel('Size cm')
    plt.title("Sepal Length Comparison cm")
    plt.show()
""")

    pause_or_quit()

    print(Fore.GREEN +"""
    CODE NEEDED TO SAVE HISTOGRAM

    import numpy as np
    import pandas as pd
    from numpy.random import randn
    from scipy import stats
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Creating the dataframe 
    iris = pd.read_csv('IRIS.csv')

    #Used for filtering type column into the separate varieties of flower
    iris_setosa = iris.loc[iris['type'] == 'Setosa']
    iris_versicolor = iris.loc[iris['type'] == 'Versicolor']
    iris_virginica = iris.loc[iris['type'] == 'Virginica']

    #Used for filtering the separate varieties of flower and just referencing one column e.g. sepal length or sepal width
    Setosa_Sepal_Length = iris_setosa.filter(items=['sepal_length'])
    Versicolor_Sepal_Length = iris_versicolor.filter(items=['sepal_length'])
    Virginica_Sepal_Length = iris_virginica.filter(items=['sepal_length'])


    #extracting dataset for histogram
    dataset1 = pd.DataFrame(Setosa_Sepal_Length)
    dataset2 = pd.DataFrame(Versicolor_Sepal_Length)
    dataset3 = pd.DataFrame(Virginica_Sepal_Length)

    #converts the dataframes to arrays to be used in histogram
    dataset1 = dataset1.to_numpy()
    dataset2 = dataset2.to_numpy()
    dataset3 = dataset3.to_numpy()

    plt.hist(dataset1, color='blue', label='Setosa', alpha=0.5,bins=50, )
    plt.hist(dataset2, color='orange', label='Versicolor', alpha=0.5,bins=50)
    plt.hist(dataset3, color='green',label='Virginica', alpha=0.5,bins=50)
    plt.xlabel('Size cm')
    plt.title("Sepal Length Comparison cm")
    plt.savefig("histogram.png")
    plt.clf()""")

    pause_or_quit()


      

    import numpy as np
    import pandas as pd
    from numpy.random import randn
    from scipy import stats
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Creating the dataframe 
    iris = pd.read_csv('IRIS.csv')

    #Used for filtering type column into the separate varieties of flower
    iris_setosa = iris.loc[iris['type'] == 'Setosa']
    iris_versicolor = iris.loc[iris['type'] == 'Versicolor']
    iris_virginica = iris.loc[iris['type'] == 'Virginica']

    #Used for filtering the separate varieties of flower and just referencing one column e.g. sepal length or sepal width
    Setosa_Sepal_Length = iris_setosa.filter(items=['sepal_length'])
    Versicolor_Sepal_Length = iris_versicolor.filter(items=['sepal_length'])
    Virginica_Sepal_Length = iris_virginica.filter(items=['sepal_length'])


    #extracting dataset for histogram
    dataset1 = pd.DataFrame(Setosa_Sepal_Length)
    dataset2 = pd.DataFrame(Versicolor_Sepal_Length)
    dataset3 = pd.DataFrame(Virginica_Sepal_Length)

    #converts the dataframes to arrays to be used in histogram
    dataset1 = dataset1.to_numpy()
    dataset2 = dataset2.to_numpy()
    dataset3 = dataset3.to_numpy()

    plt.hist(dataset1, color='blue', label='Setosa', alpha=0.5,bins=50, )
    plt.hist(dataset2, color='orange', label='Versicolor', alpha=0.5,bins=50)
    plt.hist(dataset3, color='green',label='Virginica', alpha=0.5,bins=50)
    plt.xlabel('Size cm')
    plt.title("Sepal Length Comparison cm")
    plt.savefig("histogram.png")
    plt.clf()

    

    import numpy as np
    import pandas as pd
    from numpy.random import randn
    from scipy import stats
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Creating the dataframe 
    iris = pd.read_csv('IRIS.csv')

    #Used for filtering type column into the separate varieties of flower
    iris_setosa = iris.loc[iris['type'] == 'Setosa']
    iris_versicolor = iris.loc[iris['type'] == 'Versicolor']
    iris_virginica = iris.loc[iris['type'] == 'Virginica']

    #Used for filtering the separate varieties of flower and just referencing one column e.g. sepal length or sepal width
    Setosa_Sepal_Length = iris_setosa.filter(items=['sepal_length'])
    Versicolor_Sepal_Length = iris_versicolor.filter(items=['sepal_length'])
    Virginica_Sepal_Length = iris_virginica.filter(items=['sepal_length'])


    #extracting dataset for histogram
    dataset1 = pd.DataFrame(Setosa_Sepal_Length)
    dataset2 = pd.DataFrame(Versicolor_Sepal_Length)
    dataset3 = pd.DataFrame(Virginica_Sepal_Length)

    #converts the dataframes to arrays to be used in histogram
    dataset1 = dataset1.to_numpy()
    dataset2 = dataset2.to_numpy()
    dataset3 = dataset3.to_numpy()

    plt.hist(dataset1, color='blue', label='Setosa', alpha=0.5,bins=50, )
    plt.hist(dataset2, color='orange', label='Versicolor', alpha=0.5,bins=50)
    plt.hist(dataset3, color='green',label='Virginica', alpha=0.5,bins=50)
    plt.xlabel('Size cm')
    plt.title("Sepal Length Comparison cm")
    plt.show()




    #Code below is from https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
    #I had to rename size to height in code below, The height parameter is available in seaborn 0.9.0., In seaborn 0.8.1 (or lower) this parameter was named size.
    #https://stackoverflow.com/questions/51400076/change-seaborn-pair-plot-figure-size
    
    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"petal_length").add_legend()
    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"petal_width").add_legend()
    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"sepal_length").add_legend()
    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"sepal_width").add_legend()
    plt.show()



    """
ax = sns.scatterplot(x="total_bill", y="tip", hue="time",
                     data=tips)
    """

def display_menu():
    print(Fore.WHITE +"Iris Data Set")
    print("--------")
    print("MENU")
    print("====")
    print("1 – Introduction To Iris Data Set")
    print("2 - View Image Of Iris Varieties")
    print("3 – View Average Sizes Iris")
    print("4 – View Minimum Sizes Iris")
    print("5 – View Maximum Sizes Iris")
    print("6 – Save Summary Data To Text File")
    print("7 – View Data As Paired Graph Plots")
    print("8 – Save Data As Scatter Plot")
    print("9 – Save Data As Histogram")
    print("x – Exit application")


if __name__ == "__main__":
    # execute only if run as a script
    main()
