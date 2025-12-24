import streamlit as st

def interpretasi_hasil():
    st.subheader("Interpretasi Hasil Clustering")

    st.markdown("""
    **K-Means**  
    K-Means menghasilkan pemisahan cluster yang cukup jelas dengan nilai Silhouette Score yang relatif tinggi, menunjukkan bahwa metode ini efektif dalam mengelompokkan data diabetes agregat.

    **Gaussian Mixture Model (GMM)**  
    GMM mempertimbangkan distribusi probabilistik data sehingga mampu menangkap variasi pola antar cluster dengan baik.

    **Hierarchical Clustering**  
    Metode hierarchical membentuk struktur cluster bertingkat yang memberikan gambaran hubungan antar data.

    **MeanShift**  
    MeanShift menentukan jumlah cluster secara otomatis berdasarkan kepadatan data, sehingga hasil clustering bersifat fleksibel.

    **Spectral Clustering**  
    Spectral Clustering mampu mengidentifikasi hubungan non-linear dalam data diabetes.
    """)
