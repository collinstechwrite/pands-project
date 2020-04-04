"""
Author Christopher Collins
"""

#imports required to run analysis.py
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style
from PIL import Image
import matplotlib.image as mpimg 
#for handling keyboard reactions and pausing
import keyboard  # using module keyboard
import os



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
            View_Paired_Graph_Plots()
            display_menu()
        elif (choice == "8"):
            clear_screen()
            View_Data_As_Scatter_Plot()
            display_menu()
        elif (choice == "9"):
            clear_screen()
            View_Data_As_Histogram()
            display_menu()

        elif (choice == "10"):
            clear_screen()
            Save_Paired_Graph_Plots()
            display_menu()
            
        elif (choice == "11"):
            clear_screen()
            Save_Data_As_Scatter_Plot()
            display_menu()            

        elif (choice == "12"):
            clear_screen()
            Save_Data_As_Histogram()
            display_menu()
        elif (choice == "x"):
            break;
        else:
            display_menu()


def display_menu():
    print(Fore.WHITE +"Iris Data Set")
    print("--------")
    print("MENU")
    print("====")
    print("1 – Introduction To Iris Data Set")
    print("2 - View Image Of Iris Varieties")
    print("-----------------------------------")
    print("3 – View Average Sizes Iris")
    print("4 – View Minimum Sizes Iris")
    print("5 – View Maximum Sizes Iris")
    print("-----------------------------------")
    print("6 – Save Summary Data To Text File")
    print("-----------------------------------")
    print("7 – View Paired Graph Plots")
    print("8 – View Scatter Plots")
    print("9 – View Histograms")
    print("-----------------------------------")
    print("10 – Save Paired Graph Plots")   
    print("11 – Save Scatter Plots")   
    print("12 – Save Histograms")
    print("-----------------------------------")
    print("x – Exit application")


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


def View_Paired_Graph_Plots():

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

def Save_Paired_Graph_Plots():

    print(Fore.GREEN +"""CODE USED TO GET GRAPH PAIRS OF ALL IRIS DATA


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IRIS.csv")
sns.pairplot(df, hue="type")
plt.savefig("Paired Graph Plots.png")
plt.clf()


PRESS KEY TO SAVE
""")

    pause_or_quit()
    
    df = pd.read_csv("IRIS.csv")
    sns.pairplot(df, kind='scatter',hue='type')
    plt.savefig("Paired Graph Plots.png")
    plt.clf()
    print("You will find your file here: ", os.getcwd(), "\\" + "Paired Graph Plots.png")

def generate_scatter_plot(x_axis,y_axis):
    #DISPLAYING THE SCATTER GRAPH FILES
    
    #https://seaborn.pydata.org/generated/seaborn.scatterplot.html
    mydata = pd.read_csv('IRIS.csv')

    #petal_length
    #https://stackoverflow.com/questions/50091591/plotting-seaborn-heatmap-on-top-of-a-background-picture
    map_img = mpimg.imread('Iris_setosa_image_wikimdia_commons.jpg')
    ax = sns.scatterplot(x=x_axis, y=y_axis, hue="type", data=mydata)
    plt.imshow(map_img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
    plt.title(x_axis + " & " + y_axis + " Comparison cm")
    plt.show()    


def save_scatter_plot(x_axis,y_axis):
    #SAVING THE SCATTER GRAPH FILES

    #https://seaborn.pydata.org/generated/seaborn.scatterplot.html
    mydata = pd.read_csv('IRIS.csv')

    #petal_length
    #https://stackoverflow.com/questions/50091591/plotting-seaborn-heatmap-on-top-of-a-background-picture
    map_img = mpimg.imread('Iris_setosa_image_wikimdia_commons.jpg')
    ax = sns.scatterplot(x=x_axis, y=y_axis, hue="type", data=mydata)
    plt.imshow(map_img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
    plt.title(x_axis + " & " + y_axis + " Comparison cm")
    plt.savefig(x_axis + " & " + y_axis + " Comparison.png")
    plt.clf()
    print("You will find your file here: ", os.getcwd()+ "\\" + x_axis + " & " + y_axis + " Comparison.png")

def View_Data_As_Scatter_Plot():

    #petal_length
    generate_scatter_plot("petal_length","petal_width")
    generate_scatter_plot("petal_length","sepal_width")
    generate_scatter_plot("petal_length","sepal_length")

    #petal_width
    generate_scatter_plot("petal_width","petal_length")
    generate_scatter_plot("petal_width","sepal_width")
    generate_scatter_plot("petal_width","sepal_length")

    #sepal_length
    generate_scatter_plot("sepal_length","petal_length")
    generate_scatter_plot("sepal_length","petal_width")
    generate_scatter_plot("sepal_length","petal_width")

    #sepal_width
    generate_scatter_plot("sepal_width","petal_length")
    generate_scatter_plot("sepal_width","petal_width")
    generate_scatter_plot("sepal_width","sepal_length")



def Save_Data_As_Scatter_Plot():
    #petal_length
    save_scatter_plot("petal_length","petal_width")
    save_scatter_plot("petal_length","sepal_width")
    save_scatter_plot("petal_length","sepal_length")

    #petal_width
    save_scatter_plot("petal_width","petal_length")
    save_scatter_plot("petal_width","sepal_width")
    save_scatter_plot("petal_width","sepal_length")

    #sepal_length
    save_scatter_plot("sepal_length","petal_length")
    save_scatter_plot("sepal_length","petal_width")
    save_scatter_plot("sepal_length","petal_width")

    #sepal_width
    save_scatter_plot("sepal_width","petal_length")
    save_scatter_plot("sepal_width","petal_width")
    save_scatter_plot("sepal_width","sepal_length")


def View_Data_As_Histogram():

    pause_or_quit()


    """--------------------------------------------------------------------------------"""

    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Creating the dataframe 
    iris = pd.read_csv('IRIS.csv')

    #Code below is from https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
    #I had to rename size to height in code below, The height parameter is available in seaborn 0.9.0., In seaborn 0.8.1 (or lower) this parameter was named size.
    #https://stackoverflow.com/questions/51400076/change-seaborn-pair-plot-figure-size


    #code used to display graphs
    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"petal_length").add_legend()
    plt.title("Petal Length Comparison cm")
    plt.show()   

    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"petal_width").add_legend()
    plt.title("Petal Width Comparison cm")
    plt.show()

    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"sepal_length").add_legend()
    plt.title("Sepal Length Comparison cm")
    plt.show()
    
    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"sepal_width").add_legend()
    plt.title("Sepal Width Comparison cm")
    plt.show()

    pause_or_quit()




def Save_Data_As_Histogram():
    #code used to save graphs
    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"petal_length").add_legend()
    plt.title("Petal Length Comparison cm")
    plt.savefig("Histogram Petal Length Comparison cm.png")
    plt.clf()  
    print("You will find your file here: "+ os.getcwd()+ "\\" + "Histogram Petal Length Comparison cm.png")


    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"petal_width").add_legend()
    plt.title("Petal Width Comparison cm")
    plt.savefig("Histogram Petal Width Comparison cm.png")
    plt.clf()
    print("You will find your file here: "+ os.getcwd()+ "\\" + "Histogram Petal Width Comparison cm.png")

    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"sepal_length").add_legend()
    plt.title("Sepal Length Comparison cm")
    plt.savefig("Histogram Sepal Length Comparison cm.png")
    plt.clf()
    print("You will find your file here: "+ os.getcwd()+ "\\" + "Histogram Sepal Length Comparison cm.png")

    
    sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"sepal_width").add_legend()
    plt.title("Sepal Width Comparison cm")
    plt.savefig("Histogram Sepal Width Comparison cm.png")
    plt.clf()
    print("You will find your file here: "+ os.getcwd()+ "\\" + "Histogram Sepal Width Comparison cm.png")



if __name__ == "__main__":
    # execute only if run as a script
    main()
