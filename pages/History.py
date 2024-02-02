import streamlit as st
import pandas as pd

titulo_style = "font-size: 32px; font-weight:bold; text-align:center;"

st.markdown("<h1 style='{}'>History".format(titulo_style), unsafe_allow_html=True)

order_history = pd.read_csv('./data/transactions.csv')
st.dataframe(order_history)