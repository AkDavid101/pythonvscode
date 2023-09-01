"""
-Add a restaurant picture
-Create a restaurant app that welcomes users and shows them the food selections
-If they choose/select their meals, show them the total amount
-Ask a question if you want to share the bill with others #use checkbox
-if yes, then ask how many people want to share the bill
-Then show the amount each person must contribute to pay the bill
"""

import streamlit as st
st.set_page_config(layout='wide')
st.title('Pay n Eat Restaurant')
st.write('...satisfaction at your service')
st.image('https://cdn.pixabay.com/photo/2017/09/23/12/40/catering-2778755_1280.jpg')

st.title('Meal')
meal1,meal2,meal3,meal4=st.columns(4)

bill=0

with meal1:
    if st.checkbox('Ofada Rice: #3000'):
     bill +=3000
     st.success('Added to Menu')


with meal2:
   if st.checkbox('Jolof Rice & Chicken: #2500'):
      bill +=2500
      st.success('Added to Menu')

with meal3:
   if st.checkbox('Fried Rice & Plantain: #4500'):
      bill +=4500
      st.success('Added to Menu')

with meal4:
   if st.checkbox('Coconut Rice: #1500'):
      bill +=1500
      st.success('Added to Menu')



st.title('Salad')
salad1,salad2,salad3,salad4=st.columns(4)


with salad1:
   if st.checkbox('Coleslaw: #500'):
      bill +=500
      st.success('Added to Menu')

with salad2:
   if st.checkbox('Green Salad: #1500'):
      bill +=1500
      st.success('Added to Menu')

with salad3:
   if st.checkbox('Red Cabbage: #2600'):
      bill +=2600
      st.success('Added to Menu')

with salad4:
   if st.checkbox('Fruit Salad: #3000'):
      bill +=3000
      st.success('Added to Menu') 


st.title('Fast Foods')
fastfood1,fastfood2,fastfood3,fastfood4=st.columns(4)


with fastfood1:
   if st.checkbox('Burger: #4500 '):
      bill +=4500
      st.success('Added to Menu')


with fastfood2:
   if st.checkbox('Sharwamma: #1000 '):
      bill +=1000
      st.success('Added to Menu')


with fastfood3:
   if st.checkbox('Pizza: #6500 '):
      bill +=6500
      st.success('Added to Menu')
                                 

with fastfood4:
   if st.checkbox('Hot Dog: #2500 '):
      bill +=2500
      st.success('Added to Menu')



st.title('Drinks')
drinks1,drinks2,drinks3,drinks4=st.columns(4)


with drinks1:
   if st.checkbox('Fanta: #250'):
      bill +=250
      st.success('Added to Menu')

with drinks2:
   if st.checkbox('Water: #650'):
      bill +=650
      st.success('Added to Menu')

with drinks3:
   if st.checkbox('Coke: #250'):
      bill +=250
      st.success('Added to Menu')

with drinks4:
   if st.checkbox('Chapman: #1000'):
      bill +=1000
      st.success('Added to Menu') 
   



if st.button('Check your bill'):
   st.header(f'The total bill is #{bill}')

people1,people2=st.columns(2)
with people1:
      if st.checkbox('Click to share the bill with others'):

         people = st.slider('How many people in total',2,100,value=2)
         person = bill/people
         st.header(f'Each person will have to pay ${person}')
      


     



      





     

