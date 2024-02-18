# awards.py
# ENDG 233 F23
# BASHIR AADIL
# A terminal-based program for analyzing movie awards data.
# You must include the code listed below. You may add your own additional functions, variables, etc. 
# You may not import any modules.
# You may only use built-in functions that directly support strings, lists, dictionaries, sets, and tuples.
# Remember to include docstrings for your functions and comments throughout your code.
#


# ******************************************************************************************************
# Data is imported from the included awards_data.py file. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
from awards_data import SAG, oscars, NBR, ISA, GLAAD, NAACP
award_list_names = ['sag', 'oscars', 'nbr', 'isa', 'glaad', 'naacp']
award_list_options = [SAG, oscars, NBR, ISA, GLAAD, NAACP]
# ******************************************************************************************************



# ******************************************************************************************************
# DEFINE FUNCTIONS HERE
def count_awards(movie_title):
    titles = movie_title.lower().strip()
    count = 0
    for i in award_list_options:
        for j in i:
            if titles == j.lower():
                count+=1
    print("--Number of Awards Won--")
    print(count)
    '''
    First step to make the input and the value in the awards list the same,
    if the input exists.
    If they do exist, print the number of awards.
    '''

def print_award_winners(awards):
     if awards == "oscars":
        for i in set(oscars):
            print(i)
     else:
        rem_awards = awards.upper()
        if rem_awards == "SAG":
            for i in set(SAG):
                print(i)
        elif rem_awards == "NBR":
            for i in set(NBR):
                print(i)
        elif rem_awards == "ISA":
            for i in set(ISA):
                print(i)
        elif rem_awards == "GLAAD":
            for i in set(GLAAD):
                print(i)
        else:
            for i in set(NAACP):
                print(i)
       
     '''
     We first bring the input to lower case to try to get "oscars"
     If it is not oscars, we keep going through the conditions to find the award option to print.
     we use set() to prevent duplicates.
     '''

# ******************************************************************************************************
print("ENDG 233 Awards Data Program")

# DEFINE MAIN CODE BELOW

# You may find the following strings helpful for the interface design:
# "\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "
# "Please enter the movie title you would like to search: "
# "\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n"
# "Awards list not found."
# "You must select either 1, 2, or 0."
# "Thank you for using the awards data program."
# "--Number of Awards Won--"
# "--Requested Award Winners--"




choice = int(input("\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "))


while choice != 0:
    if choice == 1:
        movie = input("Please enter the movie title you would like to search: ")
        count_awards(movie)                   # usage of the function if the choice is equal to 1 
    elif choice == 2:
        awards = input( "\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n")
        awards = awards.lower().strip()
        if awards in award_list_names:
            print("--Requested Award Winners--")
            print_award_winners(awards)           # usage of the function if the choice is equal to 2
        else:
            print("Awards list not found.")
    if choice != 0 and choice != 1 and choice != 2:              #To prevent use of a value not given
        print("You must select either 1, 2, or 0.")
    choice = int(input("Select 1 to search a specific movie, 2 to print specific rewards results, 0 to end: "))     #To keep repeating until we end the loop
else:
    print("Thank you for using the awards data program.")    

