import streamlit as st
import pandas as pd
import os

st.title("✏️ Edit Product Data")

file_path = "data/products.csv"

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    df = pd.read_csv(file_path)
else:
    st.warning("No data found")
    st.stop()

# แก้ไขตาราง
edited_df = st.data_editor(df, num_rows="dynamic")

# Save
if st.button("💾 Save Changes"):
    edited_df.to_csv(file_path, index=False)
    st.success("Saved! ✅")
    st.experimental_rerun()
