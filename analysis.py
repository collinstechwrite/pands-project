"""
Author Christopher Collins
"""


from colorama import init, Fore, Back, Style

from PIL import Image


from sklearn import datasets

# importing pandas as pd 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the dataframe 
IrisData = pd.read_csv('IRIScsv.csv')


averageofdata = IrisData.mean(axis = 0, skipna = True)




Iris_setosa = IrisData.loc[IrisData['variety'] == 'Setosa']
Iris_versicolor = IrisData.loc[IrisData['variety'] == 'Versicolor']
Iris_virginica = IrisData.loc[IrisData['variety'] == 'Virginica']


#Used for calculating averages
averageofdata = IrisData.mean(axis = 0,skipna = True)
average_of_Setosa = Iris_setosa.mean(axis = 0, skipna = True)
average_of_Versicolor = Iris_versicolor.mean(axis = 0, skipna = True)
average_of_Virginica = Iris_virginica.mean(axis = 0, skipna = True)


#Used for calculating maximum
maximum_of_data = IrisData.max(axis = 0, skipna = True)
maximum_of_Setosa = Iris_setosa.max(axis = 0, skipna = True)
maximum_of_Versicolor = Iris_versicolor.max(axis = 0, skipna = True)
maximum_of_Virginica = Iris_virginica.max(axis = 0, skipna = True)


#Used for calculating minimum
minimum_of_data = IrisData.min(axis = 0, skipna = True)
minimum_of_Setosa = Iris_setosa.min(axis = 0, skipna = True)
minimum_of_Versicolor = Iris_versicolor.min(axis = 0, skipna = True)
minimum_of_Virginica = Iris_virginica.min(axis = 0, skipna = True)






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
    print("""
This python application is used to access the Iris Dataset

'The aim is to classify iris flowers among three species (setosa, versicolor or virginica) from measurements of length and width of sepals and petals.
The iris data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.'
https://www.neuraldesigner.com/learning/examples/iris-flowers-classification


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
IrisData = pd.read_csv('IRIScsv.csv')

# sum over the column axis.
averageofdata = IrisData.mean(axis = 0, skipna = True)

print("Average Sizes of All Iris Data")
print(averageofdata)


RESULTS OF CODE
""")

   

    # sum over the column axis.
    
    print(Fore.WHITE + "Average Sizes of All Iris Data")
    print(pd.DataFrame(averageofdata))




    pause_or_quit()


def View_Average_of_Setosa():
    print("Average of Setosa")
    print(pd.DataFrame(average_of_Setosa))
    pause_or_quit()
        

def View_Average_of_Versicolor():
    print("Average of Versicolor")
    print(pd.DataFrame(average_of_Versicolor))
    pause_or_quit()
        

def View_Average_of_Virginica():
    print("Average of Virginica")
    print(pd.DataFrame(average_of_Virginica))
    pause_or_quit()
        

def View_Minimum_Sizes_Iris():
    print(Fore.GREEN + """
CODE USED TO GET THE MINIMUM SIZE OF ALL IRIS

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
IrisData = pd.read_csv('IRIScsv.csv')

# sum over the column axis.
minimum_of_data = IrisData.min(axis = 0, skipna = True)

print("Minimum Sizes of All Iris Data")
print(minimum_of_data)


RESULTS OF CODE
""")

   

    # sum over the column axis.
    
    print(Fore.WHITE + "Minium Sizes of All Iris Data")
    print(pd.DataFrame(minimum_of_data))
    pause_or_quit()


def View_Minimum_Sizes_Setosa():
    print("Minimum of Setosa")
    print(pd.DataFrame(minimum_of_Setosa))
    pause_or_quit()
        

def View_Minimum_Sizes_Versicolor():
    print("Minimum of Versicolor")
    print(pd.DataFrame(minimum_of_Versicolor))
    pause_or_quit()
        

def View_Minimum_Sizes_Virginica():
    print("Minimum of Virginica")
    print(pd.DataFrame(minimum_of_Virginica))
    pause_or_quit()


def View_Maximum_Sizes_Iris():
    print(Fore.GREEN + """
CODE USED TO GET THE MAXIMUM SIZE OF ALL IRIS

# importing pandas as pd 
import pandas as pd

# Creating the dataframe 
IrisData = pd.read_csv('IRIScsv.csv')

# sum over the column axis.
maximum_of_data = IrisData.max(axis = 0, skipna = True)

print("Maximum Sizes of All Iris Data")
print(maximum_of_data)


RESULTS OF CODE
""")

   

    # sum over the column axis.
    
    print(Fore.WHITE + "Maximum Sizes of All Iris Data")
    print(pd.DataFrame(maximum_of_data))
    pause_or_quit()


def View_Maximum_Sizes_Setosa():
    print("Maximum of Setosa")
    print(pd.DataFrame(maximum_of_Setosa))
    pause_or_quit()
        

def View_Maximum_Sizes_Versicolor():
    print("Maximum of Versicolor")
    print(pd.DataFrame(maximum_of_Versicolor))
    pause_or_quit()
        

def View_Maximum_Sizes_Virginica():
    print("Maximum of Virginica")
    print(pd.DataFrame(maximum_of_Virginica))
    pause_or_quit()
        




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

df = pd.read_csv("IRIScsv.csv")
sns.pairplot(df, hue="variety")
plt.show()

Source: https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029

PRESS KEY TO CONTINUE TO SEE RESULTS OF CODE
""")

    pause_or_quit()
    
    df = pd.read_csv("IRIScsv.csv")
    sns.pairplot(df, kind='scatter',hue='variety')
    plt.show()
    


def View_Data_As_Scatter_Plot():
    print("Save Scatter Plot")


    df = pd.read_csv("IRIScsv.csv")

    plt.scatter(df['sepal.length'], df['sepal.width'])
    plt.title("Sepal length versus sepal width")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.show()

    plt.scatter(df['petal.length'], df['petal.width'])
    plt.title("Petal length versus sepal width")
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")
    plt.show()



def View_Data_As_Histogram():

    """source https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib"""
    iris= datasets.load_iris()

    fig, axes = plt.subplots(nrows= 2, ncols=2)
    colors= ['blue', 'red', 'green']

    for i, ax in enumerate(axes.flat):
        for label, color in zip(range(len(iris.target_names)), colors):
            ax.hist(iris.data[iris.target==label, i], label=             
                                iris.target_names[label], color=color)
            ax.set_xlabel(iris.feature_names[i])  
            ax.legend(loc='upper right')


    plt.show()




"""
outputs a summary of each variable to a single text file,
saves a histogram of each variable to png files, and
outputs a scatter plot of each pair of variables.
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
    print("8 – Vied Data As Scatter Plot")
    print("9 – View Data As Histogram")
    print("x – Exit application")


if __name__ == "__main__":
    # execute only if run as a script
    main()
