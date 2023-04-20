import streamlit as st
import numpy as np 
import cv2
from PIL import Image
import tensorflow as tf




st.set_page_config(
    page_title="Herb Detchtion", page_icon="🔎",)

#st.sidebar.success("↑↑↑ เลือกเมนู ↑↑↑")

model = tf.keras.models.load_model("saved_model/ProjectHerb2_11_0D11.h5",compile=False)

st.markdown("<h2 style='text-align: center; color:#3B130C ;'>ตรวจสอบสมุนไพร</h2>", unsafe_allow_html=True)
st.write("")
st.write("")

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
            padding: 10px 100px;
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
    <a href='http://localhost:8501/%E0%B8%84%E0%B8%B9%E0%B9%88%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99' target="_blank"><button class="button-1"><b>📖 คู่มือการใช้งาน</b></button></a>
'''
    st.components.v1.html(button_html, height=50)

st.write("___________________________________________________________________________________________________________________________________________________________________")


st.write("<p style='text-align: left; color:#3B130C ;'><h4><b>เลือกรูปภาพเพื่อตรวจสอบ</b></h4></p>", unsafe_allow_html=True)
st.write("<p style='text-align: left; color:#3B130C ;'>(เพื่อการตรวจสอบที่ถูกต้องควรใช้ภาพรูปใบไม้ในลักษณะเต็มใบและเห็นหน้าใบอย่างชัดเจน)</p>", unsafe_allow_html=True)

st.write("")
st.write("<p style='text-align: left; color:#3B130C ;'><b>ตัวอย่างรูปภาพที่จะนำมาตรวจสอบ</b></p>", unsafe_allow_html=True)

col4,col5,col6 = st.columns(3)
with col4:
    image = Image.open('p1.jpg')
    st.image(image, width=200)
with col5:
    image = Image.open('p3.jpg')
    st.image(image, width=200)
with col6:
    image = Image.open('p2.jpg')
    st.image(image, width=200)


uploaded_file = st.file_uploader("", type=["png","jpg","jpeg"])

class_names = ['กะเพราแดง','การบูร','ขมิ้นอ้อย','ข่า','จำปา','จำปี','ชมนาด','น้อยหน่า','บัวบก','ฝรั่ง','พริกไทย','พลู','พุดซ้อน','พุทรา','ฟ้าทะลายโจร','มะกรูด','มะตูม','มะนาว','มะระขี้นก','ย่านาง','รางจืด',
 'ว่านหางจระเข้','สะระแหน่','สะระแหน่ญี่ปุ่น','เสลดพังพอนตัวเมีย']

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(256,256))
    resized = np.array(resized)
    resized = np.expand_dims(resized,0)
    # Now do something with the image! For example, let's display it:
    st.image(resized, channels="RGB")

    Genrate_pred = st.button("ตรวจสอบ") 
    st.write("___________________________________________________________________________________________________________________________________________________________________")
    if Genrate_pred:
        prediction = model.predict(resized)#.argmax()
        top_n = 5
        top_indices = prediction.argsort()[0][-top_n:]
        top_values = prediction[0][top_indices]
        for i in range(top_n):
            idx = top_indices[top_n - 1 - i]
            class_name = class_names[idx]
            confidence = round(top_values[top_n - 1 - i] * 100, 2)
            if confidence > 0:
                class_name = class_names[idx]
                check_data=" [ดูข้อมูลสมุนไพร](http://localhost:8501/Data?class_name={})".format(class_name)
                st.set_option('client.caching', False)
                col1,col2,col3 = st.columns(3)
                with col1:
                    st.write("สมุนไพร : {} ".format(class_name))
                with col2:
                    st.write("ค่าความแม่นยำ  : {} ".format(confidence),"%")
                with col3:
                    st.write(check_data)
               
                #st.write("สมุนไพร : {} ".format(class_name) ," | ค่าความแม่นยำ  : {} ".format(confidence),"%",check_data)
                           
