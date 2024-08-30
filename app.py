import streamlit as st
import pandas as pd
import requests

'''
# Taxi Fare Model

### Enter information here:
'''

#1. Let's ask for:
pickup_datetime = st.text_input('Pickup date and time', value='2024-08-30 10:00:00')
pickup_longitude = st.text_input('Pickup longitude', value=-73.950655)
pickup_latitude = st.text_input('Pickup latitude', value=40.783282)
dropoff_longitude = st.text_input('Dropoff longitude', value=-73.984365)
dropoff_latitude = st.text_input('Dropoff latitude', value=40.769802)
passenger_count = st.number_input('Passenger count', min_value=1, max_value=10, step=1)


## Once we have these, let's call our API in order to retrieve a prediction
# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
# 🤔 How could we call our API ? Off course... The `requests` package 💡

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('**Click on the Submit button to see your approximate taxi fare for your trip.**')

#2. Let's build a dictionary containing the parameters for our API...
params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

#3. Let's call our API using the `requests` package...
if st.button('Submit'):
    response = requests.get(url, params=params)
#4. Let's retrieve the prediction from the **JSON** returned by the API...
    fare = response.json()['fare']
#Finally, we can display the prediction to the user
    st.markdown(f'## Your predicted taxi fare: ${fare:.2f}')