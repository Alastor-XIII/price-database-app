import streamlit as st
import pandas as pd

st.title("✏️ Edit Product Data")

df = pd.read_csv("data/products.csv")

edited_df = st.data_editor(df, num_rows="dynamic")

if st.button("💾 Save Changes"):
    edited_df.to_csv("data/products.csv", index=False)
    st.success("Saved!")
    st.rerun()
