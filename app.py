import streamlit as st
import pickle
import pandas as pd
teams = ['New Zealand','England','South Africa','Australia','Pakistan', 'Bangladesh', 'India', 'West Indies','Sri Lanka', 'Ireland', 'Afghanistan','Zimbabwe']

cities = ['Colombo','Mirpur','Johannesburg',         
'Dhaka',                 
'Auckland',              
'Abu Dhabi',             
'Cape Town',             
'London',                
'Barbados',              
'Wellington',            
'Durban',                
'Nottingham',            
'Lauderhill',            
'Lahore',                
'St Lucia',             
'Hamilton',              
'Harare',                
'Centurion',             
'Southampton',           
'Kolkata',               
'Belfast',               
'Manchester',            
'Dubai',                 
'Sydney',                 
'Mount Maunganui',        
'Cardiff','NULL']
pipe = pickle.load(open('final_try.pkl','rb'))
st.title('T20 Win Predictor')
col1, col2 = st.columns(2)
with col1:
    team_1 = st.selectbox('Select the batting team',sorted(teams))
with col2:
    team_2 = st.selectbox('Select the bowling team',sorted(teams))
    
selected_city = st.selectbox('Select host city',sorted(cities))

if st.button('Predict Probability'):
    team1 = team_1
    team2 = team_2
    place = selected_city
    input_df = pd.DataFrame({'team_1':[team1],'team_2':[team2],'city':[selected_city]})
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(team_1 + "- " + str(round(win*100)) + "%")
    st.header(team_2 + "- " + str(round(loss*100)) + "%")
    








