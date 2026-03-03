import streamlit as st
import os
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")

st.title("ĐÁNH GIÁ HÌNH ẢNH LƯỠI")

# Tạo thư mục ảnh
image_folder = "images"

if not os.path.exists(image_folder):
    st.error("Chưa có thư mục images")
    st.stop()

image_files = sorted(os.listdir(image_folder))

if "index" not in st.session_state:
    st.session_state.index = 0

if st.session_state.index >= len(image_files):
    st.success("Đã hoàn thành đánh giá!")
    st.stop()

current_image = image_files[st.session_state.index]

col1, col2 = st.columns([1,1])

with col1:
    st.image(os.path.join(image_folder, current_image), use_column_width=True)

with col2:
    st.subheader("Câu hỏi")

    shape = st.radio("1. Hình dạng lưỡi:", ["To", "Bình thường", "Gầy"])
    color = st.radio("2. Màu sắc lưỡi:", ["Đỏ", "Hồng", "Nhạt"])
    coating = st.radio("3. Rêu lưỡi:", ["Khô", "Nhuận", "Ướt"])

    if st.button("Lưu & tiếp tục"):
        data = {
            "image": current_image,
            "shape": shape,
            "color": color,
            "coating": coating
        }

        df = pd.DataFrame([data])

        if os.path.exists("results.csv"):
            df.to_csv("results.csv", mode="a", header=False, index=False)
        else:
            df.to_csv("results.csv", index=False)

        st.session_state.index += 1
        st.rerun()
