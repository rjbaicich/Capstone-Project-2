import streamlit as st # Aliasing the streamlit import as st

st.title('Endangered Fish Flash Cards')

st.image('https://pbs.twimg.com/media/E-GjyUsVgAMZ5q8.jpg:large')

st.header('Here are the different pages of my application:')

st.subheader('Your Fish Is')
st.text("""

        This application that is solely designed for educational purposes, provides valuable information about endangered fish species,
        including their name, species, genus, endangered score, location, and temperature.
        By highlighting these details, users can gain a deeper understanding of the critical 
        status of these species and the importance of conservation efforts.

        """)


st.image('https://www.cleveland.com/resizer/w0-DJ095Yw-jgxI2UxkCQZln6Jw=/1280x0/smart/advancelocal-adapter-image-uploads.s3.amazonaws.com/image.cleveland.com/home/cleve-media/width2048/img/plain_dealer_metro/photo/fishjpg-4aec78f162193aeb.jpg')


st.subheader('Further Learning')
st.text('''

The Further Learning page offers an opportunity to delve deeper into the fascinating world of
endangered fish species and conservation. This page provides a curated selection of additional
resources, references, and recommendations for users who are interested in expanding their knowledge
and understanding

        ''')


st.subheader('Summary')
st.text('Summary: Is a summarization page of my application.')


st.image('https://cdn.hswstatic.com/gif/endangered-fish-13.jpg')