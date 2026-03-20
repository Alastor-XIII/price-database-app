__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
import pandas as pd
import os

st.title("📊 Product Price Database (Home)")

product_file = "data/products.csv"

# โหลด CSV
if os.path.exists(product_file) and os.path.getsize(product_file) > 0:
    df = pd.read_csv(product_file)
else:
    df = pd.DataFrame(columns=[
        "category","product_name","material","model","brand","supplier",
        "size_or_capacity","price","currency","last_update","status","description"
    ])

# 🔎 Filter
st.subheader("🔎 Filter")

col1, col2 = st.columns(2)

with col1:
    categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
    selected_category = st.selectbox("Category", categories)

with col2:
    brands = ["All"] + sorted(df["brand"].dropna().unique().tolist())
    selected_brand = st.selectbox("Brand", brands)

df_show = df.copy()
if selected_category != "All":
    df_show = df_show[df_show["category"] == selected_category]
if selected_brand != "All":
    df_show = df_show[df_show["brand"] == selected_brand]

st.subheader("Products Table")
st.dataframe(df_show, use_container_width=True)
