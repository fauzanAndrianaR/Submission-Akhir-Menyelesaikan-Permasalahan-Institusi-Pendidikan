import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #007bff;
        margin: 0.5rem 0;
    }
    .success-card {
        background: linear-gradient(135deg, #28a745, #20c997);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .danger-card {
        background: linear-gradient(135deg, #dc3545, #fd7e14);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stSelectbox > div > div {
        border-radius: 10px;
    }
    .stNumberInput > div > div {
        border-radius: 10px;
    }
    .stSlider > div > div {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Load model dan scaler
@st.cache_resource
def load_models():
    try:
        model = joblib.load('model_logreg.pkl')
        scaler = joblib.load('scaler.pkl')
        return model, scaler
    except FileNotFoundError:
        st.error("⚠️ File model atau scaler tidak ditemukan. Pastikan file 'model_logreg.pkl' dan 'scaler.pkl' tersedia.")
        st.stop()

@st.cache_data
def load_sample_data():
    try:
        return pd.read_csv('df_student_labeled.csv')
    except FileNotFoundError:
        st.error("⚠️ File 'df_student_labeled.csv' tidak ditemukan.")
        st.stop()

model, scaler = load_models()
df_sample = load_sample_data()

# Header utama
st.markdown("""
<div class="main-header">
    <h1>🎓 Sistem Prediksi Dropout Mahasiswa</h1>
    <p>Menggunakan Machine Learning untuk memprediksi status mahasiswa</p>
</div>
""", unsafe_allow_html=True)

# Sidebar untuk informasi
with st.sidebar:
    st.header("📊 Informasi Sistem")
    st.info("""
    **Model**: Logistic Regression  
    **Akurasi**: Diestimasi > 85%  
    **Dataset**: Data mahasiswa dengan berbagai faktor  
    """)
    
    st.header("📋 Petunjuk Penggunaan")
    st.markdown("""
    1. Isi semua field yang diperlukan
    2. Klik tombol **Prediksi** 
    3. Lihat hasil klasifikasi
    4. Gunakan insights untuk pengambilan keputusan
    """)
    
    st.header("🔍 Quick Stats")
    if len(df_sample) > 0:
        total_students = len(df_sample)
        st.metric("Total Sampel Data", f"{total_students:,}")
        
        if 'Target' in df_sample.columns:
            dropout_rate = (df_sample['Target'] == 'Dropout').mean() * 100
            st.metric("Tingkat Dropout", f"{dropout_rate:.1f}%")

# Layout utama dengan kolom
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Input Data Mahasiswa")
    
    # Tabs untuk kategori input
    tab1, tab2, tab3, tab4 = st.tabs(["👤 Data Pribadi", "🎓 Data Akademik", "👨‍👩‍👧‍👦 Data Keluarga", "📈 Data Ekonomi"])
    
    with tab1:
        st.subheader("Informasi Pribadi")
        col_a, col_b = st.columns(2)
        
        with col_a:
            marital_status = st.selectbox(
                "Status Pernikahan", 
                df_sample['Marital_status'].unique(),
                help="Status pernikahan mahasiswa saat ini"
            )
            
            application_mode = st.selectbox(
                "Mode Aplikasi", 
                df_sample['Application_mode'].unique(),
                help="Cara mahasiswa mendaftar ke universitas"
            )
        
        with col_b:
            application_order = st.slider(
                "Urutan Aplikasi", 
                1, 10, 1,
                help="Urutan prioritas saat mendaftar"
            )
    
    with tab2:
        st.subheader("Informasi Akademik")
        col_c, col_d = st.columns(2)
        
        with col_c:
            course = st.selectbox(
                "Program Studi", 
                df_sample['Course'].unique(),
                help="Program studi yang diambil"
            )
            
            attendance = st.selectbox(
                "Waktu Kuliah", 
                df_sample['Daytime_evening_attendance'].unique(),
                help="Jadwal kuliah (siang/malam)"
            )
            
            prev_qualification = st.selectbox(
                "Kualifikasi Sebelumnya", 
                df_sample['Previous_qualification'].unique(),
                help="Tingkat pendidikan sebelum masuk universitas"
            )
        
        with col_d:
            prev_grade = st.number_input(
                "Nilai Kualifikasi Sebelumnya", 
                min_value=0.0, max_value=200.0, step=0.1, value=120.0,
                help="Nilai dari pendidikan sebelumnya"
            )
            
            uc2_eval = st.number_input(
                "Evaluasi Semester 2", 
                min_value=0, max_value=30, value=6,
                help="Jumlah mata kuliah yang dievaluasi"
            )
            
            uc2_approved = st.number_input(
                "Lulus Semester 2", 
                min_value=0, max_value=30, value=6,
                help="Jumlah mata kuliah yang lulus"
            )
            
            uc2_grade = st.number_input(
                "Rata-rata Nilai Semester 2", 
                min_value=0.0, max_value=20.0, value=12.0,
                help="Rata-rata nilai semester 2"
            )
    
    with tab3:
        st.subheader("Informasi Keluarga")
        col_e, col_f = st.columns(2)
        
        with col_e:
            mother_edu = st.selectbox(
                "Pendidikan Ibu", 
                df_sample['Mothers_qualification'].unique(),
                help="Tingkat pendidikan tertinggi ibu"
            )
        
        with col_f:
            father_edu = st.selectbox(
                "Pendidikan Ayah", 
                df_sample['Fathers_qualification'].unique(),
                help="Tingkat pendidikan tertinggi ayah"
            )
    
    with tab4:
        st.subheader("Indikator Ekonomi")
        col_g, col_h, col_i = st.columns(3)
        
        with col_g:
            inflation = st.number_input(
                "Tingkat Inflasi (%)", 
                value=1.0, step=0.1,
                help="Tingkat inflasi saat mahasiswa kuliah"
            )
        
        with col_h:
            gdp = st.number_input(
                "Nilai GDP (%)", 
                value=1.0, step=0.1,
                help="Pertumbuhan GDP"
            )
        
        with col_i:
            unemployment = st.number_input(
                "Tingkat Pengangguran (%)", 
                value=10.0, step=0.1,
                help="Tingkat pengangguran di wilayah tersebut"
            )

# Tombol prediksi dengan styling khusus
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button(
        "🔍 Prediksi Status Mahasiswa", 
        use_container_width=True,
        type="primary"
    )

# Kolom kedua untuk hasil
with col2:
    st.header("📊 Hasil Prediksi")
    
    # Placeholder untuk hasil
    result_placeholder = st.empty()
    insights_placeholder = st.empty()

# Proses prediksi
if predict_button:
    with st.spinner("Sedang memproses prediksi..."):
        try:
            # Buat dataframe input
            input_data = pd.DataFrame({
                'Marital_status': [marital_status],
                'Application_mode': [application_mode],
                'Application_order': [application_order],
                'Course': [course],
                'Daytime_evening_attendance': [attendance],
                'Previous_qualification': [prev_qualification],
                'Previous_qualification_grade': [prev_grade],
                'Mothers_qualification': [mother_edu],
                'Fathers_qualification': [father_edu],
                'Curricular_units_2nd_sem_evaluations': [uc2_eval],
                'Curricular_units_2nd_sem_approved': [uc2_approved],
                'Curricular_units_2nd_sem_grade': [uc2_grade],
                'Inflation_rate': [inflation],
                'GDP': [gdp],
                'Unemployment_rate': [unemployment]
            })

            # One-hot encoding
            input_data = pd.get_dummies(input_data)

            # Sesuaikan kolom
            model_features = scaler.feature_names_in_
            for col in model_features:
                if col not in input_data.columns:
                    input_data[col] = 0
            input_data = input_data[model_features]

            # Standarisasi
            input_scaled_array = scaler.transform(input_data)
            input_scaled = pd.DataFrame(input_scaled_array, columns=model_features)

            # Prediksi
            prediction = model.predict(input_scaled)[0]

            # Tampilkan hasil di kolom kedua
            with result_placeholder.container():
                if prediction == 1:
                    st.markdown(f"""
                    <div class="danger-card">
                        <h2>❌ DROPOUT</h2>
                        <h3>Mahasiswa diprediksi akan dropout</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Recommendations untuk dropout
                    st.subheader("🎯 Rekomendasi Tindakan")
                    st.warning("""
                    **Tindakan yang Diperlukan:**
                    - Konseling akademik intensif
                    - Program mentoring khusus
                    - Evaluasi beban akademik
                    - Dukungan finansial jika diperlukan
                    - Monitoring progress bulanan
                    """)
                else:
                    st.markdown(f"""
                    <div class="success-card">
                        <h2>✅ LULUS</h2>
                        <h3>Mahasiswa diprediksi akan lulus</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Recommendations untuk graduate
                    st.subheader("🎯 Rekomendasi Tindakan")
                    st.success("""
                    **Pertahankan Performa:**
                    - Monitoring rutin progress
                    - Dukungan pengembangan karir
                    - Program pengayaan akademik
                    - Persiapan transisi ke dunia kerja
                    - Keterlibatan dalam aktivitas kampus
                    """)

            # Insights tambahan
            with insights_placeholder.container():
                st.subheader("💡 Analisis Faktor")
                
                # Analisis faktor penting
                factors = []
                
                if uc2_approved < uc2_eval * 0.7:
                    factors.append("📚 Tingkat kelulusan mata kuliah semester 2 rendah")
                
                if uc2_grade < 10:
                    factors.append("📉 Rata-rata nilai semester 2 di bawah standar")
                
                if unemployment > 15:
                    factors.append("💼 Tingkat pengangguran tinggi di wilayah")
                
                if prev_grade < 100:
                    factors.append("🎓 Nilai kualifikasi sebelumnya relatif rendah")
                
                if factors:
                    st.info("**Faktor yang Perlu Diperhatikan:**")
                    for factor in factors:
                        st.write(f"- {factor}")
                else:
                    st.success("✅ Tidak ada faktor negatif yang signifikan teridentifikasi")
                
                # Metrics tambahan
                col_m1, col_m2, col_m3 = st.columns(3)
                
                with col_m1:
                    success_rate = uc2_approved / max(uc2_eval, 1) * 100
                    st.metric("Tingkat Kelulusan MK", f"{success_rate:.1f}%")
                
                with col_m2:
                    grade_performance = "Baik" if uc2_grade >= 12 else "Perlu Perbaikan"
                    st.metric("Performa Nilai", grade_performance)
                
                with col_m3:
                    academic_load = "Tinggi" if uc2_eval > 8 else "Normal"
                    st.metric("Beban Akademik", academic_load)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat prediksi: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🎓 Sistem Prediksi Dropout Mahasiswa </p>
</div>
""", unsafe_allow_html=True)