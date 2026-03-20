import streamlit as st
import pandas as pd
import os

st.title("➕ Add Product")

product_file = "data/products.csv"
material_file = "data/materials.csv"

# --- โหลด CSV หรือสร้างใหม่ถ้าไม่มี ---
if os.path.exists(product_file) and os.path.getsize(product_file) > 0:
    products = pd.read_csv(product_file)
else:
    products = pd.DataFrame(columns=[
        "category","product_name","material","model","brand","supplier",
        "size_or_capacity","price","currency","last_update","status","description"
    ])
    products.to_csv(product_file, index=False)

if os.path.exists(material_file) and os.path.getsize(material_file) > 0:
    materials = pd.read_csv(material_file)
else:
    materials = pd.DataFrame(columns=["material"])
    materials.to_csv(material_file, index=False)

material_options = [""] + materials["material"].dropna().tolist()

# --- ฟอร์มเพิ่มสินค้า ---
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
        # เพิ่มสินค้าใหม่
        products = pd.concat([products, pd.DataFrame([new_row])], ignore_index=True)
        products.to_csv(product_file, index=False)

        st.success("Product added successfully! ✅")
        st.write("Preview of added product:")
        st.dataframe(pd.DataFrame([new_row]))
