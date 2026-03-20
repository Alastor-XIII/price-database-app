import streamlit as st
import pandas as pd
import os

st.title("📊 Product Price Database")

file_path = "data/products.csv"

# โหลดข้อมูล
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=[
        "category","product_name","supplier","price","currency","last_update","status"
    ])

# 🔎 Filter ตามหมวด
st.subheader("🔎 Filter by Category")
categories = df["category"].dropna().unique().tolist()
selected_category = st.selectbox("Select category", ["All"] + categories)

if selected_category != "All":
    df_show = df[df["category"] == selected_category]
else:
    df_show = df

st.dataframe(df_show, use_container_width=True)

# ➕ เพิ่มข้อมูล
st.subheader("➕ Add New Product")

with st.form("add_form"):
    category = st.text_input("Category")
    product_name = st.text_input("Product Name")
    supplier = st.text_input("Supplier")
    price = st.number_input("Price", min_value=0.0)
    currency = st.text_input("Currency", value="THB")
    last_update = st.date_input("Last Update")
    status = st.selectbox("Status", ["Purchased", "Not yet"])

    submitted = st.form_submit_button("Add")

    if submitted:
        new_row = {
            "category": category,
            "product_name": product_name,
            "supplier": supplier,
            "price": price,
            "currency": currency,
            "last_update": str(last_update),
            "status": status
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(file_path, index=False)

        st.success("Added successfully! Please refresh")

# ✏️ แก้ไขข้อมูล (basic)
st.subheader("✏️ Edit Data (manual)")

edited_df = st.data_editor(df, num_rows="dynamic")

if st.button("💾 Save Changes"):
    edited_df.to_csv(file_path, index=False)
    st.success("Saved!")
