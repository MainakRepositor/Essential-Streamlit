import streamlit as st
import pandas as pd
import numpy as np
import random

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.subheader('A dataframe of random values of 50x20 dimension')
st.dataframe(df)  # Same as st.write(df)

#=====================================================
st.subheader('A dataframe of random values of 50x20 dimension, highlighting max values column-wise')
st.dataframe(df.style.highlight_max(axis=0))

#=====================================================

st.subheader('A dataframe with container widths')
# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)

#=====================================================