import streamlit as st

# Function to add new size input fields
def add_size_input(size_list, qty_list):
    size = st.selectbox("Select Size", ["S", "M", "L", "XL", "XXL"])
    qty = st.number_input("Quantity", min_value=1, value=1)
    size_list.append(size)
    qty_list.append(qty)

# Main app code
def main():
    st.title("T-shirt Size and Quantity Selection")

    tshirt_name = st.text_input("Enter T-shirt Name")
    
    if st.button("Add T-shirt"):
        with st.expander(tshirt_name, expanded=True):
            size_list = []
            qty_list = []
            
            # Initial size and quantity input
            add_size_input(size_list, qty_list)

            if st.button("Add Size"):
                add_size_input(size_list, qty_list)
            
            # Displaying the selected sizes and quantities
            st.write("Selected Sizes and Quantities:")
            for size, qty in zip(size_list, qty_list):
                st.write(f"Size: {size}, Quantity: {qty}")

if __name__ == "__main__":
    main()
