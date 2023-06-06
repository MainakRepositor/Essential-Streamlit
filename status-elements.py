import streamlit as st
import time

# st.progress
progress_text = "This is the operation of a progress bar"
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

# st.spinner
st.subheader("Spinner ready!")
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Done!')
st.divider()

# balloons
st.subheader("Balloons inflated!")
st.balloons()
st.divider()

# snow
st.subheader("Some snowfalls!")
st.snow()
st.divider()

# status bars

st.header("Status indicators")
st.error("This is error")
st.warning("This is warning")
st.success("This is success")
st.info("This is info")
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)