import streamlit as st
import pandas as pd

def about_dataset():
    st.subheader("Deskripsi Dataset")

    st.write("""
    Dataset yang digunakan merupakan data diabetes agregat per negara.
    Data ini berisi informasi jumlah penderita diabetes yang direpresentasikan
    melalui nilai rata-rata, minimum, dan maksimum.
    """)

    st.write("""
    **Variabel dalam dataset:**
    - SpatialDimensionValueCode : Kode negara
    - diabetes_mean : Rata-rata jumlah penderita diabetes
    - diabetes_min : Nilai minimum jumlah penderita diabetes
    - diabetes_max : Nilai maksimum jumlah penderita diabetes
    - Country : Region negara
    """)

    df = pd.read_csv("diabetes_aggregated.csv")
    st.dataframe(df.head())
