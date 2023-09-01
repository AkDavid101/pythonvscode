import streamlit as st

st.title('Age Calculator App')

name = st.text_input('Enter your name here')

yob = st.number_input("Enter your year of birth",1985,2023,value =1985)

curr = st.number_input("Enter your current year",2023,2050,value=2023)

age = curr - yob

if st.button('Check Your Age'):
    st.write(name,"you will be",age,'in',curr)

#data types
# 1.2 float
# 15 integer
# 'Jason' string 
# True Boolean