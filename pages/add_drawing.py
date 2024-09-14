import streamlit as st
from datetime import date
from statics.css_ import *
from streamlit_option_menu import option_menu
import os
import json
json_file_path = 'drawings_data.json'


def add_drawinng_fun():
    
    hide_pages()
    sidebar_colour()
    
    option_menu(menu_title=None,options=[f"Add Drawing for {st.session_state.project_name}"],icons=["bi bi-window-fullscreen"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "white"},})
    
    with st.form(key='drawing_form'):
        name_of_work = st.text_input("Name of Work")
        work_date = st.date_input("Date", value=date.today())
        drawings = st.file_uploader("Drawing Upload", accept_multiple_files=True)
        col_1, col_2, col_3 = st.columns([1, 2, 1])
        
        with col_2:
            submit_button = st.form_submit_button(label='Submit', use_container_width=True, type="primary")

    if submit_button:
        # Load existing data
        data = load_data()
        print(data)

        # Collect file names
        drawing_files = [file.name for file in drawings]

        # Create a new entry
        new_entry = {
            'Name of Work': name_of_work,
            'Date': work_date.isoformat(),  # Convert date to ISO format
            'Drawings': drawing_files
        }

        # Append the new entry to existing data
        data.append(new_entry)

        # Save the updated data back to the JSON file
        save_data(data)

        # Provide feedback to the user
        st.success("Form submitted successfully!")
       

def load_data():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    return []  # Handle unexpected data format
            except (json.JSONDecodeError, ValueError):
                return []  # Handle corrupted or empty JSON
    return []

# Function to save data to the JSON file
def save_data(data):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    add_drawinng_fun()