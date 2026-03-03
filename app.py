import streamlit as st
import pandas as pd
from PIL import Image
import os

# Cấu hình trang
st.set_page_config(layout="wide")

st.title("Hệ thống thiệt chẩn")

# ===== Load ảnh cố định =====
from PIL import Image

img = Image.open("images/luoi_1.jpg")

# ===== Layout 2 cột =====
col1, col2 = st.columns([1, 1])

# ============================
# CỘT TRÁI - ẢNH
# ============================
with col1:
    st.subheader("Ảnh lưỡi")
    st.image(img, width=450)

# ============================
# CỘT PHẢI - 8 CÂU HỎI
# ============================
with col2:
    st.subheader("Nhập đặc điểm thiệt chẩn")

    q1 = st.radio("1. Màu sắc lưỡi:",
                  ["Hồng nhạt", "Đỏ", "Tím", "Nhợt"],
                  horizontal=True)

    q2 = st.radio("2. Rêu lưỡi:",
                  ["Không", "Mỏng", "Dày"],
                  horizontal=True)

    q3 = st.radio("3. Màu rêu:",
                  ["Trắng", "Vàng", "Xám"],
                  horizontal=True)

    q4 = st.radio("4. Hình dạng lưỡi:",
                  ["Bình thường", "Sưng", "Teo"],
                  horizontal=True)

    q5 = st.radio("5. Có vết răng?",
                  ["Không", "Có"],
                  horizontal=True)

    q6 = st.radio("6. Độ ẩm:",
                  ["Ẩm", "Khô"],
                  horizontal=True)

    q7 = st.radio("7. Có nứt lưỡi?",
                  ["Không", "Có"],
                  horizontal=True)

    q8 = st.radio("8. Có đốm bất thường?",
                  ["Không", "Có"],
                  horizontal=True)

# ============================
# LƯU CSV TỰ ĐỘNG
# ============================

data = {
    "Màu sắc": [q1],
    "Rêu lưỡi": [q2],
    "Màu rêu": [q3],
    "Hình dạng": [q4],
    "Vết răng": [q5],
    "Độ ẩm": [q6],
    "Nứt lưỡi": [q7],
    "Đốm bất thường": [q8]
}

df = pd.DataFrame(data)

file_path = "ket_qua.csv"

# Nếu file tồn tại thì append, không thì tạo mới
if os.path.exists(file_path):
    df.to_csv(file_path, mode='a', header=False, index=False)
else:
    df.to_csv(file_path, index=False)
