import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title='FIFA 22 OVR Player Predict',
    page_icon='⚽',
    layout='wide',
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox('Select Page', ['EDA', 'Prediction'])

if page == 'EDA':
  eda.run()
elif page == 'Prediction':
  prediction.run()