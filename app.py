import streamlit as st
from dotenv import load_dotenv
import base64
import os
import time
from pathlib import Path
from statics.css_ import *
from app_utils import *

st.set_page_config(page_title='Oliots ERP', page_icon='images/logo.ico')



def app():
    image_path = f"{IMAGES}{LOGO_IMAGE}"
    space1,logo_space,space2=st.columns([20,60,20])
    with logo_space:
        st.image(image_path,use_column_width=True) 
        st.markdown("""<center><h1 style="color: teal;">Sign in to Workspace</h1></center>""",unsafe_allow_html=True)
    with st.container(border=True):
        pad_left,content,pad_right=st.columns([10,80,10])
        with content:
            st.markdown("""<div style="height: 20px;"></div>""",unsafe_allow_html=True)
            username_inp=st.text_input("Username")
            password_inp=st.text_input("Password")
            login_butt=st.button("Login",use_container_width=True,type="primary")
            st.markdown("""<div style="height: 20px;"></div>""",unsafe_allow_html=True)


    if login_butt:
        st.switch_page("pages/projects.py")



if __name__=="__main__":
    app()