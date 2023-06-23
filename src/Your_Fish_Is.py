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