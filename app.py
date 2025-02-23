import streamlit as st
import pandas as pd

# Load the data
file_path = 'Lineman_Shops_Final_Clean.csv'  # ใส่พาธของไฟล์ CSV ที่ใช้งาน
data = pd.read_csv(file_path)

# Title of the app with custom styles
st.markdown("""
    <style>
    body {
        background-color: #f4f8fb;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 40px;
        color: #FF5722;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .subheader {
        color: #333;
        font-size: 18px;
        font-weight: 600;
    }
    .card {
        background-color: #FFFFFF;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 25px;
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .price-tag {
        background-color: #FFEB3B;
        padding: 5px 10px;
        border-radius: 5px;
        color: #333;
        font-weight: bold;
    }
    .button {
        background-color: #FF5722;
        color: white;
        border: none;
        padding: 12px 25px;
        cursor: pointer;
        font-size: 16px;
        border-radius: 5px;
        text-align: center;
        display: inline-block;
    }
    .button:hover {
        background-color: #E64A19;
    }
    .header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .container {
        margin-top: 20px;
        padding: 20px;
    }
    .filter {
        background-color: #FFCCBC;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<div class="title">แนะนำเมนูอาหารเย็น</div>', unsafe_allow_html=True)

# Filter section with nice background and padding
with st.container():
    st.markdown('<div class="filter">', unsafe_allow_html=True)
    
    # Dropdown for choosing price range
    price_levels = data['price_level'].unique()  # ดึงช่วงราคาจากคอลัมน์ในไฟล์ CSV
    price_range = st.selectbox('เลือกช่วงราคา:', price_levels)

    # Dropdown for selecting cuisine type
    cuisine_type = st.selectbox('เลือกประเภทอาหาร:', data['cuisine'].unique())

    # Slider for rating (1 to 5)
    rating = st.slider('เลือกคะแนนจาก 1 ถึง 5:', 1, 5)

    st.markdown('</div>', unsafe_allow_html=True)

# Filter the data based on the selections
filtered_data = data[(data['price_level'] == price_range) & 
                     (data['cuisine'] == cuisine_type)]

# Show filtered data and display
if not filtered_data.empty:
    st.write(f'แนะนำร้านอาหารในหมวด **{cuisine_type}** ที่ราคาประมาณ **{price_range}** และมีคะแนนสูงสุด **{rating}** คะแนน:')

    for index, row in filtered_data.iterrows():
        with st.container():
            st.markdown(f'<div class="card">', unsafe_allow_html=True)
            st.subheader(row['name'])
            st.write(f"ประเภทอาหาร: {row['cuisine']}")
            st.write(f"ที่ตั้ง: {row['street']}")
            st.write(f"คะแนนจากลูกค้า: {rating} / 5")
            st.write(f"ราคา: <span class='price-tag'>{row['price_level']}</span>", unsafe_allow_html=True)

            # Check if the Facebook URL is available, if so display it
            if row['facebook'] != '-':
                st.write(f"เยี่ยมชมร้านได้ที่: [Facebook]({row['facebook']})")
            else:
                st.write("ไม่มีลิงก์ Facebook")

            st.markdown('</div>', unsafe_allow_html=True)

else:
    st.write("ไม่พบร้านอาหารที่ตรงกับเงื่อนไขที่เลือก")

# Add a call-to-action button at the bottom
st.markdown('<div class="container"><button class="button">ดูข้อมูลเพิ่มเติม</button></div>', unsafe_allow_html=True)
