import streamlit as st
import pandas as pd
import numpy as np

def foo():
	print('bar')

st.set_page_config(layout='wide')
st.title('Streamlit Test App')

st.subheader('Interactive Widgets')

st.button('Click me')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100,50)
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

st.subheader('Text Items')

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

st.subheader('Media Items')
st.image('./doggo-unsplash.jpp')
st.audio(data)
st.video(data)
link = '[GitHub](http://github.com)'
st.markdown(link, unsafe_allow_html=True)

st.subheader('Side Bar')
with st.sidebar:
	st.radio('Select one:', [



st.subheader('Map of all pickups at %s:00' % hour_to_filter)

