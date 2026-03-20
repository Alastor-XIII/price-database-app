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
categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
selected_category = st.selectbox("Select Category", categories)

# Filter ตาม Category
if selected_category != "All":
    df_show = df[df["category"] == selected_category].copy()
else:
    df_show = df.copy()

# แก้ไขตาราง
edited_df = st.data_editor(df_show, num_rows="dynamic")

# Save
if st.button("💾 Save Changes"):
    # ถ้าเลือก Category ให้ update เฉพาะแถวนั้น
    if selected_category != "All":
        # ลบข้อมูลเก่าของ category นั้น
        df = df[df["category"] != selected_category]
        # เพิ่มข้อมูลที่แก้แล้ว
        df = pd.concat([df, edited_df], ignore_index=True)
    else:
        # Save ทั้งหมด
        df = edited_df.copy()

    df.to_csv(file_path, index=False)
    st.success("Saved! ✅")
    st.experimental_rerun()
