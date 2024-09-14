import streamlit as st
from app_utils import *
import pandas as pd
from statics.css_ import *
from streamlit_option_menu import option_menu
# page_congig()

def lab_attendance():
    margin_top()
    hide_header_top()
    
    hide_pages()
    sidebar_colour()
    option_menu(menu_title=None,options=["labour Attendance"],icons=["bi bi-people"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    try:
        data = pd.read_json(f"UserWorkspace/{st.session_state.user_name_}/{st.session_state.project_name}/labour_data.json")
    except FileNotFoundError:
        st.error("Please add Labour to the Project")
    with st.container(border=True):
    # Create a DataFrame
        df = pd.DataFrame(data)

        # Add the 'Select' column with all values set to False
        df.insert(0, 'Select', False)
        st.write("Labour Details")
        edited_df = st.data_editor(df,use_container_width=True,hide_index=True)

        # Button to save the attendance (for demonstration purposes)
        col_1,col_2,col_3=st.columns([1,2,1])
        with col_2:
            if st.button("Save Attendance",use_container_width=True,type="primary"):
                st.write("Attendance saved!")
    contractors = ["Contractor A", "Contractor B", "Contractor C", "Contractor D"]

    with st.container(border=True):
        # Title of the page
        st.title("Contractor Labour Management")

        # Dropdown for selecting contractor
        contractor_name = st.selectbox("Select Contractor", contractors)

        # Numeric input for the number of laborers
        num_labours = st.number_input("Enter number of labours under contractor", min_value=0, step=1)

        # Button to record the details
        if st.button("Record Details"):
            if contractor_name and num_labours >= 0:
                st.success(f"Recorded: {contractor_name} has {num_labours} labour(s).")
            else:
                st.error("Please select a contractor and enter a valid number of labours.")

        # Display the recorded details
        if st.button("Show Recorded Details"):
            st.write(f"Contractor: {contractor_name}")
            st.write(f"Number of Labours: {num_labours}")
    
        


    



if __name__=="__main__":
    lab_attendance()