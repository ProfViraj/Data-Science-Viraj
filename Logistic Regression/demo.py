# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st

name = st.text_input('Enter your name','')
job = st.text_area('What do you do?')
age = st.number_input('Select your age:',min_value=1, max_value=60)

if name!='':
    st.markdown(
                f"""
                * Name : {name}
                * Job : {job}
                * Age : {age}
                """
                )

is_available_for_work = st.checkbox('Available for work?')

st.write(is_available_for_work)

threshold = st.slider("Pick a threshold",min_value=1.0, max_value=100.0,value=50.0,step=0.5)
st.write(threshold)
#import pandas as pd

#df=pd.read_csv('Titanic_train.csv')
#st.line_chart(df['Survived'])

st.title('Logistic Regression Model :chart_with_upwards_trend:')
st.markdown('This is my logistic regression web application :computer:')
st.text('Logistic Regression')

st.selectbox('Select your city',('Pune','Mumbai','Delhi','Nashik'))

