#streamlit run *insert file name.py*

import streamlit as st
import pandas as pd

#Title
st.title("Spotify Song Analyzer")


#Read data
data = pd.read_csv("spotify dataset.csv")
data = data.drop_duplicates()
data = data[["track_name", "artists", "album_name", "explicit", "danceability", "energy", "valence", "tempo", "duration_ms", "loudness", "track_genre", "popularity"]]
data.rename(columns = {"track_genre": "Genre",
                       "artists": "Artist",
                       "album_name": "Album",
                       "track_name": "Title",
                       "explicit": "Explicit",
                       "danceability": "Danceability",
                       "energy": "Energy",
                       "valence": "Valence",
                       "tempo": "Tempo",
                       "duration_ms": "Length",
                       "popularity": "Popularity",
                       "loudness": "Loudness"}, inplace= True)
genres = data["Genre"].unique()

#Sidebar
st.sidebar.title("Filter Options")
danceability = st.sidebar.slider("Danceability", 0.0, 1.0, (0.0, 1.0), 0.01)
energy = st.sidebar.slider("Energy", 0.0, 1.0, (0.0, 1.0), 0.01)
mood = st.sidebar.slider("Mood", 0.0, 1.0, (0.0, 1.0), 0.01)
tempo = st.sidebar.slider("Tempo (BPM)", 0, 250, (0, 250), 1)

searchbox = st.sidebar.text_input("Search for album, song, or artist")

choosegenre = st.sidebar.multiselect("Search by genre", genres, default = None)

plotXs = st.sidebar.multiselect("X axis parameters", ["Danceability"], default=None)
plotYs = st.sidebar.multiselect("Y axis parameters", ["Energy", "Tempo", "Loudness"], default = None)

explicit = st.sidebar.toggle("Explicit", value = False)

#Filtering
data = data[(data["Danceability"]>= danceability[0]) & (data["Danceability"]<= danceability[1])]
data = data[(data["Energy"]>= energy[0]) & (data["Energy"]<= energy[1])]
data = data[(data["Valence"]>= mood[0]) & (data["Valence"]<= mood[1])]
data = data[(data["Tempo"]>= tempo[0]) & (data["Tempo"]<= tempo[1])]

if searchbox:
    data = data[(data["Title"].str.contains(searchbox, case = False)) | (data["Artist"].str.contains(searchbox, case = False)) | (data["Album"].str.contains(searchbox, case = False))]

if explicit == False:
    data = data[data["Explicit"]==False]

if choosegenre:
    data["Genre Filter"] = data.apply(lambda x: x["Genre"] in choosegenre, axis = 1)
    data = data[(data["Genre Filter"] == True)]
    data = data.drop(columns = ["Genre Filter"])

if len(data) == 0:
    st.warning('No matches found, try widening your filters', icon="⚠️")

else:
    st.dataframe(data)
    
    col1, col2, col3 = st.columns(3)
    col1.metric(":red[Total Songs Found]", f":red[{len(data)}]")
    col2.metric(":green[Average Popularity]", f":green[{round(data["Popularity"].mean())}]")
    m60 = data[data["Popularity"] >= 60]
    col3.metric(":blue[Amount of Popular Songs]", f":blue[{len(m60)}]")

    popularSongs = data.sort_values(by="Popularity", ascending = False).reset_index(drop=True)
    st.dataframe(popularSongs.head(10))