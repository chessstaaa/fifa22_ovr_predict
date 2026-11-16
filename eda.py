import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image # Untuk load gambar
import plotly.express as px

def run():
    # Membuat title
    st.title('OVR Player Predict FIFA 22')

    # Membuat sub-header
    st.subheader('This page contains Exploratory Data Analysis (EDA)')

    # Menulis baris
    st.write('By *Kai Emilian*')
    # st.write('# Kai Emilian')
    # st.write('## Kai Emilian')

    # Memasukan dataset
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.4/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)

    # Memasukan gambar
    image = Image.open('img_assets/madrid.jpeg')
    st.image(image, caption='EDA FIFA 2022')

    # Menampilkan histogram OVR
    # st.write('### Histogram of Player Overall Ratings')
    # fig = plt.figure(figsize=(10, 5))
    # sns.histplot(df['Overall'], bins=20, kde=True)
    # st.pyplot(fig)

    # Membuat histogram berdasarkan input user
    st.write('### Histogram by User Input')
    fig = plt.figure(figsize=(10, 5))
    option = st.selectbox('Select a column to plot', ('Overall', 'Weight', 'Height', 'ShootingTotal'))
    sns.histplot(df[option], bins=20, kde=True)
    st.pyplot(fig)

    # Membuat plotly plot
    st.write('### Plotly Plot - Rating vs Price')
    fig = px.scatter(df, x='Overall', y='ValueEUR', title='Rating vs Price')
    st.plotly_chart(fig)

    # Memasukan gambar
    image = Image.open('img_assets/madrid-2.jpeg')
    st.image(image, caption='EDA FIFA 2022')

if __name__ == '__main__':
    run()