import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def chart():
    st.subheader("Visualisasi Clustering (K-Means)")

    df = pd.read_csv("diabetes_aggregated.csv")

    plt.figure()
    plt.scatter(df['diabetes_mean'], df['diabetes_max'])
    plt.xlabel("Diabetes Mean")
    plt.ylabel("Diabetes Max")
    st.pyplot(plt)
