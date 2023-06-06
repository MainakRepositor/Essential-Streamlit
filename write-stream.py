# Hello streamlit with write, header and subheader
import streamlit as st

st.write("Hello **Streamlit** write") # write a line
st.caption('Hello Caption') # write a caption
st.header("Hello Header") # write a header
st.subheader("Hello Subheader") # write a subheader
st.markdown('''**Hello Markdown in Bold**''') # write a markdown in bold
st.markdown ('''***Hello Markdown in italics***''') # write a markdown in italics
st.markdown('''# Hello in H1''') # write a markdown in H1
st.markdown('''## Hello in H2''') # write a markdown in H2
st.markdown('''### Hello in H3''') # write a markdown in H3
st.markdown('''#### Hello in H4''') # write a markdown in H4
st.markdown('''##### Hello in H5''') # write a markdown in H5
st.markdown('''###### Hello in H6''') # write a markdown in H6
st.code('int a = 15') # write a code
st.divider() #set a <hr> tag or line divider
st.latex('\int a^2\,dx +\int b^2\,dx +\int sin x\,dx') # write a latex expression
