import streamlit as st
from PIL import Image
import numpy as np 

query_params = st.experimental_get_query_params()
class_name = query_params["class_name"][0] if "class_name" in query_params else None

st.set_page_config(
    page_title="HomePage", page_icon="🍀",)

#หัวข้อ
st.markdown("<h2 style='text-align: center; color: Black;'>รู้จำสมุนไพรจากภาพถ่าย</h2>", unsafe_allow_html=True)
st.write("")
st.write("")


#ปุ่มตัวเลือก
col1, col2  = st.columns(2)
with col1:
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
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Check_Herb' target="_blank"><button class="button-1"><b>🔎 เช็คสมุนไพร</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
with col2:
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 95px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 50px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/%E0%B8%84%E0%B8%B9%E0%B9%88%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99' target="_blank"><button class="button-1"><b>📖 คู่มือการใช้งาน</b></button></a>
'''
    st.components.v1.html(button_html, height=50)

st.write("___________________________________________________________________________________________________________________________________________________________________")

#กล่องเลือกข้อความ
options = [ '','กะเพราแดง', 'การบูร', 'ขมิ้นอ้อย','ข่า','จำปา','จำปี','ชมนาด','ชะเอมไทย','ช้าพลู','น้อยหน่า',
           'บอระเพ็ด','บัวบก','ฝรั่ง','พญาสัตบรรณ','พริกไทย','พลู','พุดซ้อน','พุทรา','ฟ้าทะลายโจร','มะกรูด',
           'มะตูม','มะนาว','มะระขี้นก','ย่านาง','รางจืด','ว่านหางจระเข้','เสลดพังพอนตัวเมีย','สะระแหน่','สะระแหน่ญี่ปุ่น','อบเชย']
selected_option = st.selectbox('', options)


if selected_option == 'กะเพราแดง':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9E%E0%B8%A3%E0%B8%B2%E0%B9%81%E0%B8%94%E0%B8%87' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'การบูร':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%B9%E0%B8%A3' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ขมิ้นอ้อย':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%82%E0%B8%A1%E0%B8%B4%E0%B9%89%E0%B8%99%E0%B8%AD%E0%B9%89%E0%B8%AD%E0%B8%A2' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ข่า':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%82%E0%B9%88%E0%B8%B2' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'จำปา':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%88%E0%B8%B3%E0%B8%9B%E0%B8%B2' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'จำปี':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%88%E0%B8%B3%E0%B8%9B%E0%B8%B5' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ชมนาด':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%8A%E0%B8%A1%E0%B8%99%E0%B8%B2%E0%B8%94' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ชะเอมไทย':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%8A%E0%B8%B0%E0%B9%80%E0%B8%AD%E0%B8%A1%E0%B9%84%E0%B8%97%E0%B8%A2' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ช้าพลู':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%8A%E0%B9%89%E0%B8%B2%E0%B8%9E%E0%B8%A5%E0%B8%B9' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'น้อยหน่า':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%99%E0%B9%89%E0%B8%AD%E0%B8%A2%E0%B8%AB%E0%B8%99%E0%B9%88%E0%B8%B2' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'บอระเพ็ด':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9A%E0%B8%AD%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9E%E0%B9%87%E0%B8%94' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'บัวบก':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9A%E0%B8%B1%E0%B8%A7%E0%B8%9A%E0%B8%81' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ฝรั่ง':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9D%E0%B8%A3%E0%B8%B1%E0%B9%88%E0%B8%87' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'พญาสัตบรรณ':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9E%E0%B8%8D%E0%B8%B2%E0%B8%AA%E0%B8%B1%E0%B8%95%E0%B8%9A%E0%B8%A3%E0%B8%A3%E0%B8%93' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'พริกไทย':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9E%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B9%84%E0%B8%97%E0%B8%A2' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'พลู':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9E%E0%B8%A5%E0%B8%B9' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'พุดซ้อน':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9E%E0%B8%B8%E0%B8%94%E0%B8%8B%E0%B9%89%E0%B8%AD%E0%B8%99' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'พุทรา':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9E%E0%B8%B8%E0%B8%97%E0%B8%A3%E0%B8%B2' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ฟ้าทะลายโจร':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9F%E0%B9%89%E0%B8%B2%E0%B8%97%E0%B8%B0%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B9%82%E0%B8%88%E0%B8%A3' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'มะกรูด':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%A1%E0%B8%B0%E0%B8%81%E0%B8%A3%E0%B8%B9%E0%B8%94' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'มะตูม':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%A1%E0%B8%B0%E0%B8%95%E0%B8%B9%E0%B8%A1' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'มะนาว':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%A1%E0%B8%B0%E0%B8%99%E0%B8%B2%E0%B8%A7' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'มะระขี้นก':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%A1%E0%B8%B0%E0%B8%A3%E0%B8%B0%E0%B8%82%E0%B8%B5%E0%B9%89%E0%B8%99%E0%B8%81' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ย่านาง':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%99%E0%B8%B2%E0%B8%87' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'รางจืด':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%A3%E0%B8%B2%E0%B8%87%E0%B8%88%E0%B8%B7%E0%B8%94' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'ว่านหางจระเข้':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%A7%E0%B9%88%E0%B8%B2%E0%B8%99%E0%B8%AB%E0%B8%B2%E0%B8%87%E0%B8%88%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%82%E0%B9%89' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'เสลดพังพอนตัวเมีย':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B9%80%E0%B8%AA%E0%B8%A5%E0%B8%94%E0%B8%9E%E0%B8%B1%E0%B8%87%E0%B8%9E%E0%B8%AD%E0%B8%99%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B9%80%E0%B8%A1%E0%B8%B5%E0%B8%A2' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'สะระแหน่':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%AA%E0%B8%B0%E0%B8%A3%E0%B8%B0%E0%B9%81%E0%B8%AB%E0%B8%99%E0%B9%88' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'สะระแหน่ญี่ปุ่น':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%AA%E0%B8%B0%E0%B8%A3%E0%B8%B0%E0%B9%81%E0%B8%AB%E0%B8%99%E0%B9%88%E0%B8%8D%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%B8%E0%B9%88%E0%B8%99' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)
elif selected_option == 'อบเชย':
    button_html = '''
    <style>
        .button-1 {
            background-color: #3B130C; /* Green */
            border: none;
            color: white;
            padding: 10px 325px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: auto;
            cursor: pointer;
            border-radius: 10px;
        }
        .button-1:hover {
            background-color: #F3885E;
        }
    </style>
    <a href='http://localhost:8501/Data?class_name=%E0%B8%9D%E0%B8%99%E0%B9%80%E0%B8%AA%E0%B8%99%E0%B8%AB%E0%B8%B2(%E0%B8%AD%E0%B8%9A%E0%B9%80%E0%B8%8A%E0%B8%A2)' target="_blank"><button class="button-1"><b>ค้นหา</b></button></a>
'''
    st.components.v1.html(button_html, height=50)

st.write("")
st.write("")
#รูปด้านล่าง

col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    class_name="กระเพราแดง"
    check_data=" [กะเพราแดง](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('กะเพราแดง.png')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤ",check_data," ")
with col2:
    st.header("")
with col3:
    class_name="การบูร"
    check_data=" [การบูร](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('การบูร.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col4:
    st.header("")
with col5:
    class_name="ขมิ้นอ้อย"
    check_data=" [ขมิ้นอ้อย](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ขมิ้นอ้อย.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤ",check_data," ")

st.write("")
st.write("")
col6,col7,col8,col9,col10 = st.columns(5)
with col6:
    class_name="ข่า"
    check_data=" [ข่า](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ข่า.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col7:
    st.header("")
with col8:
    class_name="จำปา"
    check_data=" [จำปา](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('จำปา.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col9:
    st.header("")
with col10:
    class_name="จำปี"
    check_data=" [จำปี](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('จำปี.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")

st.write("")
st.write("")
col11,col12,col13,col14,col15 = st.columns(5)
with col11:
    class_name="ชมนาด"
    check_data=" [ชมนาด](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ชมนาด.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col12:
    st.header("")
with col13:
    class_name="ชะเอมไทย"
    check_data=" [ชะเอมไทย](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ชะเอมไทย.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤ",check_data," ")
with col14:
    st.header("")
with col15:
    class_name="ช้าพลู"
    check_data=" [ช้าพลู](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ช้าพลู.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")

st.write("")
st.write("")
col16,col17,col18,col19,col20 = st.columns(5)
with col16:
    class_name="น้อยหน่า"
    check_data=" [น้อยหน่า](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('น้อยหน่า.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤ",check_data," ")
with col17:
    st.header("")
with col18:
    class_name="บอระเพ็ด"
    check_data=" [บอระเพ็ด](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('บอระเพ็ด.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤ",check_data," ")
with col19:
    st.header("")
with col20:
    class_name="บัวบก"
    check_data=" [บัวบก](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('บัวบก.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")

st.write("")
st.write("")
col21,col22,col23,col24,col25 = st.columns(5)
with col21:
    class_name="ฝรั่ง"
    check_data=" [ฝรั่ง](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ฝรั่ง.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col22:
    st.header("")
with col23:
    class_name="พญาสัตบรรณ"
    check_data=" [พญาสัตบรรณ](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('พญาสัตบรรณ.png')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤ",check_data," ")
with col24:
    st.header("")
with col25:
    class_name="พริกไทย"
    check_data=" [พริกไทย](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('พริกไทย.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")

st.write("")
st.write("")
col25,col26,col27,col28,col29 = st.columns(5)
with col25:
    class_name="พลู"
    check_data=" [พลู](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('พลู.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col26:
    st.header("")
with col27:
    class_name="พุดซ้อน"
    check_data=" [พุดซ้อน](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('พุดซ้อน.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤ",check_data," ")
with col28:
    st.header("")
with col29:
    class_name="พุทรา"
    check_data=" [พุทรา](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('พุทรา.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")

st.write("")
st.write("")
col30,col31,col32,col33,col34 = st.columns(5)
with col30:
    class_name="ฟ้าทะลายโจร"
    check_data=" [ฟ้าทะลายโจร](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ฟ้าทะลายโจร.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤ",check_data," ")
with col31:
    st.header("")
with col32:
    class_name="มะกรูด"
    check_data=" [มะกรูด](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('มะกรูด.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col33:
    st.header("")
with col34:
    class_name="มะตูม"
    check_data=" [มะตูม](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('มะตูม.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")

st.write("")
st.write("")
col35,col36,col37,col38,col39 = st.columns(5)
with col35:
    class_name="มะนาว"
    check_data=" [มะนาว](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('มะนาว.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col36:
    st.header("")
with col37:
    class_name="มะระขี้นก"
    check_data=" [มะระขี้นก](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('มะระขี้นก.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤ",check_data," ")
with col38:
    st.header("")
with col39:
    class_name="ย่านาง"
    check_data=" [ย่านาง](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ย่านาง.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")

st.write("")
st.write("")
col40,col41,col42,col43,col44 = st.columns(5)
with col40:
    class_name="รางจืด"
    check_data=" [รางจืด](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('รางจืด.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col41:
    st.header("")
with col42:
    class_name="ฝนเสนหา(อบเชย)"
    check_data=" [อบเชย](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ฝนสเหนหา(อบเชย).jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤㅤ",check_data," ")
with col43:
    st.header("")
with col44:
    class_name="ว่านหางจระเข้"
    check_data=" [ว่านหางจระเข้](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('ว่านหางจระเข้.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤ",check_data," ")

st.write("")
st.write("")
col45,col46,col47,col48,col49 = st.columns(5)
with col45:
    class_name="สะระแหน่"
    check_data=" [สะระแหน่](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('สะระแหน่.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤㅤ",check_data," ")
with col46:
    st.header("")
with col47:
    class_name="เสลดพังพอนตัวเมีย"
    check_data=" [เสลดพังพอนตัวเมีย](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('พญาปล้องทอง.png')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("",check_data," ")
with col48:
    st.header("")
with col49:
    class_name="สะระแหน่ญี่ปุ่น"
    check_data=" [สะระแหน่ญี่ปุ่น](http://localhost:8501/Data?class_name={})".format(class_name)
    st.set_option('client.caching', False)
    image = Image.open('สะระแหน่ญี่ปุ่น.jpg')
    resizedImg = image.resize((225, 325), Image.ANTIALIAS)
    st.image(resizedImg)
    st.write("ㅤ",check_data," ")



    
    