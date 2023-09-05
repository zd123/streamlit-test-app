import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Create a page header
st.header("Welcome to my homepage! 👋")


# Create three columns 
col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.image('images/covid-icon.png')
    st.write('<a href="/covid"> Check out my Covid Dashboard</a>', unsafe_allow_html=True)

    st.image('images/friends.png')
    st.write('<a href="https://www.behance.net/datatime">View more pretty data visualizations.</a>', unsafe_allow_html=True)


with col2:
    st.image('images/covid-map.png')
    st.write('<a href="/map"> Check out my Interactive Map</a>', unsafe_allow_html=True)    
    
    st.image('images/github.png')
    st.write('<a href="https://github.com/zd123"> View more awesome code on my github.</a>', unsafe_allow_html=True)    

with col3:    
    st.image('https://i1.sndcdn.com/avatars-000034142709-fv26gu-t500x500.jpg')
    st.markdown('<a href="/Bio">Learn more about me as a human :blush:</a>', unsafe_allow_html=True)






