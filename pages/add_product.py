import streamlit as st
import pandas as pd
import os

st.title("➕ Add Product")

product_file = "data/products.csv"
material_file = "data/materials.csv"

# โหลด CSV
products = pd.read_csv(product_file) if os.path.exists(product_file) else pd.DataFrame(
    columns=[
        "category","product_name","material","model","brand","supplier",
        "size_or_capacity","price","currency","last_update","status","description"
    ]
)

materials = pd.read_csv(material_file) if os.path.exists(material_file) else pd.DataFrame(columns=["material"])
material_options = [""] + materials["material"].dropna().tolist()

with st.form("add_form"):
    category = st.text_input("Category")
    product_name = st.text_input("Product Name")
    material = st.selectbox("Material", material_options)
    model = st.text_input("Model")
    brand = st.text_input("Brand")
    supplier = st.text_input("Supplier")
    size = st.text_input("Size / Capacity")
    price = st.number_input("Price", min_value=0.0)
    currency = st.text_input("Currency", value="THB")
    last_update = st.date_input("Last Update")
    status = st.selectbox("Status", ["Purchased", "Not yet"])
    description = st.text_area("Description")

    submitted = st.form_submit_button("Add Product")

    if submitted:
        new_row = {
            "category": category,
            "product_name": product_name,
            "material": material,
            "model": model,
            "brand": brand,
            "supplier": supplier,
            "size_or_capacity": size,
            "price": price,
            "currency": currency,
            "last_update": str(last_update),
            "status": status,
            "description": description
        }
        products = pd.concat([products, pd.DataFrame([new_row])], ignore_index=True)
        products.to_csv(product_file, index=False)
        st.success("Product added successfully! ✅")
