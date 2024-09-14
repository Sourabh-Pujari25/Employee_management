
import streamlit as st
import json
import os

from app_utils import *
# Streamlit app
def main():
    st.title('User Management System')

    menu = st.sidebar.selectbox('Menu', ['Login', 'Create User', 'Delete User', 'Edit User'])

    if menu == 'Login':
        st.header('Login')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            role = check_credentials(username, password)
            if role:
                st.success(f'Logged in as {role}')
            else:
                st.error('Invalid credentials')

    elif menu == 'Create User':
        st.header('Create User')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        role = st.selectbox('Role', ['Superadmin', 'Admin', 'Team Member'])
        if st.button('Create User'):
            if create_user(username, password, role):
                st.success('User created successfully')
            else:
                st.error('User already exists')

    elif menu == 'Delete User':
        st.header('Delete User')
        username = st.text_input('Username')
        if st.button('Delete User'):
            if delete_user(username):
                st.success('User deleted successfully')
            else:
                st.error('User not found')

    elif menu == 'Edit User':
        st.header('Edit User')
        users = load_users()
        if users:
            usernames = list(users.keys())
            selected_user = st.selectbox('Select User', [''] + usernames)
            if selected_user:
                new_password = st.text_input('New Password', type='password')
                new_role = st.selectbox('New Role', ['Superadmin', 'Admin', 'Team Member'], index=['Superadmin', 'Admin', 'Team Member'].index(users[selected_user]['role']))
                if st.button('Edit User'):
                    if edit_user(selected_user, new_password, new_role):
                        st.success('User details updated successfully')
                    else:
                        st.error('Failed to update user details')
        else:
            st.info('No users found')

if __name__ == "__main__":
    main()
