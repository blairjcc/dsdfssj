import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in JCC')

st.button('Click me')
st.experimental_data_editor('Edit data', data)
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
st.download_button('Download file', data)
st.camera_input("Take a picture")
st.color_picker('Pick a color')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')


# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)


st.subheader('Map of all pickups at %s:00' % hour_to_filter)

