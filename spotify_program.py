# spotify_program.py
# AADIL BASHIR, ENDG 233 F23
# A terminal-based application to process and plot data based on given user input and provided data values.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.


import numpy as np
import matplotlib.pyplot as plt
import math
# ******************************************************************************************************
# Data is imported from the included csv file. You may not modify the content, order, or location of the csv file.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter = ',', skip_header = True, dtype = str)
# ******************************************************************************************************


# ******************************************************************************************************
# DEFINE BONUS CLASS HERE (optional)
class Song:
    #We're saving each column as an attribute, so:
    def __init__(self, row):
        self.row = row
        self.title = "Blinding Lights"
        self.artist = 'The Weekend'
        self.release = 0.0
        self.num_of_streams = 0.0
        self.bpm = 0.0
        self.key = 'C-sharp'
        self.mode = 'Major'
        self.danceability = 0.0
        self.valence = 0.0
        self.energy = 0.0
        self.acousticness = 0.0
        self.instrumentalness= 0.0
        self.liveness = 0.0
        self.speechiness = 0.0
        self.percentages = np.array(num[8:] for num in data[row])
         
        
        
    def bar(self):
        plt.figure
        x_axis = column_names[8:]
        plt.bar(x_axis,self.percentages)
        plt.xlabel("Feature")
        plt.ylabel("Percentage")
        plt.title("Song Stats for Believer")
        xtick = [x for x in range(0,100,10)]
        plt.xticks(xtick)
        plt.savefig("figure2.png")

# ******************************************************************************************************
# DEFINE FUNCTIONS HERE

def feature_stats(input_value):
    converted_data = np.array([row[input_value] for row in data], dtype= int)
    maximum_value = converted_data.max()
    minimum_value = converted_data.min()
    mean_value  = math.floor(np.mean(converted_data))
    index = converted_data.argmax() 
    top_song = data[index][0]
    
    print(f"Highest value: {maximum_value}")
    print(f"Lowest value: {minimum_value}")
    print(f"Mean value: {mean_value}")
    print(f"Top song in selected feature: {top_song}")
    return top_song
    
    '''
    First, we get the column the user requests, then we find the maximum, 
    minimum, mean value, and the song at the same row as the index location
    of the highest value requested.
    '''
    

def age_stats(input_value):
    converted_date = np.array([row[input_value] for row in data], dtype= int)
    max_date = converted_date.max()
    min_date = converted_date.min()
    index = converted_date.argmin()    #Gives the row wit the oldest song
    artists = data[index][1]
    key = data[index][5]
    mode = data[index][6] 
    print(f"Span of years: {max_date - min_date}")
    print(f"Artist of oldest song: {artists}")
    print(f"Key and mode of oldest song: {key} {mode}")
    '''
    First get the data needed from the csv file, input them into variables,
    Then print the phrase with the variables.
    '''


# ******************************************************************************************************
# DEFINE MAIN CODE
# Add your code within the main function. A docstring is not required for this function.

# You may find the following hints helpful:
# A list comprehension can be used to convert data values in a column and create a new array
# e.g. converted_data = np.array([row[column_value] for row in data], dtype='float')
# NumPy has many built-in functions/methods, including those for finding the index location of a value (e.g. argmax(), argmin(), etc.)
# Refer to the NumPy and Matplotlib documentation for more


def main():
    print("ENDG 233 Spotify Statistics\n")
    print("Song analysis options: ")
    for menu, option in enumerate(column_names):
        print(menu, option)
    print("Choose -1 to end the program.")
    # Continue main code below
    user_input = int(input("Please enter a song feature to analyze: ")) 
    fakes = [0,1,5,6]
    feature_num = [3,4,7,8,9,10,11,12,13]

    while user_input != -1:
        if user_input == 2:
            age_stats(user_input)
        elif user_input in feature_num:
            feature_stats(user_input)
        elif user_input in fakes:
            user_input = int(input("Please enter a song feature to analyze: "))
        else:
            print("You must enter a valid menu option.")
        user_input = int(input("Please enter a song feature to analyze: "))
    

    # Create and print danceability vs. bpm plot
    danceability = np.array([row[7] for row in data], dtype= float)
    bpm = np.array([i[4] for i in data], dtype= float)
    xtick = [x for x in range(60,220,20)]
    ytick = [y for y in range(20,100,10)]


    
    plt.figure(figsize=[20,12])     #This comes first else, nothing shows
    plt.scatter(bpm, danceability, label="Song Stats", c="blue")
    plt.title("Danceability vs Beats per Minute")
    plt.xlabel("BPM")
    plt.ylabel("Danceability")
    plt.legend(loc='upper right')   #Allows the label to be on the top right
    plt.xticks(xtick)              #For the ticks on the x axis to be the same as the picture
    plt.yticks(ytick)              #For the ticks on the y axis to be the same as the picture
    plt.savefig("figure1.png")     #To save the scatter plot
    plt.show()
    # Create bonus Song object (optional)
    # Create and print bonus plot (optional)




if __name__ == '__main__':
    main()
