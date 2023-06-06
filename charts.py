import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.markdown('''# Types of Charts''')

#================LINE CHART==================
st.subheader("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.divider()
#================AREA CHART===================
st.subheader("Area Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

st.divider()
#================BAR CHART===================
st.subheader("Bar Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.divider()
#================HISTOGRAM====================
st.subheader("Histogram")
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
st.divider()
