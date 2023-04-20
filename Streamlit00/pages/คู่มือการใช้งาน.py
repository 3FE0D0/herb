import streamlit as st
from PIL import Image
import os
import cv2
import numpy as np 

st.set_page_config(
    page_title="Herb Detchtion", page_icon="📖",)

st.markdown("<h2 style='text-align: center; color: Black;'>คู่มือการใช้งาน</h2>", unsafe_allow_html=True)

# สร้าง CSS สำหรับตกแต่งตัวหนังสือ
css = """
.big-text {
    font-size: 20px;
    color: #3B130C;
}

.red-text {
    color: red;

}

"""

# ใช้ st.markdown() เพื่อแสดงตัวหนังสือและ CSS บน Streamlit
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown('<p class="big-text"><b>หน้าหลัก</b></p>', unsafe_allow_html=True)
st.write("ประกอบด้วย 3 ส่วนหลัก")
st.write("1.	เมนู")
st.write("2.	ค้นหาข้อมูล")
st.write("3.	รูปภาพ")

image = Image.open('1B.jpg')
st.image(image)

st.write("___________________________________________________________________________________________________________________________________________________________________")
st.markdown('<p class="big-text"><b>เมนู</b></p>', unsafe_allow_html=True)
st.write("1.	Home (หน้าหลัก)")
st.write("2.	Check Herb (เช็คสมุนไพร)")
st.write("3.	Data (ข้อมูลสมุนไพร)")
st.write("4.	คู่มือการใช้งาน")

image = Image.open('2B.jpg')
st.image(image)

st.write("___________________________________________________________________________________________________________________________________________________________________")
st.markdown('<p class="big-text"><b>ค้นหาข้อมูล</b></p>', unsafe_allow_html=True)
st.write("1.	คลิกที่ช่องค้นหา")
st.write("2.	ใส่ชื่อสมุนไพรที่ต้องการหรือเลือกจากรายการที่มีอยู่ในช่องค้นหา")
image = Image.open('3B.jpg')
st.image(image)
st.write("3.	คลิกปุ่ม “ค้นหา” เพื่อดูข้อมูลสมุนไพร")
image = Image.open('3.1B.jpg')
st.image(image)

st.write("___________________________________________________________________________________________________________________________________________________________________")
st.markdown('<p class="big-text"><b>รูปภาพ</b></p>', unsafe_allow_html=True)
st.write("1.	คลิกที่ชื่อใต้รูปสมุนไพรเพื่อดูข้อมูลของสมุนไพร")

image = Image.open('4B.jpg')
st.image(image)

st.write("___________________________________________________________________________________________________________________________________________________________________")
st.markdown('<p class="big-text"><b>เช็คข้อมูลสมุนไพร</b></p>', unsafe_allow_html=True)
st.write("1.	คลิกเมนู “Check Herb” หรือปุ่ม “เช็คข้อมูลสมุนไพร” เพื่อไปยังหน้าเช็คข้อมูลสมุนไพร")
image = Image.open('5B.jpg')
st.image(image)
image = Image.open('5.1.png')
st.image(image)

st.write("2. 	นำเข้าข้อมูล")
st.write("ㅤㅤ","2.1    ㅤคลิกปุ่ม “Browse files” เพื่อนำรูปที่ต้องการตรวจสอบเข้าระบบ")
image = Image.open('6B.jpg')
st.image(image)
st.write("ㅤㅤ","2.2	ㅤหากต้องการเปลี่ยนรูปสามารถคลิก “Browse files” เพื่อเลือกรูปใหม่")
st.write("ㅤㅤ","2.3	ㅤคลิกปุ่ม “ตรวจสอบ” เพื่อเป็นการยืนยัน ระบบจะนำรูปที่ใส่เข้ามาไปตรวจสอบ")
image = Image.open('6.1B.jpg')
st.image(image)
st.write("3.	แสดงข้อมูล")
st.write("ㅤㅤ","3.1	ㅤชื่อสมุนไพร")
st.write("ㅤㅤ","3.2	ㅤค่าความแม่นยำ")
st.write("ㅤㅤ","3.3	ㅤดูรายละเอียดเพิ่มเติม ")
st.write("4.	หลังจากระบบตรวจสอบเสร็จหากต้องการดูรายละเอียดเพิ่มเติมคลิก “ดูข้อมูลสมุนไพร”")

image = Image.open('7B.jpg')
st.image(image)

st.write("___________________________________________________________________________________________________________________________________________________________________")
st.markdown('<p class="big-text"><b>รายละเอียดสมุนไพร</b></p>', unsafe_allow_html=True)
st.write("1.    แสดงข้อมูล")
st.write("ㅤㅤ","1.1	ㅤรูปภาพ")
st.write("ㅤㅤ","ㅤㅤ","1.1.1	ㅤรูปภาพสมุนไพร")
st.write("ㅤㅤ","ㅤㅤ","1.1.2	ㅤชื่อสมุนไพร")
st.write("ㅤㅤ","1.2	ㅤข้อมูลสมุนไพร")
st.write("ㅤㅤ","ㅤㅤ","1.2.1	ㅤชื่อภาษาไทย")
st.write("ㅤㅤ","ㅤㅤ","1.2.2	ㅤชื่อวิทยาศาสตร์")
st.write("ㅤㅤ","ㅤㅤ","1.2.3	ㅤชื่อท้องถิ่น")
st.write("ㅤㅤ","ㅤㅤ","1.2.4	ㅤรสและสรรพคุณ")

image = Image.open('8B.jpg')
st.image(image)

st.write("___________________________________________________________________________________________________________________________________________________________________")
col1, col2  = st.columns(2)
with col1:
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 120px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 50px;
            white-space: nowrap;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/' target="_blank"><button class="button-1"><b>🍀 หน้าหลัก</b></button></a>
'''
    st.components.v1.html(button_html, height=50)

with col2:
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 110px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 50px;
            white-space: nowrap;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Check_Herb' target="_blank"><button class="button-1"><b>🔎 เช็คสมุนไพร</b></button></a>
'''
    st.components.v1.html(button_html, height=50)



