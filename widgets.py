import streamlit as st
from datetime import time
from datetime import datetime
import numpy as np

st.header('Streamlit Widgets')
st.divider()


st.subheader("Buttons")
# Simple Button
if st.button('Say Hello'):
    st.write('Hello Streamlit')

else:
    st.write('Goodbye!')

st.divider()

# download text
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

# download binary file
binary_contents = b'example content'
# Defaults to 'application/octet-stream'
st.download_button('Download binary file', binary_contents)

# download image
with open("flower.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
          )
st.divider()


# checkbox
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
else:
    st.write("Do you agree?")
st.divider()

# Radio buttons with checkbox widgets

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )
st.divider()
# dropdown or select box

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.divider()

# multiselect or multiple selector

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    )

st.write('You selected:', options)

st.divider()


st.subheader("Sliders")

# age slider

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.divider()

# range slider

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.divider()

# duration slider

appointment = st.slider(
    "Choose your event duration:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.divider()

# datetime slider

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

# textual slider

st.divider()

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

st.divider()


st.subheader("Widgets")

# text input widget
title = st.text_input('Movie title', '')
st.write('The current movie title is', title)
st.divider()
# number input widget

number = st.number_input('Insert a number')
st.write('The current number is ', number)
st.divider()

# text area
txt = st.text_area('''''')
st.write('Output text:', txt)

# file uploader
    
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# camera widget

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    st.image(img_file_buffer)
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))

# color picker widget

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)
st.divider()

# Media Widgets
st.subheader("Media Widgets")
st.text('Image widget')
from PIL import Image
image = Image.open('flower.png')
st.image(image, caption='Image of a flower')

st.divider()

# audio widget
st.text('Audio widget')
audio_file = open('audio.wav', 'rb')
audio_bytes = audio_file.read()

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)
st.divider()

# video widget
st.text('Video widget')
video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

