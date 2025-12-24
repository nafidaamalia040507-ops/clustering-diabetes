import streamlit as st

def analysis_steps():
    st.subheader("Langkah-Langkah Analisis")

    st.markdown("""
    Analisis clustering ini dilakukan melalui beberapa tahapan sistematis
    untuk memastikan hasil yang valid dan dapat diinterpretasikan dengan baik.
    Dataset yang digunakan bersumber dari **World Health Organization (WHO)**.
    """)

    st.markdown("""
    ### 1️⃣ Pengumpulan Data
    Data diperoleh dari World Health Organization (WHO) yang berisi informasi
    jumlah penderita diabetes di berbagai negara. Data yang digunakan merupakan
    data agregat per negara.
    """)

    st.markdown("""
    ### 2️⃣ Pemahaman dan Seleksi Variabel
    Variabel yang digunakan dalam analisis ini meliputi:
    - Rata-rata jumlah penderita diabetes (mean)
    - Nilai minimum jumlah penderita diabetes (min)
    - Nilai maksimum jumlah penderita diabetes (max)

    Variabel-variabel tersebut dipilih karena merepresentasikan karakteristik
    distribusi jumlah penderita diabetes di setiap negara.
    """)

    st.markdown("""
    ### 3️⃣ Praproses Data
    Pada tahap ini dilakukan:
    - Pemeriksaan data
    - Pemilihan variabel numerik
    - Normalisasi data menggunakan StandardScaler

    Normalisasi dilakukan agar setiap variabel memiliki skala yang sama
    sehingga tidak mendominasi proses clustering.
    """)

    st.markdown("""
    ### 4️⃣ Penerapan Metode Clustering
    Lima metode clustering digunakan dalam analisis ini, yaitu:
    - K-Means
    - Hierarchical Clustering
    - Gaussian Mixture Model (GMM)
    - MeanShift
    - Spectral Clustering

    Penggunaan beberapa metode bertujuan untuk membandingkan pola
    pengelompokan yang dihasilkan.
    """)

    st.markdown("""
    ### 5️⃣ Visualisasi Hasil
    Hasil clustering divisualisasikan dalam bentuk grafik untuk membantu
    interpretasi pola pengelompokan negara berdasarkan karakteristik diabetes.
    """)

    st.markdown("""
    ### 6️⃣ Interpretasi dan Kesimpulan
    Setiap cluster dianalisis untuk mengetahui karakteristik negara yang
    termasuk di dalamnya, seperti kelompok negara dengan tingkat diabetes
    rendah, sedang, dan tinggi.
    """)
