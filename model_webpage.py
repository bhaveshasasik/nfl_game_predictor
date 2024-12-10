import streamlit as st
import tensorflow as tf
import numpy as np


def load_model():
    model = tf.keras.models.load_model('best_model.h5')
    return model 

model = load_model()

st.write("""
         # NFL Victor Predictor
         """)

team_list = ['Select Team',
    'bears',
    'bengals',
    'bills',
    'broncos_data',
    'browns_data',
    'buccaneers',
    'cardinals',
    'chargers',
    'chiefs',
    'colts',
    'commanders',
    'cowboys',
    'dolphins',
    'eagles',
    'falcons',
    'giants',
    'jaguars',
    'jets',
    'lions',
    'packers',
    'panthers',
    'patriots',
    'raiders',
    'rams',
    'ravens',
    'saints',
    'seahawks',
    'steelers',
    'texans',
    'titans',
    'vikings',
    '49ers']

team_1 = st.selectbox("Team 1", team_list)
team_2 = st.selectbox("Team 2", team_list)

#def import_and_predict(image_data, model):

#    prediction = model.predict()

#    return prediction

if st.button("Predict", type="primary"):
    if team_1 == team_2:
        st.text("A team can't play against itself!")
    elif (team_1 == 'Select Team') or (team_2 == 'Select Team'):
        st.text("Please select two different teams to compete")
    else:
        output = "This is a placeholder"
        st.success(output)
    

