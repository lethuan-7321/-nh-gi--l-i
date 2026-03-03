import streamlit as st
from PIL import Image

# Cấu hình trang
st.set_page_config(layout="wide")

st.title("Hệ thống phân tích lưỡi")

# Upload ảnh
uploaded_file = st.file_uploader("Tải ảnh lưỡi lên", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)

    # Tạo 2 cột
    col1, col2 = st.columns([1, 1])

    # ===== CỘT TRÁI =====
    with col1:
        st.subheader("Ảnh lưỡi")
        st.image(img, width=450)

    # ===== CỘT PHẢI =====
    with col2:
        st.subheader("Nhập đặc điểm lưỡi")

        color = st.radio(
            "Màu sắc lưỡi:",
            ["Hồng nhạt", "Đỏ", "Tím", "Nhợt"]
        )

        coat = st.radio(
            "Rêu lưỡi:",
            ["Mỏng", "Dày", "Trắng", "Vàng"]
        )

        shape = st.radio(
            "Hình dạng lưỡi:",
            ["Bình thường", "Sưng", "Có vết răng"]
        )

        moisture = st.radio(
            "Độ ẩm:",
            ["Ẩm", "Khô"]
        )

        cracks = st.radio(
            "Có nứt lưỡi?",
            ["Không", "Có"]
        )

        spots = st.radio(
            "Có đốm bất thường?",
            ["Không", "Có"]
        )

        if st.button("Phân tích"):
            st.success("Đã ghi nhận thông tin!")
            st.write("### Kết quả bạn chọn:")
            st.write("Màu sắc:", color)
            st.write("Rêu lưỡi:", coat)
            st.write("Hình dạng:", shape)
            st.write("Độ ẩm:", moisture)
            st.write("Nứt lưỡi:", cracks)
            st.write("Đốm bất thường:", spots)

else:
    st.info("Vui lòng tải ảnh lên để bắt đầu.")
