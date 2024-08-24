import streamlit as st
from statics.css_ import *
import pandas as pd
import json
import datetime

import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Oliots ERP', page_icon='images/logo.ico',layout="wide")

def dashboard():
    hide_pages()
    sidebar_colour()
    if "overview_but" not in st.session_state:
         st.session_state.overview_but=True
    if "overview_but" not in st.session_state:
         st.session_state.overview_but=False
    # header_hide()
    st.sidebar.markdown("   ")

    image = 'images/logo.png'
    st.sidebar.image(image,use_column_width=True)
    st.sidebar.markdown("   ")

    dashboard_select=st.sidebar.selectbox("Select an option",options=["Overview","Add New Work","Labour Attendance"])
    # dashboard_overview=st.sidebar.selectbox("Overview",use_container_width=True)
    if dashboard_select =="Overview" :
        overview()
    if dashboard_select=="Add New Work":
        add_new_work()
    if dashboard_select=="Labour Attendance":
        st.switch_page("pages/labour_attendance.py")

def overview():
    st.title("Overview")
    with st.expander("All Work Details"):
        df_work=all_works()
        work_df=st.data_editor(df_work,use_container_width=True)



    col1,col2=st.columns([1,1])
    with col1:
        with st.expander("Add New Material"):
            add_new_material()
    with col2:
        with st.expander("Add New Worker"):
            add_new_worker()
    demo_graph()

def add_new_work():
    expanded_state=True
    with st.expander("Add / Delete New Work",expanded=expanded_state):
        df_work=all_works()
        st.data_editor(df_work,use_container_width=True)
        but1_col,but2_col=st.columns([1,4])
        
        with but2_col:
            with st.popover("Add New Work",use_container_width=True):
                st.markdown("Add New Work 🏗️")
                work_name = st.text_input("Enter Work Name")
                work_data = st.date_input("Select Date")
                add_work=st.button("Add New Work",use_container_width=True,type="primary")
        with but1_col:
            delete_work=st.button("🗑️",use_container_width=True)
    
    if add_work:
        expanded_state=False
        tab1, tab2 = st.tabs(["Add Work", "Work History"])
        with tab2:
            path = "database/work/material_details.txt"
            path_1="database/work/Excavation_details.txt"
            data_dict = read_and_parse_file(path)
            data_dict2 = read_and_parse_file(path_1)
            st.subheader("Material Details")
            st.data_editor(pd.DataFrame(data_dict),use_container_width=True,hide_index=True)
            st.subheader("Excavation and JCB Details")
            st.data_editor(pd.DataFrame(data_dict2),use_container_width=True,key="11",hide_index=True)
        with tab1:
            material_details()

def material_details():
    id=get_work_id()
    with st.container(border=True):
        st.subheader("Step 1: Add Material Details")
        col1,col2=st.columns([4,1])
    
        with col1:
            ard_material=st.selectbox("Vardhaman Material",options=["Option 1","Option 2","Option 3"]) # QTY with this
            mcc_material=st.selectbox("MCC Material",key="mcc",options=["Option 1","Option 2","Option 3"]) # QTY with this
        with col2:
            vard_material_qty = st.number_input("Select Quantity",min_value=1)
            mcc_material_qty = st.number_input("Select Quantity",key="mcc_qty",min_value=1)
        col_1,col_2,col_3=st.columns([1,1,1])
        # with col_2:
        #     save_prog=st.button("",use_container_width=True)
        with col_3:
            excav_prog=st.button("Save",use_container_width=True,type="primary")
            if excav_prog:
                material_details_var=str({"work_id":id+1,"vardhaman_material": ard_material,"mcc_material":mcc_material,"mcc_material_qty":mcc_material_qty})+','
                with open(f"database/work/material_details.txt",'a') as f:
                    f.write(material_details_var)
        st.markdown("---")
        excavation()
        st.markdown("---")
        additional()
                


def excavation():
    st.session_state.stage = "excavation_"
    # with st.container(border=True):
    st.subheader("Step 2: Add Excavation and JCB Details ")
    with st.container(border=True):
        col1,col2=st.columns([1,2])
    
        with col1:
            excavation_material=st.selectbox("Excavation Material",key="excavation_material",options=["Option 1","Option 2","Option 3"]) 
            excavation_len=st.number_input("Length",min_value=0.1,placeholder="m",key="exc_len")
            excavation_width=st.number_input("Width",min_value=0.1,placeholder="m",key="exc_width")
            excavation_depth=st.number_input("Depth",min_value=0.94,placeholder="m",key="exc_depth")
            with st.container(border=True):
                st.subheader("Dewatering")
                dewatering_inp = st.number_input("Select Quantity",key="dewatering_inp",min_value=1)
            
            
    # QTY with this
        with col2:
            with st.container(border=True):
                jcb_bucket_start_time=st.time_input("Start Time",value="now")
                jcb_start_photo = st.file_uploader("Upload Start Time Photo",accept_multiple_files=True)
                jcb_bucket_end_time=st.time_input("End Time",value="now")
                jcb_end_photo = st.file_uploader("Upload End Time Photo",accept_multiple_files=True)
            space_col,pre_col,next_col=st.columns([1,1,1])
            with pre_col:
                pass
                # back_prog=st.button("Previous",use_container_width=True)
            with next_col:
                additional_prog=st.button("Save",use_container_width=True,type="primary",key="jhsvdj")
            if additional_prog:
                excavation_details_var=str({"excavation_material": excavation_material,"excavation_len":excavation_len,"excavation_width":excavation_width,"excavation_depth":excavation_depth,"dewatering_inp":dewatering_inp,"jcb_bucket_start_time":jcb_bucket_start_time,"jcb_bucket_end_time":jcb_bucket_end_time})+','
                with open(f"database/work/Excavation_details.txt",'a') as f:
                    f.write(excavation_details_var)


            
            
def additional():
    st.header("Additional Details")
    site_pic = st.file_uploader("Upload Site Photos",accept_multiple_files=True)
    drawing_pic = st.file_uploader("Upload Drawing Documents",accept_multiple_files=True)
    select_labours=st.multiselect("Select labours",options=["Option 1","Option 2","Option 3"])

    #notes
    notes = st.text_area("Add Additional Notes",height=200)
    add_cols=st.columns([1,2,1])
    with add_cols[1]:
        submit_works=st.button("Save & Submit",use_container_width=True,type="primary")

def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    data_dict = eval(content)
    return data_dict

def get_work_id():
    file_path = 'database/work/material_details.txt'
    with open(file_path, 'r') as file:
        content = file.read()
        data_list = eval(f"[{content}]")
        last_element = data_list[-1]
        last_work_id = last_element['work_id']
    return last_work_id


def add_new_material():

    # Streamlit form
    with st.form(key='add_material_form'):
        # Material Name
        material_name = st.text_input("Material Name")

        # Material Type
        material_type = st.selectbox("Select Material Type", ("Type 1", "Type 2"))

        # Material Description
        material_description = st.text_area("Material Description")

        # Submit button
        submit_button = st.form_submit_button(label="Add Material")

        # Handling form submission
        if submit_button:
            st.write("New material added successfully!")
            st.write(f"Material Name: {material_name}")
            st.write(f"Material Type: {material_type}")
            st.write(f"Material Description: {material_description}")


def add_new_worker():
    with st.form(key='add_employee_form'):
        # Employee Name
        employee_name = st.text_input("Employee Name")
        
        # Employee ID
        employee_id = st.text_input("Employee ID")
        
        # Position
        position = st.text_input("Position")
        
        # Department
        department = st.selectbox("Select Department", ("HR", "Finance", "Development", "Sales", "Marketing"))
        
        # Date of Joining
        joining_date = st.date_input("Date of Joining")
        
        # Contact Number
        contact_number = st.text_input("Contact Number")
        
        # Email Address
        email_address = st.text_input("Email Address")
        
        # Submit button
        submit_button = st.form_submit_button(label="Add Employee")
        
        # Handling form submission
        if submit_button:
            st.write("New employee added successfully!")
            st.write(f"Employee Name: {employee_name}")
            st.write(f"Employee ID: {employee_id}")
            st.write(f"Position: {position}")
            st.write(f"Department: {department}")
            st.write(f"Date of Joining: {joining_date}")
            st.write(f"Contact Number: {contact_number}")
            st.write(f"Email Address: {email_address}")

def all_works():
    work_details = [
        {"Work Name": "Construction of Building A", "Date": "2024-07-30"},
        {"Work Name": "Road Repair Project", "Date": "2024-07-29"},
        {"Work Name": "Bridge Maintenance", "Date": "2024-07-28"},
        {"Work Name": "Park Landscaping", "Date": "2024-07-27"},
        {"Work Name": "Office Renovation", "Date": "2024-07-26"},
        {"Work Name": "School Expansion", "Date": "2024-07-25"}
    ]
    df_work = pd.DataFrame(work_details)

    return df_work

def demo_graph():

    work_details = [
        {"Work Name": "Construction of Building A", "Date": "2024-07-30"},
        {"Work Name": "Road Repair Project", "Date": "2024-07-29"},
        {"Work Name": "Bridge Maintenance", "Date": "2024-07-28"},
        {"Work Name": "Park Landscaping", "Date": "2024-07-27"},
        {"Work Name": "Office Renovation", "Date": "2024-07-26"},
        {"Work Name": "School Expansion", "Date": "2024-07-25"}
    ]

    labour_details = [
        {"Labour Name": "John Doe", "Work Name": "Construction of Building A", "Attendance %": 95},
        {"Labour Name": "Jane Smith", "Work Name": "Road Repair Project", "Attendance %": 88},
        {"Labour Name": "Alice Johnson", "Work Name": "Bridge Maintenance", "Attendance %": 92},
        {"Labour Name": "Bob Brown", "Work Name": "Park Landscaping", "Attendance %": 85},
        {"Labour Name": "Charlie Davis", "Work Name": "Office Renovation", "Attendance %": 90},
        {"Labour Name": "Diana White", "Work Name": "School Expansion", "Attendance %": 87}
    ]

    # Convert to DataFrames
    df_work = pd.DataFrame(work_details)
    df_labour = pd.DataFrame(labour_details)

    # Merge DataFrames on 'Work Name'
    df_combined = pd.merge(df_labour, df_work, on="Work Name")

    # Streamlit App
    st.write("Labour Data Visualizations")

    # Plotting
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Histogram
    sns.histplot(df_combined["Attendance %"], kde=True, bins=10, color="skyblue", ax=axes[0, 0])
    axes[0, 0].axvline(df_combined["Attendance %"].mean(), color="black", linestyle="--", linewidth=2, label=f"Mean: {df_combined['Attendance %'].mean():.1f}")
    axes[0, 0].set_title("Histogram of Labour Attendance Percentages")
    axes[0, 0].set_xlabel("Attendance Percentage")
    axes[0, 0].set_ylabel("Frequency")
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    # Bar Chart
    sns.barplot(x="Work Name", y="Attendance %", data=df_combined, palette="viridis", ax=axes[0, 1])
    axes[0, 1].set_title("Bar Chart of Labour Attendance Percentages by Work")
    axes[0, 1].set_xlabel("Work Name")
    axes[0, 1].set_ylabel("Attendance Percentage")
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].grid(True)

    # Scatter Plot
    sns.scatterplot(x="Date", y="Attendance %", hue="Labour Name", data=df_combined, palette="viridis", ax=axes[1, 0])
    axes[1, 0].set_title("Scatter Plot of Attendance % by Date")
    axes[1, 0].set_xlabel("Date")
    axes[1, 0].set_ylabel("Attendance Percentage")
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].grid(True)

    # Box Plot
    sns.boxplot(x="Work Name", y="Attendance %", data=df_combined, palette="Set2", ax=axes[1, 1])
    axes[1, 1].set_title("Box Plot of Labour Attendance Percentages by Work")
    axes[1, 1].set_xlabel("Work Name")
    axes[1, 1].set_ylabel("Attendance Percentage")
    axes[1, 1].tick_params(axis='x', rotation=45)
    axes[1, 1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)



if __name__=="__main__":
    dashboard()