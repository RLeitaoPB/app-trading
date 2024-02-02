import streamlit as st
import pandas as pd

if not st.session_state.authentication_status:
    st.info('Please Login from the Home page and try again.')
    st.stop()
else:
  st.title('Order History')

  order_history = pd.read_csv('./data/transactions.csv')
  st.dataframe(order_history)