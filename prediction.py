# Import libraries
import pickle
import json
import pandas as pd
import numpy as np
import streamlit as st

# Load all files
with open('model_inf/model_lin_reg.pkl', 'rb') as file_1:
  model_lin_reg = pickle.load(file_1)

with open('model_inf/model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('model_inf/model_encoder.pkl','rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('model_inf/list_num_cols.txt', 'r') as file_4:
  list_num_cols = json.load(file_4)

with open('model_inf/list_cat_cols.txt', 'r') as file_5:
  list_cat_cols = json.load(file_5)

def run():
  # Membuar form
  with st.form('fifa22-ovr-predict'):
    name = st.text_input('Player Name', value='Name')
    age = st.number_input('Age', min_value=16, max_value=45, step=1, help='Enter the players age', value=25)
    weight = st.number_input('Weight (kg)', min_value=60, max_value=120, step=1, help='Enter the players weight', value=75)
    height = st.slider('Height (cm)', min_value=150, max_value=230, help='Enter the players height', value=180)
    price = st.number_input('Price (EUR)', min_value=0, max_value=1000000000, step=10000, help='Enter the players price', value=1000000)
    st.markdown('---')

    attacking_work_rate = st.selectbox('Attacking Work Rate', options=['Low', 'Medium', 'High'], help='Select the players attacking work rate')
    defensive_work_rate = st.radio('Defensive Work Rate', options=['Low', 'Medium', 'High'], help='Select the players defensive work rate')
    st.markdown('---')

    pace = st.number_input('Pace', min_value=0, max_value=100, step=1, help='Enter the players pace', value=50)
    shooting = st.number_input('Shooting', min_value=0, max_value=100, step=1, help='Enter the players shooting', value=50)
    passing = st.number_input('Passing', min_value=0, max_value=100, step=1, help='Enter the players passing', value=50)
    dribbling = st.number_input('Dribbling', min_value=0, max_value=100, step=1, help='Enter the players dribbling', value=50)
    defending = st.number_input('Defending', min_value=0, max_value=100, step=1, help='Enter the players defending', value=50)
    physicality = st.number_input('Physicality', min_value=0, max_value=100, step=1, help='Enter the players physicality', value=50)
    st.markdown('---')

    submitted = st.form_submit_button('Predict')

    # Create a new data
    # Use all columns not just the results of feature selection
    data_inf = {
        'Name': name,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Price': price,
        'AttackingWorkRate': attacking_work_rate,
        'DefensiveWorkRate': defensive_work_rate,
        'PaceTotal': pace,
        'ShootingTotal': shooting,
        'PassingTotal': passing,
        'DribblingTotal': dribbling,
        'DefendingTotal': defending,
        'PhysicalityTotal': physicality
    }

    data_inf = pd.DataFrame([data_inf])
    data_inf

    if submitted:
      # Split between numerical and categorical columns
      data_inf_num = data_inf[list_num_cols]
      data_inf_cat = data_inf[list_cat_cols]

      # Feature scaling and encoding
      data_inf_num_scaled = model_scaler.transform(data_inf_num)
      data_inf_cat_encoded = model_encoder.transform(data_inf_cat)
      data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)

      # Predict using the model
      prediction = model_lin_reg.predict(data_inf_final)
      st.write(f'The predicted OVR for {name} is: {prediction[0]:.2f}')

if __name__ == '__main__':
  run()