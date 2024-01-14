# Mengimpor library
import pandas as pd
import streamlit as st
import pickle
from PIL import Image

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Membuat judul
st.title('Prediksi Breast Cancer')

# Menambah subheader
st.subheader('Selamat datang di Model Prediksi Breast Cancer')

image = Image.open('feature importance 2.png')
st.image(image, use_column_width=True)

# Menulis text (ukuran kecil)
st.write('Grafik di atas adalah capture dari feature importance')

# Load model
my_model = pickle.load(open('model_prediksi_breast_cancer5.pkl', 'rb'))


# Menulis text (ukuran kecil)
st.subheader('Silahkan masukkan data Pasien')

# Baris Pertama
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        concave_points_worst = st.number_input('concave_points_worst', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    with col2:
        radius_worst = st.number_input('radius_worst', value=1012)

#Baris Kedua
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        concave_points_mean = st.number_input('concave_points_mean', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    with col2:
        perimeter_worst = st.number_input('perimeter_worst', value=1012)        

# Baris Ketiga
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        texture_worst = st.number_input('texture_worst', value=1012)
    with col2:
        area_worst = st.number_input('area_worst', value=1012)
        

# Baris Keempat
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        concavity_worst = st.number_input('concavity_worst', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    with col2:
        area_mean = st.number_input('area_mean', value=1012)
        

# Baris Kelima
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        smoothness_worst = st.number_input('smoothness_worst', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    with col2:
        concavity_mean = st.number_input('concavity_mean', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    
#code untuk prediksi
cancer_diagnosis =[]

#membuat tombol prediksi

if st.button('Tes Prediksi Keganasan Breast Cancer'):
    cancer_predict = my_model.predict([[concave_points_worst,radius_worst,concave_points_mean,perimeter_worst,texture_worst,area_worst,concavity_worst,area_mean,smoothness_worst,concavity_mean]])

    if (cancer_predict[0] == 1):
        cancer_diagnosis = 'Cancer Ganas'
    else :
        cancer_diagnosis = 'Cancer  Jinak'
        
    st.success(cancer_diagnosis)