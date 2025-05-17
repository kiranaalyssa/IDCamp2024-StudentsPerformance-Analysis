import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model/students_performance_model.pkl')

# Judul Aplikasi
st.title("🎓 Smart Predictor: Status Mahasiswa Lulus atau Tidak?")
st.markdown("Masukkan data akademik dan personal mahasiswa untuk memprediksi apakah mahasiswa akan **Dropout**, **Tetap Enrolled**, atau **Lulus (Graduate)** berdasarkan model machine learning.")

# ================================
# 🧑‍🎓 DATA PRIBADI & LATAR BELAKANG
st.header("🧾 Data Pribadi & Latar Belakang")
Marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4, 5, 6])
Application_mode = st.text_input("Metode pendaftaran yang digunakan", placeholder="Isi Angka")
Application_order = st.text_input("Urutan program studi yang didaftarkan", placeholder="Isi Angka")
Course = st.text_input("Kode Program Studi", placeholder="Isi Angka")
Daytime_evening_attendance = st.selectbox("Jenis Perkuliahan", [0, 1])
Previous_qualification = st.selectbox("Kualifikasi Sebelumnya", [1, 2, 3, 4, 5])
Previous_qualification_grade = st.text_input("Nilai Kualifikasi sebelumnya", placeholder="Isi Angka")
Nacionality = st.text_input("Kewarganegaraan", placeholder="Isi Angka")
Mothers_qualification = st.text_input("Pendidikan Ibu", placeholder="Isi Angka")
Fathers_qualification = st.text_input("Pendidikan Ayah", placeholder="Isi Angka")
Mothers_occupation = st.text_input("Pekerjaan Ibu", placeholder="Isi Angka")
Fathers_occupation = st.text_input("Pekerjaan Ayah", placeholder="Isi Angka")
Admission_grade = st.text_input("Nilai Masuk", placeholder="Isi Nilai")
Displaced = st.selectbox("Mahasiswa Pindahan?", [0, 1])
Educational_special_needs = st.selectbox("Kebutuhan Khusus", [0, 1])
Debtor = st.selectbox("Punya Hutang?", [0, 1])
Tuition_fees_up_to_date = st.selectbox("Pembayaran Kuliah Lancar?", [0, 1])
Gender = st.selectbox("Jenis Kelamin", [0, 1])
Scholarship_holder = st.selectbox("Penerima Beasiswa?", [0, 1])
Age_at_enrollment = st.number_input("Umur Saat Masuk", 15, 100, value=18)
International = st.selectbox("Mahasiswa Internasional?", [0, 1])

st.markdown("---")

# ================================
# NILAI AKADEMIK SEMESTER 1 & 2
st.header("📚 Nilai Akademik Mahasiswa")
st.subheader("Semester 1")
Curricular_units_1st_sem_credited = st.text_input("SKS Diakui Sem 1", placeholder="Isi Angka")
Curricular_units_1st_sem_enrolled = st.text_input("SKS Diambil Sem 1", placeholder="Isi Angka")
Curricular_units_1st_sem_evaluations = st.text_input("Evaluasi Sem 1", placeholder="Isi Angka")
Curricular_units_1st_sem_approved = st.text_input("SKS Lulus Sem 1", placeholder="Isi Angka")
Curricular_units_1st_sem_grade = st.text_input("IPK Sem 1", placeholder="Isi Nilai")
Curricular_units_1st_sem_without_evaluations = st.text_input("Tanpa Evaluasi Sem 1", placeholder="Isi Angka")


st.subheader("Semester 2")
Curricular_units_2nd_sem_credited = st.text_input("SKS Diakui Sem 2", placeholder="Isi Angka")
Curricular_units_2nd_sem_enrolled = st.text_input("SKS Diambil Sem 2", placeholder="Isi Angka")
Curricular_units_2nd_sem_evaluations = st.text_input("Evaluasi Sem 2", placeholder="Isi Angka")
Curricular_units_2nd_sem_approved = st.text_input("SKS Lulus Sem 2", placeholder="Isi Angka")
Curricular_units_2nd_sem_grade = st.text_input("IPK Sem 2", placeholder="Isi Nilai")
Curricular_units_2nd_sem_without_evaluations = st.text_input("Tanpa Evaluasi Sem 2", placeholder="Isi Angka")

st.markdown("---")

# ================================
# KONDISI EKONOMI
st.header("📉 Kondisi Ekonomi")
Unemployment_rate = st.text_input("Tingkat Pengangguran", placeholder="Isi Angka")
Inflation_rate = st.text_input("Tingkat Inflasi", placeholder="Isi Angka")
GDP = st.text_input("GDP Negara", placeholder="Isi Angka")

# ================================
# DataFrame untuk prediksi
input_df = pd.DataFrame([[
    Marital_status, Application_mode, Application_order, Course, Daytime_evening_attendance,
    Previous_qualification, Previous_qualification_grade, Nacionality,
    Mothers_qualification, Fathers_qualification, Mothers_occupation, Fathers_occupation,
    Admission_grade, Displaced, Educational_special_needs, Debtor, Tuition_fees_up_to_date,
    Gender, Scholarship_holder, Age_at_enrollment, International,
    Curricular_units_1st_sem_credited, Curricular_units_1st_sem_enrolled,
    Curricular_units_1st_sem_evaluations, Curricular_units_1st_sem_approved,
    Curricular_units_1st_sem_grade, Curricular_units_1st_sem_without_evaluations,
    Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_enrolled,
    Curricular_units_2nd_sem_evaluations, Curricular_units_2nd_sem_approved,
    Curricular_units_2nd_sem_grade, Curricular_units_2nd_sem_without_evaluations,
    Unemployment_rate, Inflation_rate, GDP
]], columns=[
    'Marital_status', 'Application_mode', 'Application_order', 'Course', 'Daytime_evening_attendance',
    'Previous_qualification', 'Previous_qualification_grade', 'Nacionality',
    'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
    'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date',
    'Gender', 'Scholarship_holder', 'Age_at_enrollment', 'International',
    'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
    'Unemployment_rate', 'Inflation_rate', 'GDP'
])

if st.button("🔍 Prediksi Status Mahasiswa"):
    prediction = model.predict(input_df)[0]
    label_map = {
        0: 'Dropout ❌',
        1: 'Enrolled ✅',
        2: 'Graduate 🎓'
    }
    st.success(f"Hasil prediksi: **{label_map[prediction]}**")