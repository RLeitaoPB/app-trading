import streamlit as st

st.set_page_config(
  page_title='Trading App',
  layout='wide',
  initial_sidebar_state='collapsed',
)

titulo_style = "font-size: 32px; font-weight:bold; text-align:center;"

st.markdown("<h1 style='{}'>Trading App".format(titulo_style), unsafe_allow_html=True)