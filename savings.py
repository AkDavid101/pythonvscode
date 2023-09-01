#Classwork 1
#Create a python program for daily savings for a user, add up all his savings from sunday to saturday

import streamlit as st
st.title('Savings app')
name=st. text_input('Enter your name')
target=st. number_input('Enter your savings goal',1,1000000,value=1)

suns=st.number_input('Enter your Sunday savings',1,value=1)
mons=st.number_input('Enter Monday savings',1,value=1)
tues=st.number_input('Enter Tuesday savings',1,value=1)
weds=st.number_input('Enter Wednesday savings',1,value=1)
thus=st.number_input('Enter Thursday savings',1,value=1)
fris=st.number_input('Enter Friday savings',1,value=1)
sats=st.number_input('Enter Saturday savings',1,value=1)

savings=(suns+mons+tues+weds+thus+fris+sats)
left=target-savings
passed = savings-target

if st. button('Check how much you saved'):
    if target > savings:
        st.error(f"{name} you have saved ${savings} you are {left} away from your goal")
    elif savings > target:
        st.success(f'{name} you have saved ${savings} you have {passed} extra')