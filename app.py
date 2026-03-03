import streamlit as st
import os
from PIL import Image

st.set_page_config(layout="wide")

st.title("ĐÁNH GIÁ HÌNH ẢNH LƯỠI")

image_folder = "images"

# Kiểm tra thư mục tồn tại
if not os.path.exists(image_folder):
    st.error("Không tìm thấy thư mục images")
    st.stop()

# Lấy danh sách ảnh jpg
images = [f for f in os.listdir(image_folder) if f.lower().endswith(".jpg")]

if len(images) == 0:
    st.error("Không tìm thấy file JPG trong thư mục images")
    st.stop()

# Chọn ảnh
current_image = st.selectbox("Chọn ảnh:", images)

image_path = os.path.join(image_folder, current_image)

st.write("Đường dẫn:", image_path)
st.write("File tồn tại:", os.path.exists(image_path))

# Hiển thị ảnh
try:
    img = Image.open(image_path)
    st.image(img, use_column_width=True)
except Exception as e:
    st.error(f"Lỗi mở ảnh: {e}")
