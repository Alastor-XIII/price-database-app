import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Product Price Database", layout="wide")
st.title("📊 Product Price Database")

file_path = "data/products.csv"

# Columns สำหรับ CSV
columns = [
    "category","product_name","model","supplier","brand","size_or_capacity",
    ,"price","currency","last_update","status","description"
]

# โหลด CSV
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=columns)

# 🔎 Filter
st.subheader("🔎 Filter")
col1, col2 = st.columns(2)

with col1:
    categories = [""] + sorted(df["category"].dropna().unique().tolist())
    selected_category = st.selectbox("Category", categories)

with col2:
    makers = ["All"] + sorted(df["maker"].dropna().unique().tolist())
    selected_maker = st.selectbox("Maker", makers)

# ➕ Add Form
st.subheader("➕ Add Product")
with st.form("add_form"):
    category = st.text_input("Category")
    product_name = st.text_input("Product Name")
    model = st.text_input("Model")
    maker = st.text_input("Maker")
    size = st.text_input("Size / Capacity")
    supplier = st.text_input("Supplier")
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
            "maker": maker,
            "size_or_capacity": size,
            "supplier": supplier,
            "price": price,
            "currency": currency,
            "last_update": str(last_update),
            "status": status,
            "description": description
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(file_path, index=False)
        st.success("Added! ✅")
        st.experimental_rerun()  # รีเฟรชหน้าอัตโนมัติ

# แสดง Table เฉพาะเมื่อเลือก Category
if selected_category:
    df_show = df.copy()
    df_show = df_show[df_show["category"] == selected_category]
    if selected_maker != "All":
        df_show = df_show[df_show["maker"] == selected_maker]
    st.subheader(f"Products in Category: {selected_category}")
    st.dataframe(df_show, use_container_width=True)
else:
    st.info("Please select a category above to see products.")
