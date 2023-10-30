import streamlit as st

st.title('Further Learning')

st.subheader('Additional Resources')

st.write("---")
st.image('https://mymodernmet.com/wp/wp-content/uploads/2019/05/ocean-art-7.jpg')
st.write("---")

#Define the options for the drop-down menu
options = {
    'Kaggle Dataset': 'https://www.kaggle.com/datasets/harshithgupta/endangered-fish-data?select=Combined_Less.csv',
    'NOAA Fisheries': 'https://www.fisheries.noaa.gov/species-directory/threatened-endangered',
    'New York State DEC': 'https://www.dec.ny.gov/animals/7008.html',
    'Greenpeace': 'https://www.greenpeace.org/usa/oceans/sustainable-seafood/red-list-fish/',
    'Scuba Travel': 'https://www.scubatravel.co.uk/fisheat.html',
    'US Fish and Wildlife Service': 'https://ecos.fws.gov/ecp/report/species-listings-by-tax-group?statusCategory=Listed&groupName=Fishes',
    'WWF Endangered Marine Species Guide': 'https://files.worldwildlife.org/wwfcmsprod/files/Publication/file/6yj122pa08_WWF_Endangered_Marine_Species_Guide__September_2019_v3_.pdf',
    'A-Z Animals Blog': 'https://a-z-animals.com/blog/endangered-fish-population-by-state/'
    'National Fish and Wildlife Foundation': 'https://www.nfwf.org/'
    'Oceana': 'https://usa.oceana.org/save-sea-turtles'
    'MarineBio Conservation Society': 'https://marinebio.org/'
    'Marine Stewardship Council': 'https://www.msc.org/'
    'IUCN Red List of Threatened Species': 'https://www.iucnredlist.org/'
    'The Nature Conservancy': 'https://www.nature.org/en-us/what-we-do/our-insights/perspectives/the-race-to-protect-ocean-species/'
}

#Display the drop-down menu
selected_option = st.selectbox('Select a resource', list(options.keys()))

#Get the selected URL based on the selected option
selected_url = options[selected_option]

#Display the link using HTML tags
st.markdown(f'<a href="{selected_url}" target="_blank">{selected_option}</a>', unsafe_allow_html=True)

st.write("---")
st.image('https://www.fisheries.noaa.gov/s3/dam-migration/ohc_infographic.png')