#Fashion and barber app (prices are different based on age of customer for haircut)
import streamlit as st
st.title('Barbing & Fashion') 
name=st.text_input('Enter your name')
age=st.number_input('select your age',1,120,value=1)


st.header('Barbing Styles')
bar1,bar2,bar3,bar4=st.columns(4)

bill=0
#THIS IS A RADIO OPTION TO SELECT ONE OPTION A TIME
#haircut=['Punk','Fade','Skin','Lowcut']
#selectedhaircut=st.radio('Select haircut',haircut,horizontal=True)

with bar1:
    if st.checkbox('Punk'):
        st.success('Approved')


with bar2:
    if st.checkbox('Fade'):  
     st.success('Approved')    

with bar3:
   if st.checkbox('Skin'):
      st.success('Approved') 

with bar4:
   if st.checkbox('Lowcut'):            
       st.success('Approved')


if st.button('check your bill'):
  if age <=1:
   st.write('Your service is free')

  elif(age>1) and (age<=10):
    st.write('Your bill is #1000') 

  elif(age>=11) and (age<=40):
    st.write('Your bill is #2000')

  elif(age>=41) and (age<=100):
     st.write('Your bill is #1000')

  elif(age>101):
     st.write('Your service is free')    

     


