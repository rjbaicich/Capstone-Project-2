import streamlit as st
import pandas as pd
import random
import requests
from base import Base

#Read the CSV file containing the fish data
fish_data = pd.read_csv(r'C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\endangered_fish_sorted.csv')

#Check if the 'common_name' column is present
if 'common_name' not in fish_data.columns:
    st.error("The 'common_name' column is missing in the CSV file.")
    st.stop()

#Set page title
st.title("Your Fish Is...")

#Apply custom CSS to set the background color
page_bg_color = "#99F9DC"
color_css = f"""
    <style>
    body {{
        background-color: {page_bg_color};
    }}
    </style>
"""
st.markdown(color_css, unsafe_allow_html=True)

#Get the unique common names from the fish data
common_names = fish_data['common_name'].unique()

#Create a selectbox for users to choose a fish name
selected_common_name = st.selectbox('Select a fish name:', common_names, format_func=lambda name: f"{name}", help="Choose a fish name")


if selected_common_name:
    base_csv_file = r'C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\endangered_fish_sorted.csv'
    base = Base(base_csv_file)

    #Get the fish data based on the selected common name
    fish_data = base.get_data_by_common_name(selected_common_name)

    if not fish_data.empty:
        st.write(fish_data)
        st.write('Species:', fish_data['species'])
        st.write('State:', fish_data['state'])
        st.write('Common Name:', fish_data['common_name'])
        st.write('Endangered Score:', fish_data['Endangered Score'])

#Create a button to generate a random fish and display its data
if st.button('Generate Random Fish'):
    random_common_name = random.choice(common_names)
    random_fish_data = base.get_data_by_common_name(random_common_name)

    if not random_fish_data.empty:
        st.write(random_fish_data)
        st.write('Species:', random_fish_data['species'])
        st.write('State:', random_fish_data['state'])
        st.write('Common Name:', random_fish_data['common_name'])
        st.write('Endangered Score:', random_fish_data['Endangered Score'])


        # Create a selectbox for users to choose a state
selected_state = st.selectbox('Select a state:', fish_data['state'].unique(), help="Choose a state")

# Filter fish data based on the selected state
filtered_fish_data = base.get_data_by_state(selected_state)

# Display filtered fish data
if not filtered_fish_data.empty:
    st.write(f"Fish Data for {selected_state}:")
    st.write(filtered_fish_data)


import matplotlib.pyplot as plt
import seaborn as sns

# Visualize Endangered Scores
fig, ax = plt.subplots()
sns.histplot(random_fish_data['Endangered Score'], bins=10, kde=True, ax=ax)
ax.set_title('Distribution of Endangered Scores')
ax.set_xlabel('Endangered Score')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Create a radio button for users to choose endangered status
selected_status = st.radio('Select Endangered Status:', ['Endangered', 'Threatened', 'Not Listed'], index=2, help="Choose an endangered status")

# Filter fish data based on the selected endangered status
filtered_status_data = base.get_data_by_status(selected_status)

# Display filtered fish data
if not filtered_status_data.empty:
    st.write(f"Fish Data for {selected_status} Status:")
    st.write(filtered_status_data)

import folium

# Get latitude and longitude from the fish data
latitude, longitude = fish_data['latitude'].iloc[0], fish_data['longitude'].iloc[0]

# Create a folium map centered around the fish location
map_fish = folium.Map(location=[latitude, longitude], zoom_start=10)

# Add a marker for the fish location
folium.Marker(location=[latitude, longitude], popup=selected_common_name).add_to(map_fish)

# Display the map
st.write("Fish Location on Map:")
st.markdown(map_fish._repr_html_(), unsafe_allow_html=True)

# Highlight important information
st.subheader(f"Details for {selected_common_name}:")

# Check if the fish is endangered and highlight the status
if fish_data['Endangered Status'].iloc[0] == 'Endangered':
    st.write('Endangered Status:', f"**{fish_data['Endangered Status'].iloc[0]}**")
else:
    st.write('Endangered Status:', fish_data['Endangered Status'].iloc[0])

# Display other details
st.write('Species:', fish_data['species'])
st.write('State:', fish_data['state'])
st.write('Common Name:', fish_data['common_name'])
st.write('Endangered Score:', fish_data['Endangered Score'])
