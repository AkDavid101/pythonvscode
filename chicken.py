#Classwork 1:
#A poultry farm sells a chicken for 10$. Create a program in Python to ask how many chickens
 #people want to get and then tell them the total price
import streamlit as st
st. title ('Chicken Sales App')
name=st.text_input('Enter your name here')
st. write('1 chicken cost 10$') 
amc=st.number_input('put the amount of chicken you want to buy',1,1000,value=1)
chicken=amc*10
if st.button('check your amount'):
     st.write(name,'you will be charged $',chicken,'for',amc,'chickens')
