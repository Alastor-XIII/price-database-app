import streamlit as st
import pandas as pd
import os

st.title("🛠 Manage Materials")

file_path = "data/materials.csv"

# เช็คไฟล์และสร้างถ้ายังไม่มี
if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    # สร้างไฟล์เปล่าพร้อม column header
    df = pd.DataFrame(columns=["material"])
    df.to_csv(file_path, index=False)
else:
    df = pd.read_csv(file_path)

# แสดง material ปัจจุบัน
st.subheader("Existing Materials")
if not df.empty:
    for m in df["material"].dropna().tolist():
        st.text(m)
else:
    st.info("No materials yet.")

# ➕ Add new material
st.subheader("➕ Add Material")
new_material = st.text_input("New Material")
if st.button("Add Material"):
    if new_material:
        if new_material in df["material"].values:
            st.warning("Material already exists")
        else:
            df = pd.concat([df, pd.DataFrame([{"material": new_material}])], ignore_index=True)
            df.to_csv(file_path, index=False)
            st.success(f"Material '{new_material}' added! ✅")
    else:
        st.warning("Please enter a material name")
