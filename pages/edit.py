import streamlit as st
import pandas as pd
import os

st.title("✏️ Edit Product Data by Category")

file_path = "data/products.csv"

# โหลด CSV
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    df = pd.read_csv(file_path)
else:
    st.warning("No data found")
    st.stop()

# เลือก Category
categories = ["All"] + sorted(df["category"].dropna().unique().tolist()) if "category" in df.columns else ["All"]
selected_category = st.selectbox("Select Category", categories)

# Filter ตาม Category
if selected_category != "All":
    df_show = df[df["category"] == selected_category].copy()
else:
    df_show = df.copy()

# เลือก column และเรียงใหม่: model → supplier → brand → product_name → material → ...
display_columns = ["model","supplier","brand","product_name","material","size_or_capacity","price","currency","last_update","status","description"]
display_columns = [col for col in display_columns if col in df_show.columns]

# แก้ไขตาราง
edited_df = st.data_editor(df_show[display_columns], num_rows="dynamic")

# Save
if st.button("💾 Save Changes"):
    if selected_category != "All":
        df = df[df["category"] != selected_category]
        df = pd.concat([df, edited_df], ignore_index=True)
    else:
        df = edited_df.copy()

    df.to_csv(file_path, index=False)
    st.success("Saved! ✅")
    st.experimental_rerun()
