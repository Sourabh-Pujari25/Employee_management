import streamlit as st
import pandas as pd
import json
import os
from streamlit_option_menu import option_menu

# Function to load existing stock data from JSON
def load_stock_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

# Function to save stock data to JSON
def save_stock_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to generate a new Stock_ID
def generate_stock_id(stock_data):
    if stock_data:
        last_stock_id = stock_data[-1]['Stock_ID']
        num = int(last_stock_id.split('_')[1]) + 1
        return f'Stock_{num:03}'
    return 'Stock_001'


def stock_list_fun():
    option_menu(menu_title=None,options=["Manage Your Stocks"],key="manage_stocks",icons=["bi bi-pencil"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
        
    # Load existing data
    filename = f'UserWorkspace/{st.session_state.user_name_}/{st.session_state.project_name}/stocklist.json'
    stock_data = load_stock_data(filename)
    with st.container(border=True):
        stock_opt_space,stock_display_space=st.columns([3,7])
        with stock_opt_space:
            with st.container(border=True):
                    if st.toggle("Update Stock"):
                        update_stock=pd.DataFrame(stock_data)
                        update_stock_list=update_stock["Item Name"].to_list()

                        item_name = st.selectbox("Item Name",options=update_stock_list)
                        date = st.date_input("Date")
                        size_col,qty_col=st.columns(2)
                        with size_col:
                            size = st.text_input("Size")
                            godown_names = st.text_input("Godown Name")
                        with qty_col:
                            qty = st.number_input("")
                            vendor_names = st.text_input("Vendor Name")
                        if st.button("Submit"):
                            # Generate a new Stock_ID
                            new_stock_id = generate_stock_id(stock_data)
                    else:
                        date = st.date_input("Date")
                        item_name = st.text_input("Item Name")
                        with st.expander("Size",expanded=True):
                            size_col,qty_col=st.columns(2)
                            with size_col:
                                size = st.text_input("Size")
                                godown_names = st.text_input("Godown Name")
                            with qty_col:
                                qty = st.number_input("")
                                vendor_names = st.text_input("Vendor Name")
                        if st.button("Submit"):
                            # Generate a new Stock_ID
                            new_stock_id = generate_stock_id(stock_data)
            
            # Create new stock entry
            try:
                new_entry = {
                    'Stock_ID': new_stock_id,
                    'Date': date.isoformat(),
                    'Item Name': item_name,
                    'Size': size,
                    'Quantity':qty,
                    'Godown Name': godown_names,
                    'Vendor Name': vendor_names
                }
            
            # Append new entry to existing data and save
                stock_data.append(new_entry)
                save_stock_data(stock_data, filename)
                
                st.success("Stock added successfully!")
            except:
                pass


        # Display existing stock data
        with stock_display_space:
            stock_df=pd.DataFrame(stock_data)
            stock_df.insert(0,'Select',False)
            st.data_editor(stock_df,use_container_width=True,hide_index=True)


if __name__=="__main__":
    stock_list_fun()