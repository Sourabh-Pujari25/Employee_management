import streamlit as st
import pandas as pd
from datetime import date
import json
import os
from statics.css_ import *

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def load_stock_data():
    file_path = f"UserWorkspace/{st.session_state.user_name_}/{st.session_state.project_name}/stocklist.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        available_stock = pd.DataFrame(data.get('available_stock', []))
        used_stock = pd.DataFrame(data.get('used_stock', []))
        # Convert date strings back to date objects
        if 'Date' in available_stock.columns:
            available_stock['Date'] = pd.to_datetime(available_stock['Date']).dt.date
        if 'Date' in used_stock.columns:
            used_stock['Date'] = pd.to_datetime(used_stock['Date']).dt.date
    else:
        available_stock = pd.DataFrame(columns=["Sr.No", "Date", "Item Name", "Size", "Godown Name", "Vendor Name"])
        used_stock = pd.DataFrame(columns=["Sr.No", "Date", "Item Name", "Size", "Godown Name", "Vendor Name", "Name of Project", "Name of Work", "Sr.No of Work"])
    return available_stock, used_stock

def save_stock_data(available_stock, used_stock):
    file_path = f"UserWorkspace/{st.session_state.user_name_}/{st.session_state.project_name}/stocklist.json"
    ensure_directory_exists(os.path.dirname(file_path))
    
    # Convert date objects to strings
    available_stock_dict = available_stock.to_dict('records')
    used_stock_dict = used_stock.to_dict('records')
    
    for item in available_stock_dict + used_stock_dict:
        if 'Date' in item and isinstance(item['Date'], date):
            item['Date'] = item['Date'].isoformat()
    
    data = {
        'available_stock': available_stock_dict,
        'used_stock': used_stock_dict
    }
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def stock_list_fun():
    hide_pages()
    sidebar_colour()
    st.sidebar.markdown("   ")

    image = 'images/logo.png'
    st.sidebar.image(image, use_column_width=True)
    st.sidebar.markdown("   ")

    dashboard_select = st.sidebar.selectbox("Select an option", options=["Stock List", "Add New Work", "Labour Attendance", "Add Drawing", "Overview"])
    
    if dashboard_select == "Stock List":
        stokk()
    elif dashboard_select == "Overview":
        st.switch_page("pages/dashboard.py")
    elif dashboard_select == "Add New Work":
        st.switch_page("pages/dashboard.py")
    elif dashboard_select == "Labour Attendance":
        st.switch_page("pages/labour_attendance.py")
    elif dashboard_select == "Add Drawing":
        st.switch_page("pages/add_drawing.py")

def stokk():   
    # Load existing data
    if 'available_stock' not in st.session_state or 'used_stock' not in st.session_state:
        st.session_state.available_stock, st.session_state.used_stock = load_stock_data()

    # Sample data for dropdowns
    godowns = ["Godown A", "Godown B", "Godown C"]
    vendors = ["Vendor X", "Vendor Y", "Vendor Z"]

    st.title("Stock List")

    # Tabs
    tab1, tab2, tab3 = st.tabs(["Add New Stock", "Show Used Stock", "Show Available Stock"])

    with tab1:
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
            new_entry = pd.DataFrame({
                "Sr.No": [sr_no],
                "Date": [used_date],
                "Item Name": [item_name],
                "Size": [size],
                "Godown Name": [godown_name],
                "Vendor Name": [vendor_name],
                "Name of Project": [project_name],
                "Name of Work": [work_name],
                "Sr.No of Work": [work_sr_no]
            })
            st.session_state.used_stock = pd.concat([st.session_state.used_stock, new_entry], ignore_index=True)
            save_stock_data(st.session_state.available_stock, st.session_state.used_stock)
        
        st.subheader("Used Stock Data")
        st.dataframe(st.session_state.used_stock, use_container_width=True, hide_index=True)

    with tab3:
        st.header("Show Available Stock")
        with st.form(key='available_stock_form'):
            sr_no = st.text_input("Sr.No")
            stock_date = st.date_input("Date", value=date.today())
            item_name = st.text_input("Item Name")
            size = st.text_input("Size")
            godown_name = st.text_input("Godown Name")
            vendor_name = st.text_input("Vendor Name")
            submit_available = st.form_submit_button(label='Add to Available Stock')
        
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
