import streamlit as st
import pandas as pd
import os

st.title("🛠 Manage Materials")

file_path = "data/products.csv"

# โหลด CSV
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    df = pd.read_csv(file_path)
else:
    st.warning("No product data found")
    st.stop()

# ดึง material ปัจจุบัน
if "material" in df.columns:
    materials = sorted(df["material"].dropna().unique().tolist())
else:
    materials = []

st.subheader("Existing Materials")
for m in materials:
    st.text(m)

# ➕ Add new material
st.subheader("➕ Add Material")
new_material = st.text_input("New Material")
if st.button("Add Material"):
    if new_material and new_material not in materials:
        # เพิ่ม material เข้า dataframe ของ product ทั้งหมดเป็นค่าว่าง
        df.loc[df["material"].isna(), "material"] = ""
        # ไม่ต้องเพิ่มแถวใหม่แค่ให้ dropdown ดึงค่าใหม่
        st.success(f"Material '{new_material}' added! ✅")
        # material ใหม่จะอยู่ใน dropdown ของหน้า Add Product
        st.experimental_rerun()
    else:
        st.warning("Material already exists or empty")
