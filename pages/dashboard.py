import streamlit as st
from statics.css_ import *
import pandas as pd
import json
import datetime
from statics.css_ import *
import matplotlib.pyplot as plt
import seaborn as sns
import os
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Oliots ERP', page_icon='images/logo.ico',layout="wide")

def dashboard():
    if "user_name_" not in st.session_state:
         st.session_state.user_name_=st.session_state.user_name_
    if 'add_work_butt' not in st.session_state:
        st.session_state.add_work_butt = False
    
    hide_pages()
    sidebar_colour()
    hide_header_top()
    padding_page_top()
    # st.write(st.session_state.user_name_)
    if "overview_but" not in st.session_state:
         st.session_state.overview_but=True
    if "overview_but" not in st.session_state:
         st.session_state.overview_but=False
    # header_hide()
    st.sidebar.markdown("   ")

    image = 'images/logo.png'
    st.sidebar.image(image,use_column_width=True)
    st.sidebar.markdown("   ")

    st.sidebar.markdown(
                """
                <div style="color: white; padding-bottom: 10px;">
                    Select User Action
                </div>
                """,
                unsafe_allow_html=True
            )

    dashboard_select=st.sidebar.selectbox("Select an option",options=["Overview","Add New Work","Labour Attendance","Add Drawing","Stock List"],label_visibility="collapsed")
    # dashboard_overview=st.sidebar.selectbox("Overview",use_container_width=True)
    if dashboard_select =="Overview" :
        overview()
    elif dashboard_select=="Add New Work":
        add_new_work()
    elif dashboard_select=="Labour Attendance":
        st.switch_page("pages/labour_attendance.py")
    elif dashboard_select=="Add Drawing":
        st.switch_page("pages/add_drawing.py")
    elif dashboard_select=="Stock List":
        st.switch_page("pages/stock_list.py")

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
    
    st.session_state.work_data_save_path=f"UserWorkspace/{st.session_state.user_name_}/{st.session_state.project_name}"
    # st.write(work_data_save_path)
    option_menu(menu_title=None,options=["Add New Work 🏗️"],icons=["bi bi-cone-striped"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    with st.container(border=True):
        # df_work=all_works()
        # st.data_editor(df_work,use_container_width=True)

        work_name_col,work_date_col=st.columns([2,2])
        with work_name_col:
            st.session_state.work_name = st.text_input("Enter Work Name")
        with work_date_col:
            st.session_state.work_date = st.date_input("Select Date")
    
    
    st.session_state.add_work_butt = True
    # expanded_state=False
    

    st.session_state.add_work_butt = False
    option_menu(menu_title=None,options=["Work Details"],key="title",icons=["bi bi-pencil"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    with st.container(border=True):
        st.subheader("Step 1: Add Material Details")
        col1,col2=st.columns([4,1])
    
        with col1:
                st.session_state.vard_material=st.selectbox("Vardhaman Material",options=["Option 1","Option 2","Option 3"]) #QTY with this
                st.session_state.mcc_material=st.selectbox("MCC Material",key="mcc",options=["Option 1","Option 2","Option 3"])# QTY with this
        with col2:
            st.session_state.vard_material_qty = st.number_input("Select Quantity",min_value=1)
            st.session_state.mcc_material_qty = st.number_input("Select Quantity",key="mcc_qty",min_value=1)
        col_1,col_2,col_3=st.columns([1,1,1])
        # with col_2:
        #     save_prog=st.button("",use_container_width=True)
        # with col_3:
            # excav_prog=st.button("Save",use_container_width=True,type="primary")
            # if excav_prog:
                #     material_details_var=str({"work_id":id+1,"vardhaman_material": ard_material,"mcc_material":mcc_material"mcc_material_qty":mcc_material_qty})+','
            #     with open(f"database/work/material_details.txt",'a') as f:
            #         f.write(material_details_var)
        st.markdown("---")
        excavation()
        st.markdown("---")
        additional()
    option_menu(menu_title=None,options=["Previous Work"],key="title_Pw",icons=["bi bi-pencil"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    with st.container(border=True):

        with open(f"{st.session_state.work_data_save_path}/work_data.json","r") as f:
            json_data=f.read()


        data = json.loads(json_data)

        df = pd.json_normalize(data)
        st.data_editor(df,hide_index=True)
                        


def excavation():
    st.session_state.stage = "excavation_"
    # with st.container(border=True):
    st.subheader("Step 2: Add Excavation and JCB Details ")
    with st.container(border=True):
        col1,col2=st.columns([1,2])
    
        with col1:
            st.session_state.excavation_material=st.selectbox("Excavation Material",key="excavation__material",options=["Option 1","Option 2","Option 3"]) 
            st.session_state.excavation_len=st.number_input("Length",min_value=0.1,placeholder="m",key="exc_len")
            st.session_state.excavation_width=st.number_input("Width",min_value=0.1,placeholder="m",key="exc_width")
            st.session_state.excavation_depth=st.number_input("Depth",min_value=0.94,placeholder="m",key="exc_depth")
            with st.container(border=True):
                st.subheader("Dewatering")
                st.session_state.dewatering_inp = st.number_input("Select Quantity",key="dewatering_inp__",min_value=1)
            
            
    # QTY with this
        with col2:
            with st.container(border=True):
                st.subheader("JCB Bucket Details")
                st.session_state.jcb_bucket_start_time=st.time_input("Start Time",value="now")
                st.session_state.jcb_start_photo = st.file_uploader("Upload Start Time Photo")
                st.session_state.jcb_bucket_end_time=st.time_input("End Time",value="now")
                st.session_state.jcb_end_photo = st.file_uploader("Upload End Time Photo")
                with st.expander("JCB Breaker Details"):
                    st.subheader("JCB Breaker Details")
                    st.session_state.jcb_breaker_start_time=st.time_input("Start Time",value="now",key="breaker 01")
                    st.session_state.jcb_breaker_start_photo = st.file_uploader("Upload Start Time Photo",key="breaker 02")
                    st.session_state.jcb_breaker_bucket_end_time=st.time_input("End Time",value="now",key="breaker 03")
                    st.session_state.jcb_breaker_end_photo = st.file_uploader("Upload End Time Photo",key="breaker 04")
            # space_col,pre_col,next_col=st.columns([1,1,1])
            # with pre_col:
            #     pass
                # back_prog=st.button("Previous",use_container_width=True)
            # with next_col:
            #     additional_prog=st.button("Save",use_container_width=True,type="primary",key="jhsvdj")
            # if additional_prog:
            #     excavation_details_var=str({"excavation_material": excavation_material,"excavation_len":excavation_len,"excavation_width":excavation_width,"excavation_depth":excavation_depth,"dewatering_inp":dewatering_inp,"jcb_bucket_start_time":jcb_bucket_start_time,"jcb_bucket_end_time":jcb_bucket_end_time})+','
            #     with open(f"database/work/Excavation_details.txt",'a') as f:
            #         f.write(excavation_details_var)


            
            
def additional():
    st.header("Additional Details")
    st.session_state.site_pic = st.file_uploader("Upload Site Photos",accept_multiple_files=True)
    st.session_state.drawing_pic = st.file_uploader("Upload Drawing Documents",accept_multiple_files=True)
    st.session_state.select_labours=st.multiselect("Select labours",options=["Option 1","Option 2","Option 3"])

    #notes
    st.session_state.notes = st.text_area("Add Additional Notes",height=200)
    add_cols=st.columns([1,2,1])
    with add_cols[1]:
        submit_works=st.button("Save & Submit",use_container_width=True,type="primary")
    
    if submit_works:
        work_id = get_next_work_id()
        work_data = {
            'Work ID': work_id,
            'Name of Work': st.session_state.work_name,
            'Date': str(st.session_state.work_date),
            'Vardhaman Material': {'items': st.session_state.vard_material, 'quantity': st.session_state.vard_material_qty},
            'MMC Material': {'items': st.session_state.mcc_material, 'quantity': st.session_state.mcc_material_qty},
            'Excavation': {
                'Length': st.session_state.excavation_len,
                'Width': st.session_state.excavation_width,
                'Depth': st.session_state.excavation_depth,
                'Material': st.session_state.excavation_material,
            },
            'JCB Bucket': {
                'Start Time': str(st.session_state.jcb_bucket_start_time),
                'Stop Time': str(st.session_state.jcb_bucket_end_time),
                'Start Photo': st.session_state.jcb_start_photo.name if st.session_state.jcb_start_photo else None,
                'Stop Photo': st.session_state.jcb_end_photo.name if st.session_state.jcb_end_photo else None
            },
            'JCB Breaker': {
                'Start Time': str(st.session_state.jcb_breaker_start_time),
                'Stop Time':  str(st.session_state.jcb_breaker_bucket_end_time),
                'Start Photo': st.session_state.jcb_breaker_start_photo.name if st.session_state.jcb_breaker_start_photo else None,
                'Stop Photo': st.session_state.jcb_breaker_end_photo.name if st.session_state.jcb_breaker_end_photo else None
            },
            'Dewatering': st.session_state.dewatering_inp,
            'Site Photos': [file.name for file in st.session_state.site_pic] if st.session_state.site_pic else [],
            'Drawing Upload': [file.name for file in st.session_state.drawing_pic] if st.session_state.drawing_pic else [],
            'Labour': st.session_state.select_labours,
            'Additional Notes': st.session_state.notes
        }

        existing_data = load_existing_data()
        existing_data.append(work_data)

        with open(f'{st.session_state.work_data_save_path}/work_data.json', 'w') as file:
            json.dump(existing_data, file, indent=4)

        st.success('Work details saved successfully!')

    


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    data_dict = eval(content)
    return data_dict

def get_next_work_id():
    """Generate the next Work ID based on the latest entry in the JSON file."""
    file_path = f'{st.session_state.work_data_save_path}/work_data.json'
    if not os.path.exists(file_path):
        return 'WID_001'

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        return 'WID_001'

    if not data:
        return 'WID_001'

    # Extract the latest Work ID
    try:
        latest_id = max(item['Work ID'] for item in data)
        number = int(latest_id.split('_')[1])
        new_number = number + 1
        return f'WID_{new_number:03}'
    except KeyError:
        return 'WID_001'

def load_existing_data():
    """Load existing work data from JSON file."""
    file_path = f'{st.session_state.work_data_save_path}/work_data.json'
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []



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