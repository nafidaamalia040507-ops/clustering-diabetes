import streamlit as st
import pandas as pd

def steps_kmeans():
    st.subheader("Langkah-langkah Metode K-Means")

    df_steps = pd.DataFrame({
        "Langkah": [
            "Menentukan jumlah cluster (K)",
            "Inisialisasi centroid awal",
            "Menghitung jarak data ke centroid",
            "Pengelompokan data",
            "Pembaruan centroid",
            "Iterasi hingga konvergen",
            "Evaluasi hasil clustering"
        ],
        "Deskripsi": [
            "Menentukan jumlah cluster berdasarkan tujuan analisis",
            "Centroid awal ditentukan secara acak oleh algoritma",
            "Menggunakan jarak Euclidean untuk mengukur kedekatan data",
            "Data dimasukkan ke cluster dengan jarak terdekat",
            "Centroid diperbarui dari rata-rata anggota cluster",
            "Iterasi berhenti ketika centroid tidak berubah signifikan",
            "Evaluasi dilakukan menggunakan silhouette score"
        ]
    })

    st.table(df_steps)
