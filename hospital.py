import streamlit as st
import pandas as pd

df=pd.read_csv('hospital.csv')

def new_hospital (title,dor,first,second,last,pref,dob,selectgender,mobilephone
                ,address,email,citytown,passcode,df):
 hospital_dict={'Title':title,'Date of Registration':dor,'First Name':first,'Second Name':second
               ,'Last Name':last,'Preferred Name':pref,'Date of Birth':dob,'Gender':selectgender
               ,'Mobile Phone':mobilephone,'Address':address,'Email':email,'City/Town':citytown
               ,'Passcode':passcode}  
 hospital_df=pd.DataFrame([hospital_dict],columns=['Title','Date of Registration','First Name','Second Name'
                                                    ,'Last Name','Preferred Name','Date of Birth','Gender'
                                                    ,'Mobile Phone','Address','Email','City/Town','Passcode'])
 df=pd.concat([df,hospital_df],ignore_index=True)
 return df



st.set_page_config(layout='wide')

menu=['Patient Registration','Patients Database','Patient File']
choice=st.sidebar.selectbox('Menu',menu)

if choice=='Patient Registration':
      with st.form('Register',clear_on_submit=True):
        st.subheader('PATIENT PERSONAL DETAILS') 

        title0,dor1=st.columns(2)

        with title0:
         title1=['Mr','Mrs','Miss','Ms']
         title=st.radio('Select title',title1,horizontal=True)
        with dor1:
            dor=st.date_input('Date of Registration') 

        name1,name2=st.columns(2) 
        with name1:
            first=st.text_input('First Name') 
        with name2:
            second=st.text_input('Second Name')
        name3,name4=st.columns(2)     
        with name3:
            last=st.text_input('Last Name')
        with name4:
            pref=st.text_input('Preferred Name')

        birth,select=st.columns(2)
        with birth:
            dob=st.date_input('Date of Birth')    
        with select:
            gender=['Male','Female']         
            selectgender=st.radio('Select Gender',gender,horizontal=True)
        st.write('')

        st.subheader('PATIENT CONTACT DETAILS')

        mp,add=st.columns(2)
        with mp:
            mobilephone=st.text_input('Mobile Phone')
        with add:
            address=st.text_input('Address')

        hp,em=st.columns(2)
        with hp:
            homephone=st.text_input('Home Phone')
        with em:
            email=st.text_input('Email')
        

        ct,pas=st.columns(2)
        with ct:
            citytown=st.text_input('City/Town')
        with pas:
            passcode=st.text_input('Passcode')

        if st.form_submit_button('Register Patient'):
            df=new_hospital(title,dor,first,second,last,pref,dob,selectgender,mobilephone,address,email,citytown,passcode,df)
            df.to_csv('hospital.csv',index = False)
            st.success('Registered')   
     
if choice==  'Patients Database':    
    st.dataframe(df)  
        

          


