import streamlit as st
from app_utils import *
import pandas as pd
from statics.css_ import *
# page_congig()

def lab_attendance():
    hide_pages()
    sidebar_colour()
    st.sidebar.markdown("   ")

    image = 'images/logo.png'
    st.sidebar.image(image,use_column_width=True)
    st.sidebar.markdown("   ")

    dashboard_select=st.sidebar.selectbox("Select an option",options=["Labour Attendance","Overview","Add New Work","Add Drawing","Stock List"])
    # dashboard_overview=st.sidebar.selectbox("Overview",use_container_width=True)
    if dashboard_select =="Overview" :
       st.switch_page("pages/dashboard.py")
    elif dashboard_select=="Add New Work":
        st.switch_page("pages/dashboard.py")
    elif dashboard_select=="Labour Attendance":
        main_attend()
    elif dashboard_select=="Add Drawing":
        st.switch_page("pages/add_drawing.py")
    elif dashboard_select=="Stock List":
        st.switch_page("pages/stock_list.py")
        

def main_attend():
    
    data = {
    "Name": ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"],
    "Role": ["Electrician", "Plumber", "Carpenter", "Painter"],
    "Hours Worked": [8, 7.5, 8, 6]
    }
    with st.container(border=True):
        st.title("Labour Attendance")
    # Create a DataFrame
        df = pd.DataFrame(data)

        # Add the 'Select' column with all values set to False
        df.insert(0, 'Select', False)

        # Title of the page
        

        # Display the DataFrame in a table
        st.write("Labour Details")
        edited_df = st.data_editor(df,use_container_width=True)

        # Button to save the attendance (for demonstration purposes)
        if st.button("Save Attendance",use_container_width=True,type="primary"):
            st.write("Attendance saved!")

    # Title of the page
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