import streamlit as st
import pandas as pd
import os

st.title("📊 Product Price Database (Home)")

file_path = "data/products.csv"

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=[
        "category","product_name","material","model","brand","supplier",
        "size_or_capacity","price","currency","last_update","status","description"
    ])

st.write("Welcome to the Product Price Database")
st.dataframe(df.head())
