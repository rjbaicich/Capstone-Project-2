import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file containing the fish data
df = pd.read_csv(r'C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\endangered_fish_sorted.csv')

# Set page title
st.title("Did You Know?")

st.image('https://www.eregulations.com/assets/images/books/flfw/23flfw/6.jpg')

# Display a paragraph
st.write("""
        Healthy freshwater ecosystems are crucial for the thriving populations of
        freshwater fish and the well-being of humans. Rivers directly provide drinking
        water to at least 2 billion people and support a quarter of the world's food production.
        """)

st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Nashua_River_Fallfish.jpg/1280px-Nashua_River_Fallfish.jpg')

# Count the occurrences of each state
most_common_state = df['state'].value_counts().head(10)

# Create a bar graph for the most common states with species occurrences
fig2, ax2 = plt.subplots(figsize=(10, 6))
bar2 = ax2.bar(most_common_state.index, most_common_state.values)
plt.xlabel('State')
plt.ylabel('Occurrences')
plt.title('Top 10 States with Species Occurrences')
plt.xticks(rotation=90)

# Count the occurrences of each species
top_species = df['species'].value_counts().head(10)

# Create a bar graph for the top species
fig1, ax1 = plt.subplots(figsize=(10, 6))
bar1 = ax1.bar(top_species.index, top_species.values)
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Top 10 Species')
plt.xticks(rotation=90)

# Display a block of space with a paragraph
st.write("---")
st.write("""
        More than 200 million people rely on freshwater fish as their primary source of
        protein, particularly in land-locked and low-income countries. Presently, 60 million
        individuals, with over half of them being women, depend on freshwater fish for their livelihoods.
        """)

# Display the initial graphs
st.pyplot(fig2)
st.pyplot(fig1)

st.image('https://upload.wikimedia.org/wikipedia/commons/9/9d/Creek_Chub%2C_Semotilus_atromaculatus.jpg')

st.write("""
        Preserving freshwater fisheries is essential for the overall ecosystem health and brings benefits
        to all those who depend on it.
        """)

st.image('https://files.worldwildlife.org/wwfcmsprod/images/Buffalo_fish/story_full_width/80b2nhfpi6_Buffalo_fish__c__Freshwaters_Illustrated.jpg')
