import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Read the CSV file containing the fish data
df = pd.read_csv(r'C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\endangered_fish_sorted.csv')

#Set page title
st.title("Did You Know?")

st.write("---")

#Add subheader paragraph
st.write("""

        Unfortunately, freshwater fish and their habitats are often overlooked. Freshwater fish play a critical
        role in maintaining the health of aquatic ecosystems, yet they are often overlooked when it comes
        to conservation efforts. With their habitats facing increasing threats such as pollution, habitat
        destruction, and overfishing, it is crucial to raise awareness about the importance of preserving
        freshwater fish and the ecosystems they inhabit.

        """)

st.write("---")
st.image('https://www.eregulations.com/assets/images/books/flfw/23flfw/6.jpg')
st.write("---")

#Display a paragraph
st.write("""

        Healthy freshwater ecosystems are crucial for the thriving populations of
        freshwater fish and the well-being of humans. Rivers directly provide drinking
        water to at least 2 billion people and support a quarter of the world's food production.
        
        """)

st.write("---")
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Nashua_River_Fallfish.jpg/1280px-Nashua_River_Fallfish.jpg')
st.write("---")

#Plot and display the top 10 species graph
top_species = df['species'].value_counts().head(10)
fig1, ax1 = plt.subplots(figsize=(10, 6))
top_species.plot(kind='bar', color='purple')
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Top 10 Species')

#Display the top 10 species graph
st.pyplot(fig1)

#Plot and display the scatter plot of average temperature by year
fig2, ax2 = plt.subplots(figsize=(10, 6))
plt.scatter(df['year'], df['temp'], alpha=0.5, color='red')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Scatter plot of Average Temperature by Year')

#Display the scatter plot
st.pyplot(fig2)

#Find state with the most occurrences in the "State" column
most_common_states = df['state'].value_counts()
most_common_state = most_common_states.idxmax()
fig3, ax3 = plt.subplots(figsize=(10, 6))
most_common_states.plot(kind='bar', color='green')
plt.xlabel('State')
plt.ylabel('Occurrences')
plt.title('Top 10 States with Species Occurrences')
plt.xticks(rotation=90)

#Display the top 10 states graph
st.pyplot(fig3)


st.write("---")
st.write("""
        More than 200 million people rely on freshwater fish as their primary source of
        protein, particularly in land-locked and low-income countries. Presently, 60 million
        individuals, with over half of them being women, depend on freshwater fish for their livelihoods.
        """)

st.write("---")
st.image('https://upload.wikimedia.org/wikipedia/commons/9/9d/Creek_Chub%2C_Semotilus_atromaculatus.jpg')
st.write("---")

st.write("""
        Preserving freshwater fisheries is essential for the overall ecosystem health and brings benefits
        to all those who depend on it.
        """)

st.write("---")
st.image('https://files.worldwildlife.org/wwfcmsprod/images/Buffalo_fish/story_full_width/80b2nhfpi6_Buffalo_fish__c__Freshwaters_Illustrated.jpg')