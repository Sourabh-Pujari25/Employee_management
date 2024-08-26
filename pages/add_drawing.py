import streamlit as st
from datetime import date
from statics.css_ import *



def add_drawinng_fun():
    hide_pages()
    sidebar_colour()
    image = 'images/logo.png'
    st.sidebar.image(image,use_column_width=True)
    st.sidebar.markdown("   ")
    dashboard_select=st.sidebar.selectbox("Select an option",options=["Add Drawing","Overview","Add New Work","Labour Attendance","Stock List"])
    # dashboard_overview=st.sidebar.selectbox("Overview",use_container_width=True)
    if dashboard_select =="Add Drawing" :
      add_drr()
    elif dashboard_select =="Overview" :
       st.switch_page("pages/dashboard.py")
    elif dashboard_select=="Add New Work":
        st.switch_page("pages/dashboard.py")
    elif dashboard_select=="Labour Attendance":
       st.switch_page("pages/labour_attendance.py")
    
    elif dashboard_select=="Stock List":
        st.switch_page("pages/stock_list.py")
    # Sample project names
def add_drr():
        # Page 2: Fill out the form
        st.title(f"Add Drawing for {st.session_state.project_name}")
        
        with st.form(key='drawing_form'):
            name_of_work = st.text_input("Name of Work")
            work_date = st.date_input("Date", value=date.today())
            drawings = st.file_uploader("Drawing Upload", accept_multiple_files=True)
            
            submit_button = st.form_submit_button(label='Submit')
            
        if submit_button:
            st.success("Form submitted successfully!")
            st.write("Details Submitted:")
            st.write(f"Name of Work: {name_of_work}")
            st.write(f"Date: {work_date}")
            if drawings:
                st.write("Drawings Uploaded:")
                for drawing in drawings:
                    st.write(f"- {drawing.name}")

    


if __name__ == "__main__":
    add_drawinng_fun()