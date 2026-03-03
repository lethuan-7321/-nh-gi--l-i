import streamlit as st
import os
import random
import csv
from datetime import datetime
from PIL import Image

st.set_page_config(layout="wide")

st.title("Hệ thống thiết chẩn")

# =========================
# RANDOM ẢNH
# =========================
image_list = ["luoi_1.jpg", "luoi_2.jpg"]
selected_image = random.choice(image_list)
image_path = os.path.join("images", selected_image)

# =========================
# CHIA 2 CỘT
# =========================
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Ảnh lưỡi")
    img = Image.open(image_path)
    st.image(img)

with col2:
    st.subheader("Nhập đặc điểm thiết chẩn")

    q1 = st.radio("Màu sắc lưỡi:", 
                  ["Hồng nhạt", "Đỏ", "Tím", "Nhợt"],
                  horizontal=True)

    q2 = st.radio("Rêu lưỡi:",
                  ["Không", "Mỏng", "Dày"],
                  horizontal=True)

    q3 = st.radio("Màu rêu:",
                  ["Trắng", "Vàng", "Xám"],
                  horizontal=True)

    q4 = st.radio("Hình dạng lưỡi:",
                  ["Bình thường", "Sưng", "Teo"],
                  horizontal=True)

    q5 = st.radio("Có vết răng?",
                  ["Không", "Có"],
                  horizontal=True)

    q6 = st.radio("Độ ẩm:",
                  ["Ẩm", "Khô"],
                  horizontal=True)

    q7 = st.radio("Có nứt lưỡi?",
                  ["Không", "Có"],
                  horizontal=True)

    q8 = st.radio("Có đốm bất thường?",
                  ["Không", "Có"],
                  horizontal=True)

    # =========================
    # NÚT LƯU
    # =========================
    if st.button("Lưu kết quả"):

        file_exists = os.path.isfile("ket_qua.csv")

        with open("ket_qua.csv", mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # ghi header nếu file chưa tồn tại
            if not file_exists:
                writer.writerow([
                    "Thoi_gian",
                    "Ten_anh",
                    "Mau_sac",
                    "Reu_luoi",
                    "Mau_reu",
                    "Hinh_dang",
                    "Vet_rang",
                    "Do_am",
                    "Nut_luoi",
                    "Dom_bat_thuong"
                ])

            writer.writerow([
                datetime.now(),
                selected_image,
                q1, q2, q3, q4, q5, q6, q7, q8
            ])

        st.success("Đã lưu kết quả vào file CSV!")
import gspread
from google.oauth2.service_account import Credentials
import json
import streamlit as st
from datetime import datetime

# Load credentials từ secrets
creds_dict = st.secrets["GOOGLE_CREDENTIALS"]
creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)

client = gspread.authorize(creds)

# Mở Google Sheet
sheet = client.open("Tên file Google Sheet của bạn").sheet1

# Khi người dùng bấm nút
if st.button("Xem kết quả"):
    
    result = "Kết quả AI trả về"

    sheet.append_row([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Tên ảnh hoặc thông tin",
        "Đặc điểm nhập",
        result
    ])
    
    st.success("Đã lưu kết quả!")
