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
from app_utils import *



def projects():
    sidebar_colour()
    hide_pages()
    hide_header_top()

    if "project_name" not in st.session_state:
         st.session_state.project_name=""

    st.write(st.session_state.user_name_)
         
    st.title("Vardhaman Projects")
    st.markdown("---")
    st.write('**Select a Project**')
    st.write("")
    image = 'images/logo.png'
    st.sidebar.image(image,use_column_width=True)
    directory=f"UserWorkspace/{st.session_state.user_name_}"
    folder_names=os.listdir(directory)
    # st.write(directory)
    num_rows = len(folder_names) // 3
    num_cols = 3
    cols = st.columns(num_cols)
    project_name = None
   
        

    

                

    with st.sidebar:
        with st.container(border=True):

            # Use HTML and CSS to set text color to white
            st.markdown(
                """
                <div style="color: white; padding-bottom: 10px;">
                    Select User Action
                </div>
                """,
                unsafe_allow_html=True
            )

            user_action=st.selectbox("",options=["Create a New Project","Add New User","Edit Existing User","Delete Existing User"],label_visibility="collapsed",placeholder="None")
        
        # with st.container(border=True):
            st.markdown("---")
            if user_action=="Create a New Project":
            
                    st.markdown(
                        """
                        <div style="color: white; padding-bottom: 10px;">
                            Create A New Project
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    input_value = st.text_input("Create A New Project",label_visibility="collapsed")
                    if st.button("Create new Project",use_container_width=True):
                        if input_value is not None or input_value!="" or input_value!=" ":
                            project_name = input_value
                            proj_dir=f"{directory}/{project_name}"
                            st.write(directory)
                            os.makedirs(proj_dir, exist_ok=True)
                            st.success(f"Project {project_name} created successfully.")
                            st.rerun()
                        else:
                            st.error("Please enter a Project Name")
                    # st.rerun()
            elif user_action =="Add New User":
                st.header('Create User')
                username = st.text_input('Username')
                password = st.text_input('Password', type='password')
                role = st.selectbox('Role', ['Superadmin', 'Admin', 'Team Member'])
                if st.button('Create User',use_container_width=True):
                    if create_user(username, password, role):
                        st.success('User created successfully')
                    else:
                        st.error('User already exists')
            elif user_action =="Edit Existing User":
                st.header('Edit User')
                users = load_users()
                if users:
                    usernames = list(users.keys())
                    selected_user = st.selectbox('Select User', [''] + usernames)
                    if selected_user:
                        new_password = st.text_input('New Password', type='password')
                        new_role = st.selectbox('New Role', ['Superadmin', 'Admin', 'Team Member'], index=['Superadmin', 'Admin', 'Team Member'].index(users[selected_user]['role']))
                        if st.button('Edit User',use_container_width=True):
                            if edit_user(selected_user, new_password, new_role):
                                st.success('User details updated successfully')
                            else:
                                st.error('Failed to update user details')
                else:
                    st.info('No users found')
            elif user_action =="Delete Existing User":
                users = load_users()
                usernames = list(users.keys())
                st.header('Delete User')
                username = st.selectbox('Select Username', [''] + usernames)
                if st.button('Delete User',use_container_width=True):
                    if delete_user(username):
                        st.success('User deleted successfully')
                    else:
                        st.error('User not found')

    for i, folder_name in enumerate(folder_names):
        column_index = i % num_cols
        column = cols[column_index]
        folder_id = f"folder_{i}"
        with column:#
            project_selected=st.button(folder_name,use_container_width=True,type="primary",key=folder_name)
            if project_selected:
                st.session_state.project_name= folder_name
                st.switch_page("pages/dashboard.py")



        


if __name__=="__main__":
    projects()