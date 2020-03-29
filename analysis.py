"""
Author Christopher Collins
"""


from colorama import init, Fore, Back, Style

from PIL import Image



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
averageofdata = IrisData.mean(axis = 0, skipna = True)
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
            display_menu()
        elif (choice == "4"):
            clear_screen()
            View_Minimum_Sizes_Iris()
            display_menu()
        elif (choice == "5"):
            clear_screen()
            View_Maximum_Sizes_Iris()
            display_menu()
        elif (choice == "6"):
            clear_screen()
            
            display_menu()
        elif (choice == "7"):
            clear_screen()
            View_Data_As_Graph()
            display_menu()
        elif (choice == "8"):
            clear_screen()
            View_Data_As_Histogram()
            display_menu()
        elif (choice == "9"):
            clear_screen()
            Save_Histogram()
            display_menu()

        elif (choice == "x"):
            break;
        else:
            display_menu()


def pause_or_quit():
    print("\n\n")
    os.system("""bash -c 'read -s -n 1 -p "Press any key to continue or q to quit..."'""")
    clear_screen()


 
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print('returning to menu!')
        main()


def Introduction_To_Iris_Data_Set():
    print("""
This python application is used to access the Iris Dataset
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
    print(averageofdata)




    pause_or_quit()

    print("Average of Setosa")
    
    print(average_of_Setosa)

    pause_or_quit()
        



    print("Average of Versicolor")
    
    print(average_of_Versicolor)

    pause_or_quit()
        


    print("Average of Virginica")
    
    print(average_of_Virginica)

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
    print(minimum_of_data)




    pause_or_quit()

    print("Minimum of Setosa")
    
    print(minimum_of_Setosa)

    pause_or_quit()
        

    print("Minimum of Versicolor")
    
    print(minimum_of_Versicolor)

    pause_or_quit()
        


    print("Minimum of Virginica")
    
    print(minimum_of_Virginica)

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
    print(maximum_of_data)




    pause_or_quit()

    print("Maximum of Setosa")
    
    print(maximum_of_Setosa)

    pause_or_quit()
        



    print("Maximum of Versicolor")
    
    print(maximum_of_Versicolor)

    pause_or_quit()
        


    print("Maximum of Virginica")
    
    print(maximum_of_Virginica)

    pause_or_quit()
        




def Save_Summary_Of_Average_Iris_Sizes_To_Text_File():
    print("Save Summary Of Average Iris Sizes To Text File")

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
    sns.pairplot(df, hue="variety")
    plt.show()
    

def Save_Scatter_Plot():
    print("Save Scatter Plot")


def View_Data_As_Histogram():
    print("View Data As Histogram")
    

def Save_Histogram():
    print("Save Histogram")


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
