import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
  page_title='Trading App',
  layout='wide',
  page_icon="chart_with_upwards_trend",
  initial_sidebar_state='expanded',
)

st.title('Trading App')

import yaml
from yaml.loader import SafeLoader
with open('./config.yaml') as file:
  config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized'],
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Dashboard')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')