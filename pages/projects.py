import streamlit as st
import os
from io import StringIO
import subprocess
import pandas as pd
import json
import xlsxwriter
import openpyxl
import glob
import shutil
from statics.css_ import *



def projects():
    sidebar_colour()
    hide_pages()

    if "project_name" not in st.session_state:
         st.session_state.project_name=""
         
    st.title("Vardhaman Projects")
    st.markdown("---")
    st.write('**Select a Project**')
    st.write("")
    image = 'images/logo.png'
    st.sidebar.image(image,use_column_width=True)
    directory="UserWorkspace"
    folder_names=os.listdir(directory)
    num_rows = len(folder_names) // 3
    num_cols = 3
    cols = st.columns(num_cols)
    project_name = None
   
    input_value = st.sidebar.text_input("Create A New Project")
    if st.sidebar.button("Create new Project",use_container_width=True):
        if input_value is not None or input_value!="" or input_value!=" ":
            project_name = input_value
            proj_dir=f"{directory}/{project_name}"
            os.makedirs(proj_dir, exist_ok=True)
            st.success(f"Project {project_name} created successfully.")
        else:
            st.error("Please enter a Project Name")




   

    for i, folder_name in enumerate(folder_names):
        column_index = i % num_cols
        column = cols[column_index]
        folder_id = f"folder_{i}"
        with column:#
            project_selected=st.button(folder_name,use_container_width=True,type="primary",key=folder_name)
            if project_selected:
                st.session_state.project_name= folder_name
                st.switch_page("pages/dashboard.py")
                

    st.write(st.session_state.project_name)

        


if __name__=="__main__":
    projects()