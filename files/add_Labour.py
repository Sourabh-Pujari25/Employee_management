import streamlit as st
import json
import os

# Define the path for the JSON file
json_file_path = f'UserWorkspace/{st.session_state.user_name_}/{st.session_state.project_name}/labour_data.json'

# Function to load existing data from the JSON file
def load_data():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save data to the JSON file
def save_data(data):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to get the next Labour ID
def get_next_labour_id(data):
    prefix = "LB-"
    base_number = 1

    # Find the highest current ID
    max_id = base_number - 1
    for record in data:
        emp_id = record.get('Employee ID', '')
        if emp_id.startswith(prefix):
            try:
                number_part = int(emp_id[len(prefix):])
                if number_part > max_id:
                    max_id = number_part
            except ValueError:
                pass

    # Generate the next ID
    next_id_number = max_id + 1
    next_id = f"{prefix}{next_id_number:03d}"
    return next_id

def add_new_worker():
    # Load existing data
    data = load_data()

    # Get the next Labour ID
    next_labour_id = get_next_labour_id(data)

    # Create form for employee details
    with st.form(key='add_labour_form'):
        employee_id = st.text_input("Labour ID", value=next_labour_id, disabled=True)
        employee_name = st.text_input("Labour Name")
        job_role = st.text_input("Enter Job Role")
        joining_date = st.date_input("Date of Joining")
        contact_number = st.text_input("Contact Number")
        email_address = st.text_input("Email Address")
        col_1,col_2_,col_3=st.columns([1,2,1])
        with col_2_:
            submit_button = st.form_submit_button(label="Add Employee",use_container_width=True,type="primary")

        if submit_button:
            # Create a new employee record
            new_employee = {
                'Employee ID': next_labour_id,
                'Name': employee_name,
                'Job Role': job_role,
                'Date of Joining': joining_date.isoformat(),  # Convert date to ISO format
                'Contact Number': contact_number,
                'Email Address': email_address
            }

            # Append the new record to existing data
            data.append(new_employee)

            # Save the updated data back to the JSON file
            save_data(data)

            # Provide feedback to the user
            st.success("Employee added successfully!")
            st.rerun()
