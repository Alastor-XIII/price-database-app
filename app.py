import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Product Price Database", layout="wide")
st.title("📊 Product Price Database")

file_path = "data/products.csv"

# Columns สำหรับ CSV
columns = [
    "category","product_name","model","maker","size_or_capacity",
    "supplier","price","currency","last_update","status","description"
]

# โหลดข้อมูล CSV
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

# ถ้าเลือก Category เท่านั้นถึงโชว์ตาราง
if selected_category:
    df_show = df.copy()
    if selected_category != "":
        df_show = df_show[df_show["category"] == selected_category]
    if selected_maker != "All":
        df_show = df_show[df_show["maker"] == selected_maker]

    st.dataframe(df_show, use_container_width=True)
else:
    st.info("Please select a category above to see products.")
