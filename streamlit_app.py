import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('adult_Income_Classifier.pkl')

# Define the categorical values for each feature
workclass_values = ['Federal-gov', 'Local-gov', 'NA', 'Never-worked', 'Private', 
                    'Self-emp-inc', 'Self-emp-not-inc', 'State-gov', 'Without-pay']
education_values = ['10th', '11th', '12th', '1st-4th', '5th-6th', '7th-8th', 
                    '9th', 'Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Doctorate', 
                    'HS-grad', 'Masters', 'Preschool', 'Prof-school', 'Some-college']
marital_status_values = ['Divorced', 'Married-AF-spouse', 'Married-civ-spouse',
                         'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed']
occupation_values = ['Adm-clerical', 'Armed-Forces', 'Craft-repair', 'Exec-managerial',
                     'Farming-fishing', 'Handlers-cleaners', 'Machine-op-inspct', 'NA',
                     'Other-service', 'Priv-house-serv', 'Prof-specialty', 'Protective-serv',
                     'Sales', 'Tech-support', 'Transport-moving']
relationship_values = ['Husband', 'Not-in-family', 'Other-relative', 'Own-child', 
                       'Unmarried', 'Wife']
race_values = ['Amer-Indian-Eskimo', 'Asian-Pac-Islander', 'Black', 'Other', 'White']
sex_values = ['Female', 'Male']
native_country_values = ['Cambodia', 'Canada', 'China', 'Columbia', 'Cuba', 'Dominican-Republic',
                         'Ecuador', 'El-Salvador', 'England', 'France', 'Germany', 'Greece',
                         'Guatemala', 'Haiti', 'Holand-Netherlands', 'Honduras', 'Hong', 
                         'Hungary', 'India', 'Iran', 'Ireland', 'Italy', 'Jamaica', 'Japan', 
                         'Laos', 'Mexico', 'NA', 'Nicaragua', 'Outlying-US(Guam-USVI-etc)', 
                         'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto-Rico', 'Scotland',
                         'South', 'Taiwan', 'Thailand', 'Trinadad&Tobago', 'United-States', 
                         'Vietnam', 'Yugoslavia']

# Function to get index of value from categorical array
def get_index_from_array(value, array):
    if value in array:
        return array.index(value)
    else:
        return 0

# Streamlit app
def main():
    st.title('Adult Income Classifier')

    # Sidebar - Input Features
    st.header('Input Features')

    age = st.number_input('Age:', min_value=17, step=1, format='%d')
    workclass = st.selectbox('Workclass', workclass_values)
    fnlwgt = st.number_input('Final Weight', min_value=0)
    education = st.selectbox('Education', education_values)
    # education_num = st.slider('Education Number', 1, 16, 10)
    marital_status = st.selectbox('Marital Status', marital_status_values)
    occupation = st.selectbox('Occupation', occupation_values)
    relationship = st.selectbox('Relationship', relationship_values)
    race = st.selectbox('Race', race_values)
    sex = st.selectbox('Sex', sex_values)
    capital_gain = st.number_input('Capital Gain', min_value=0)
    capital_loss = st.number_input('Capital Loss', min_value=0)
    hours_per_week = st.slider('Hours per Week', 1, 99, 40)
    native_country = st.selectbox('Native Country', native_country_values)

    # Prepare input for prediction
    input_data = {
        'age': age,
        'workclass': get_index_from_array(workclass, workclass_values),
        'fnlwgt': fnlwgt,
        'education': get_index_from_array(education, education_values),
        'education_num': get_index_from_array(education, education_values),
        'marital_status': get_index_from_array(marital_status, marital_status_values),
        'occupation': get_index_from_array(occupation, occupation_values),
        'relationship': get_index_from_array(relationship, relationship_values),
        'race': get_index_from_array(race, race_values),
        'sex': sex_values.index(sex),
        'capital_gain': capital_gain,
        'capital_loss': capital_loss,
        'hours_per_week': hours_per_week,
        'native_country': get_index_from_array(native_country, native_country_values)
    }

    # Predict
    input_df = pd.DataFrame([input_data])
    if st.button('Predict'):
        prediction = model.predict(input_df)
        # Display the prediction
        st.subheader('Prediction')
        st.write(f'The predicted income class is {prediction[0]}')
        if prediction[0] == 0:
           st.write(f'The predicted income class is LESS that 50K Income.')
        else:
            st.write(f'The predicted income class is MORE that 50K Income.')

if __name__ == '__main__':
    main()