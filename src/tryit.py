
import streamlit as st
import pandas as pd
from base import Base

# Read the CSV file containing the fish data
fish_data = pd.read_csv('C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\Combined_Less.csv')

# Get the unique common names from the fish data
common_names = fish_data['Common_name'].unique()

# Create a selectbox for users to choose a fish name
selected_common_name = st.selectbox('Select a fish name:', common_names)

if selected_common_name:
    base_csv_file = 'C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\Combined_Less.csv'
    base = Base(base_csv_file)

    # Get the fish data based on the selected common name
    fish_data = base.get_data_by_common_name(selected_common_name)

    if fish_data:
        st.write(fish_data)
        st.write('Name:', fish_data['Name'])
        st.write('Species:', fish_data['Species'])
        st.write('Genus:', fish_data['Genus'])
        st.write('Endangered Score:', fish_data['Endangered Score'])
        st.write('Location:', fish_data['Location'])
        st.write('Temperature:', fish_data['Temperature'])
    else:
        st.write('Dont worry not endangered! Fish not found.')
