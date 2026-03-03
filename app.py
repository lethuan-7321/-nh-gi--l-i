import streamlit as st
import os
from PIL import Image

st.set_page_config(layout="wide")

st.title("ĐÁNH GIÁ HÌNH ẢNH LƯỠI")

image_folder = "images"
images = [f for f in os.listdir(image_folder) if f.lower().endswith(".jpg")]

current_image = st.selectbox("Chọn ảnh:", images)
image_path = os.path.join(image_folder, current_image)

# ====== CHIA 2 CỘT ======
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Hình ảnh")
    img = Image.open(image_path)
    st.image(img, use_column_width=True)

with col2:
    st.subheader("Bộ câu hỏi đánh giá")

q1 = st.radio("1. Màu sắc lưỡi?", 
              ["Hồng nhạt", "Đỏ", "Tím", "Nhợt"],
              horizontal=True)

q2 = st.radio("2. Rêu lưỡi?", 
              ["Mỏng", "Dày", "Trắng", "Vàng"],
              horizontal=True)

q3 = st.radio("3. Hình dạng lưỡi?", 
              ["Bình thường", "Sưng", "Có vết răng"],
              horizontal=True)

q4 = st.radio("4. Độ ẩm?", 
              ["Ẩm", "Khô"],
              horizontal=True)

q5 = st.radio("5. Có nứt lưỡi?", 
              ["Không", "Có"],
              horizontal=True)

q6 = st.radio("6. Có đốm bất thường?", 
              ["Không", "Có"],
              horizontal=True)

q7 = st.radio("7. Mép lưỡi?", 
              ["Bình thường", "Răng cưa"],
              horizontal=True)

q8 = st.radio("8. Tổng nhận định?", 
              ["Bình thường", "Cần theo dõi", "Bất thường"],
              horizontal=True)

    if st.button("Gửi đánh giá"):
        st.success("Đã ghi nhận đánh giá!")
