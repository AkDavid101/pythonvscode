import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = ['Register Staff','Staff Database']
choice = st.sidebar.selectbox('Menu',menu)

df=pd.read_csv('employeedb.csv')

def new_employee(first,last,email,selectedgender,jobtitle,dept,doe,stats,reg,df):
 employee_dict= {'First':first,'Last':last,'Email':email,'Gender':selectedgender,'Job title':jobtitle,
                 'Department':dept,'Date of Employment':doe,'Status':stats,'Registration Date':reg}
 employee_df= pd.DataFrame([employee_dict],columns=['First','Last','Email','Gender','Job title','Department',
                                                    'Date of Employment','Status','Registration Date'])
 df = pd.concat([df,employee_df],ignore_index=True)
 return df

if choice =='Register Staff':
   with st.form('Register',clear_on_submit=True):   
      name1,name2=st.columns(2)
      with name1:
        first=st.text_input('First')
      with name2:
         last=st.text_input('Last')

      eg1,eg2=st.columns(2) 

      with eg1:
         email=st.text_input('Email') 
      with eg2:
         gender=['Male','Female']
         selectedgender=st.radio('Select Gender',gender,horizontal=True)

      stat1,stat2=st.columns(2)
      with stat1:
         Jtitle=['Board  of Director','Supervisor','Senior staff','Junior staff', 'Intern']
         jobtitle=st.selectbox('Job Title',Jtitle)

      with stat2:
         department=['Accounting Dept','Enginerring Dept','Human Resources','Security Dept','Medical Dept','Tranportation Dept']
         dept=st.selectbox('Department',department)

      sd1,sd2=st.columns(2)
      with sd1:
         doe=st.date_input('Date of Employment')
      with sd2:
         status=['Part time','Full time']
      stats=st.selectbox('Status',status)

      reg=st.date_input('Registration Date') 
      if st.form_submit_button('Register'):
         df=new_employee(first,last,email,selectedgender,jobtitle,dept,doe,stats,reg,df)
         df.to_csv('employeedb.csv')
         st.success('Registered')





if choice=='Staff Database':  
   st.dataframe(df)     









   

   
