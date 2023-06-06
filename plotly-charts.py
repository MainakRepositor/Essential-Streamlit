import streamlit as st
import numpy as np
import plotly.figure_factory as ff

st.subheader('Distribution Histogram in Plotly')

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

st.divider()
# =================CONTOUR PLOT=================

st.subheader('Contour Plot in Plotly')
import plotly.graph_objects as go
import streamlit as st

z = np.random.random_sample((3, 2))
fig = go.Figure(data=go.Contour(z=z))

st.plotly_chart(
    fig, 
    theme="streamlit",  # ✨ Optional, this is already set by default!
)
st.divider()
# ================= SCATTER PLOT ===================


import plotly.express as px
import streamlit as st


st.subheader('Scatter Plot in Plotly')
df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
