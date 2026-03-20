import streamlit as st
import pandas as pd

st.title("📊 Product Price Database")

df = pd.read_csv("data/products.csv")

st.dataframe(df)