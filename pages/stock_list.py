import streamlit as st
import pandas as pd
from datetime import date
from statics.css_ import *


def stock_list_fun():
    hide_pages()
    sidebar_colour()
    st.sidebar.markdown("   ")

    image = 'images/logo.png'
    st.sidebar.image(image,use_column_width=True)
    st.sidebar.markdown("   ")

    dashboard_select=st.sidebar.selectbox("Select an option",options=["Stock List","Add New Work","Labour Attendance","Add Drawing","Overview"])
    # dashboard_overview=st.sidebar.selectbox("Overview",use_container_width=True)
    
    if dashboard_select=="Stock List":
       stokk()
    elif dashboard_select =="Overview" :
        st.switch_page("pages/dashboard.py")
    elif dashboard_select=="Add New Work":
        st.switch_page("pages/dashboard.py")
    elif dashboard_select=="Labour Attendance":
        st.switch_page("pages/labour_attendance.py")
    elif dashboard_select=="Add Drawing":
        st.switch_page("pages/add_drawing.py")

def stokk():   
    # Initialize session state to store data
    if 'available_stock' not in st.session_state:
        st.session_state.available_stock = pd.DataFrame(columns=["Sr.No", "Date", "Item Name", "Size", "Godown Name", "Vendor Name"])
    if 'used_stock' not in st.session_state:
        st.session_state.used_stock = pd.DataFrame(columns=["Sr.No", "Date", "Item Name", "Size", "Godown Name", "Vendor Name", "Name of Project", "Name of Work", "Sr.No of Work"])

   # Sample data for dropdowns
    godowns = ["Godown A", "Godown B", "Godown C"]
    vendors = ["Vendor X", "Vendor Y", "Vendor Z"]

    st.title("Stock List")

    # Tabs
    tab1, tab2, tab3 = st.tabs(["Show Available Stock", "Show Used Stock", "Add New Stock"])

    with tab1:
        st.header("Show Available Stock")
        with st.form(key='available_stock_form'):
            sr_no = st.text_input("Sr.No")
            stock_date = st.date_input("Date", value=date.today())
            item_name = st.text_input("Item Name")
            size = st.text_input("Size")
            godown_name = st.text_input("Godown Name")
            vendor_name = st.text_input("Vendor Name")
            submit_available = st.form_submit_button(label='Add to Available Stock')
        
        if submit_available:
            new_entry = {
                "Sr.No": sr_no,
                "Date": stock_date,
                "Item Name": item_name,
                "Size": size,
                "Godown Name": godown_name,
                "Vendor Name": vendor_name
            }
            st.session_state.available_stock = st.session_state.available_stock.append(new_entry, ignore_index=True)
        
        st.subheader("Available Stock Data")
        st.dataframe(st.session_state.available_stock,use_container_width=True,hide_index=True)

    with tab2:
        st.header("Show Used Stock (Admin Only)")
        with st.form(key='used_stock_form'):
            sr_no = st.text_input("Sr.No")
            used_date = st.date_input("Date", value=date.today())
            item_name = st.text_input("Item Name")
            size = st.text_input("Size")
            godown_name = st.text_input("Godown Name")
            vendor_name = st.text_input("Vendor Name")
            project_name = st.text_input("Name of Project")
            work_name = st.text_input("Name of Work")
            work_sr_no = st.text_input("Sr.No of Work")
            submit_used = st.form_submit_button(label='Add to Used Stock')
        
        if submit_used:
            new_entry = {
                "Sr.No": sr_no,
                "Date": used_date,
                "Item Name": item_name,
                "Size": size,
                "Godown Name": godown_name,
                "Vendor Name": vendor_name,
                "Name of Project": project_name,
                "Name of Work": work_name,
                "Sr.No of Work": work_sr_no
            }
            st.session_state.used_stock = st.session_state.used_stock.append(new_entry, ignore_index=True)
        
        st.subheader("Used Stock Data")
        st.dataframe(st.session_state.used_stock,use_container_width=True,hide_index=True)

    with tab3:
        st.header("Add New Stock")
        with st.form(key='new_stock_form'):
            sr_no = st.text_input("Sr.No")
            new_stock_date = st.date_input("Date", value=date.today())
            item_name = st.text_input("Item Name")
            size = st.text_input("Size")
            
            godown_name = st.selectbox("Select Godown Name", options=["Other"] + godowns)
            if godown_name == "Other":
                godown_name = st.text_input("Enter Other Godown Name")
            
            vendor_name = st.selectbox("Select Vendor Name", options=["Other"] + vendors)
            if vendor_name == "Other":
                vendor_name = st.text_input("Enter Other Vendor Name")
            
            submit_new_stock = st.form_submit_button(label='Add to New Stock')
        
        if submit_new_stock:
            new_entry = {
                "Sr.No": sr_no,
                "Date": new_stock_date,
                "Item Name": item_name,
                "Size": size,
                "Godown Name": godown_name,
                "Vendor Name": vendor_name
            }
            st.session_state.available_stock = st.session_state.available_stock.append(new_entry, ignore_index=True)
        
        st.subheader("New Stock Data")
        st.dataframe(st.session_state.available_stock,use_container_width=True,hide_index=True)


if __name__ == "__main__":
    stock_list_fun()