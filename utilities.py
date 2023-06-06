import pandas
import streamlit as st

# set page config

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# echo statement
with st.echo():
    st.write('This code will be printed') #prints like a code

# streamlit help
with st.expander('seek help'):
    st.help(pandas.DataFrame)
st.divider()

# get query
st.experimental_get_query_params()
{"show_map": ["True"], "selected": ["asia", "america"]}

# set query
st.experimental_set_query_params(
    show_map=True,
    selected=["asia", "america"],
)

