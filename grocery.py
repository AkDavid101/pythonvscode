import streamlit as st 

st.title('Grocery')

st.subheader('Dairy')
bill=0

dairy1,dairy2,dairy3,dairy4=st.columns(4)
with dairy1:
    if st.checkbox('Milk'):
        bill +=10
        st.success('Added to cart')

with dairy2:
    if st.checkbox('Blue Cheese'):
        bill +=20
        st.success('Added to cart')
    if st.checkbox('Cheddar'):
        bill +=20
        st.success('Added to cart')    

with dairy3:
    if st.checkbox('Butter'):
        bill +=10
        st.success('Added to cart')                

with dairy4:
    if st.checkbox('Youghurt'):
        bill +=15
        st.success('Added to cart')


st.subheader('Fruits')
fruit1,fruit2,fruit3,fruit4=st.columns(4)
with fruit1:
  if st.checkbox('Apple'):
   bill +=2.5
   st.success('Added to cart')

with fruit2:
  if st.checkbox('Grapes'):
   fruit2=st.number_input('amount to buy',0,500,value=1)
   bill+=1.5*fruit2
   st.success('Added to cart')

with fruit3:
  if st.checkbox('Watermelon'):
    fruit3=st.number_input('amount to buy',0,500,value=1)
    bill+=3.5*fruit3
    st.success('Added to cart')

with fruit4:
  if st.checkbox('Bannana'):
    fruit4=st.number_input('amount to buy',0,500,value=1)
    bill+=1.5*fruit4
    st.success('Added to cart')  

food1,food2,food3,food4=st.columns(4)
     

    