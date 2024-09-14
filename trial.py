import streamlit as st
import json
import os
from datetime import datetime
import random
import pandas as pd

def get_next_work_id():
    """Generate the next Work ID based on the latest entry in the JSON file."""
    file_path = 'work_data.json'
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
    file_path = 'work_data.json'
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def main():
    st.title('Add Work')
    
    # Input fields
    name_of_work = st.text_input('Name of Work')
    date = st.date_input('Date', datetime.today())
    
    vardhaman_material = st.multiselect('Vardhaman Material', ['Material1', 'Material2', 'Material3'])
    vardhaman_quantity = st.number_input('Quantity for Vardhaman Material', min_value=1)
    
    mmc_material = st.multiselect('MMC Material', ['MaterialA', 'MaterialB', 'MaterialC'])
    mmc_quantity = st.number_input('Quantity for MMC Material', min_value=1)
    
    # Excavation Details
    st.header('Excavation Details')
    excavation_number = st.number_input('Number', value=1)
    excavation_length = st.number_input('Length (m)', value=1.0)
    excavation_width = st.number_input('Width (m)', value=1.0)
    excavation_depth = st.number_input('Depth (m)', value=random.uniform(0.94, 1.0))
    default_option = st.checkbox('Use default option', value=True)
    excavation_material = st.selectbox('Excavation Material', ['MaterialX', 'MaterialY', 'MaterialZ'])
    
    # JCB Bucket
    st.header('JCB Bucket Details')
    start_time_bucket = st.number_input('Start Time for JCB Bucket (Hours)', min_value=0.0, format='%.2f')
    stop_time_bucket = st.number_input('Stop Time for JCB Bucket (Hours)', min_value=0.0, format='%.2f')
    photo_start_bucket = st.file_uploader('Upload Photo for Start Time (JCB Bucket)', type=['jpg', 'png'])
    photo_stop_bucket = st.file_uploader('Upload Photo for Stop Time (JCB Bucket)', type=['jpg', 'png'])
    
    # JCB Breaker
    st.header('JCB Breaker Details')
    start_time_breaker = st.number_input('Start Time for JCB Breaker (Hours)', min_value=0.0, format='%.2f')
    stop_time_breaker = st.number_input('Stop Time for JCB Breaker (Hours)', min_value=0.0, format='%.2f')
    photo_start_breaker = st.file_uploader('Upload Photo for Start Time (JCB Breaker)', type=['jpg', 'png'])
    photo_stop_breaker = st.file_uploader('Upload Photo for Stop Time (JCB Breaker)', type=['jpg', 'png'])
    
    # Dewatering
    dewatering = st.number_input('Dewatering (L)', min_value=0)
    
    # Site Photo Upload
    site_photos = st.file_uploader('Upload Site Photos', type=['jpg', 'png'], accept_multiple_files=True)
    
    # Drawing Upload
    drawing_files = st.file_uploader('Upload Drawings', type=['pdf', 'jpg', 'png'], accept_multiple_files=True)
    
    # Labour
    st.header('Labour')
    labour_names = ['Labour1', 'Labour2', 'Labour3']
    selected_labour = [name for name in labour_names if st.checkbox(name, value=False)]
    
    # Additional Notes
    additional_notes = st.text_area('Additional Notes')
    
    # Submit Button
    if st.button('Submit'):
        work_id = get_next_work_id()
        work_data = {
            'Work ID': work_id,
            'Name of Work': name_of_work,
            'Date': date.strftime('%Y-%m-%d'),
            'Vardhaman Material': {'items': vardhaman_material, 'quantity': vardhaman_quantity},
            'MMC Material': {'items': mmc_material, 'quantity': mmc_quantity},
            'Excavation': {
                'Number': excavation_number,
                'Length': excavation_length,
                'Width': excavation_width,
                'Depth': excavation_depth,
                'Material': excavation_material,
                'Use Default': default_option
            },
            'JCB Bucket': {
                'Start Time': start_time_bucket,
                'Stop Time': stop_time_bucket,
                'Start Photo': photo_start_bucket.name if photo_start_bucket else None,
                'Stop Photo': photo_stop_bucket.name if photo_stop_bucket else None
            },
            'JCB Breaker': {
                'Start Time': start_time_breaker,
                'Stop Time': stop_time_breaker,
                'Start Photo': photo_start_breaker.name if photo_start_breaker else None,
                'Stop Photo': photo_stop_breaker.name if photo_stop_breaker else None
            },
            'Dewatering': dewatering,
            'Site Photos': [file.name for file in site_photos] if site_photos else [],
            'Drawing Upload': [file.name for file in drawing_files] if drawing_files else [],
            'Labour': selected_labour,
            'Additional Notes': additional_notes
        }

        existing_data = load_existing_data()
        existing_data.append(work_data)

        with open('work_data.json', 'w') as file:
            json.dump(existing_data, file, indent=4)

        st.success('Work details saved successfully!')

        with open("work_data.json","r") as f:
            json_data=f.read()


        data = json.loads(json_data)

        df = pd.json_normalize(data)
        st.data_editor(df)



if __name__ == "__main__":
    main()
