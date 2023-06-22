import streamlit as st
import pandas as pd
import random
import requests
from googlesearch import search
from base import Base


# Read the CSV file containing the fish data
fish_data = pd.read_csv(r'C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\endangered_fish_sorted.csv')

# Check if the 'common_name' column is present
if 'common_name' not in fish_data.columns:
    st.error("The 'common_name' column is missing in the CSV file.")
    st.stop()

# Get the unique common names from the fish data
common_names = fish_data['common_name'].unique()

# Create a selectbox for users to choose a fish name
selected_common_name = st.selectbox('Select a fish name:', common_names)

if selected_common_name:
    base_csv_file = r'C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\endangered_fish_sorted.csv'
    base = Base(base_csv_file)

    # Get the fish data based on the selected common name
    fish_data = base.get_data_by_common_name(selected_common_name)

    if not fish_data.empty:
        st.write(fish_data)
        st.write('Species:', fish_data['species'])
        st.write('State:', fish_data['state'])
        st.write('Temperature:', fish_data['temp'])
        st.write('Common Name:', fish_data['common_name'])
        st.write('Endangered Score:', fish_data['Endangered Score'])

    #     # Search for fish images using Google
    #     query = selected_common_name + ' fish'
    #     image_urls = []
    #     counter = 0  # Counter to track the number of results
    #     for result in search(query, num_results=10):  # Increase the number of results to iterate over
    #         if result.endswith('.jpg') or result.endswith('.png'):
    #             image_urls.append(result)
    #             counter += 1
    #         if counter >= 5:  # Adjust the limit to the desired number of results
    #             break  # Stop iterating when the desired number of results is reached
    #         time.sleep(1)  # Delay for 1 second before making the next request

    #     if image_urls:
    #         # Retrieve and display the first image from the search results
    #         response = requests.get(image_urls[0])
    #         image = response.content if response.status_code == 200 else None
    #         if image:
    #             st.image(image, caption='Fish Image', use_column_width=True)
    #         else:
    #             st.write('Image not found.')
    #     else:
    #         st.write('No images found.')

    # else:
    #     st.write("Don't worry, the fish is not endangered. Fish not found.")

# Create a button to generate a random fish and display its data
if st.button('Generate Random Fish'):
    random_common_name = random.choice(common_names)
    random_fish_data = base.get_data_by_common_name(random_common_name)

    if not random_fish_data.empty:
        st.write(random_fish_data)
        st.write('Species:', random_fish_data['species'])
        st.write('State:', random_fish_data['state'])
        st.write('Temperature:', random_fish_data['temp'])
        st.write('Common Name:', random_fish_data['common_name'])
        st.write('Endangered Score:', random_fish_data['Endangered Score'])

        # # Search for fish images using Google
        # query = random_common_name + ' fish'
        # image_urls = []
        # counter = 0  # Counter to track the number of results
        # for result in search(query, num_results=10):  # Increase the number of results to iterate over
        #     if result.endswith('.jpg') or result.endswith('.png'):
        #         image_urls.append(result)
        #         counter += 1
        #     if counter >= 5:  # Adjust the limit to the desired number of results
        #         break  # Stop iterating when the desired number of results is reached

        # if image_urls:
        #     # Retrieve and display the first image from the search results
        #     response = requests.get(image_urls[0])
        #     image = response.content if response.status_code == 200 else None
        #     if image:
        #         st.image(image, caption='Fish Image', use_column_width=True)
        #     else:
        #         st.write('Image not found.')
        # else:
        #     st.write('No images found.')