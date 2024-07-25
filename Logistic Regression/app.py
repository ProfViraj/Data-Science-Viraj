# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:49:13 2024

@author: viraj
"""

import pickle
import streamlit as st

# open model in read binary mode
load = open('classifier.pkl','rb')
model = pickle.load(load)

# Define predict function
def predict(Pclass, Age, SibSp, Parch, Fare, Sex_female, Sex_male, Embarked_C, Embarked_Q, Embarked_S):
    prediction = model.predict([[Pclass, Age, SibSp, Parch, Fare, Sex_female, Sex_male, Embarked_C, Embarked_Q, Embarked_S]])
    return prediction

def main():
    st.title('Logistic Regression Model for Titanic')
    
    #Accepting values from user through the browser
    Pclass = st.number_input('Select ticket class:', min_value=1, max_value=3, step=1)
    Age = st.number_input('Select age:',min_value=0.00, max_value=100.00)
    SibSp = st.number_input('Enter number of siblings/spouse along with the person:',min_value=0, max_value=10, step=1)
    Parch = st.number_input('Enter number of parents/children along with the person:',min_value=0, max_value=10, step=1)
    Fare = st.number_input('Enter the fare:',min_value=0.00, max_value=520.00)
    
    Gender = st.selectbox('Select gender:',('male','female'))
    if Gender == 'male':
        Sex_male = 1
        Sex_female = 0
    elif Gender == 'female':
        Sex_male = 0
        Sex_female = 1
    
    Embark = st.selectbox('Select the departure port:',('Southampton', 'Cherbourg', 'Queenstown'))
    if Embark == 'Southampton':
        Embarked_S = 1
        Embarked_C = Embarked_Q = 0
    elif Embark == 'Cherbourg':
        Embarked_C = 1
        Embarked_S = Embarked_Q = 0
    elif Embark == 'Queenstown':
        Embarked_Q = 1
        Embarked_S = Embarked_C = 0
        
    if st.button('Predict'):
        result = predict(Pclass, Age, SibSp, Parch, Fare, Sex_female, Sex_male, Embarked_C, Embarked_Q, Embarked_S)
        if result == 0:
            st.success('Person might not have survived.')
        else:
            st.success('Person might have survived.')
            
if __name__ == '__main__':
    main()