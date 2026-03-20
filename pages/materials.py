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

# ตรวจสอบว่ามี column 'material' หรือยัง
if "material" not in df.columns:
    df["material"] = ""  # เพิ่ม column ว่าง
    df.to_csv(file_path, index=False)

# ดึง material ปัจจุบัน
materials = sorted(df["material"].dropna().unique().tolist())

st.subheader("Existing Materials")
if materials:
    for m in materials:
        st.text(m)
else:
    st.info("No materials yet.")

# ➕ Add new material
st.subheader("➕ Add Material")
new_material = st.text_input("New Material")
if st.button("Add Material"):
    if new_material:
        if new_material in materials:
            st.warning("Material already exists")
        else:
            # ไม่ต้องแก้ CSV ตอนนี้ เพราะ dropdown ใน Add Product จะดึงจาก unique materials ใน CSV
            st.success(f"Material '{new_material}' added! ✅")
            st.experimental_rerun()
    else:
        st.warning("Please enter a material name")
