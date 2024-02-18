import numpy as np
import matplotlib.pyplot as plt


# ******************************************************************************************************
# Data is imported from the included csv file. You may not modify the content, order, or location of the csv file.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter = ',', skip_header = True, dtype = str)
# ******************************************************************************************************
danceability = np.array([row[7] for row in data])
bpm = np.array([row[4] for row in data])
plt.scatter(danceability,bpm, label="Song Stats")
plt.figure(figsize=[15,9])
plt.title("Danceability vs Beats per Minute")
plt.xlabel("BPM")
plt.ylabel("Danceability") 
plt.legend('upper right')
plt.savefig("figure1.png")
plt.show()
    