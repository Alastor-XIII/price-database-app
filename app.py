import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Product Price Database", layout="wide")
st.title("📊 Product Price Database")

file_path = "data/products.csv"

# Columns สำหรับ CSV (เรียงใหม่: model, supplier, brand)
columns = [
    "category","product_name","model","supplier","brand","size_or_capacity",
    "price","currency","last_update","status","description"
]

# สร้าง CSV ว่างถ้ายังไม่มี
if not os.path.exists(file_path):
    pd.DataFrame(columns=columns).to_csv(file_path, index=False)

# โหลด CSV
df = pd.read_csv(file_path)

# 🔎 Filter
st.subheader("🔎 Filter")
col1, col2 = st.columns(2)

with col1:
    categories = [""] + sorted(df["category"].dropna().unique().tolist()) if "category" in df.columns else [""]
    selected_category = st.selectbox("Category", categories)

with col2:
    brands = ["All"] + sorted(df["brand"].dropna().unique().tolist()) if "brand" in df.columns else ["All"]
    selected_brand = st.selectbox("Brand", brands)

# ➕ Add Form
st.subheader("➕ Add Product")
with st.form("add_form"):
    category = st.text_input("Category")
    product_name = st.text_input("Product Name")
    model = st.text_input("Model")
    supplier = st.text_input("Supplier")
    brand = st.text_input("Brand")
    size = st.text_input("Size / Capacity")
    price = st.number_input("Price", min_value=0.0)
    currency = st.text_input("Currency", value="THB")
    last_update = st.date_input("Last Update")
    status = st.selectbox("Status", ["Purchased", "Not yet"])
    description = st.text_area("Description")

    submitted = st.form_submit_button("Add")
    if submitted:
        new_row = {
            "category": category,
            "product_name": product_name,
            "model": model,
            "supplier": supplier,
            "brand": brand,
            "size_or_capacity": size,
            "price": price,
            "currency": currency,
            "last_update": str(last_update),
            "status": status,
            "description": description
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(file_path, index=False)
        st.success("Added! ✅")
        st.experimental_rerun()

# แสดง Table เฉพาะเมื่อเลือก Category
if selected_category:
    df_show = df.copy()
    df_show = df_show[df_show["category"] == selected_category]
    if selected_brand != "All":
        df_show = df_show[df_show["brand"] == selected_brand]
    st.subheader(f"Products in Category: {selected_category}")
    st.dataframe(df_show[["model","supplier","brand","product_name","size_or_capacity","price","currency","last_update","status","description"]], use_container_width=True)
else:
    st.info("Please select a category above to see products.")
