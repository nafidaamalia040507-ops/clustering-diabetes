import streamlit as st

st.header("Clustering Analysis of Diabetes Data")
st.write("Analisis Clustering Data Diabetes Agregat per Negara")
st.write("Universitas Muhammadiyah Semarang")

# ======================
# TAB DEFINITION
# ======================
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "About Dataset",
    "Dashboard",
    "Clustering & Evaluation",
    "Analysis Steps",
    "Interpretation",
    "steps kmeans",
    "Contact Me"
])

# ======================
# TAB 1 – ABOUT DATASET
# ======================
with tab1:
    import about
    about.about_dataset()

# ======================
# TAB 2 – DASHBOARD
# ======================
with tab2:
    import visualisasi
    visualisasi.chart()

# ======================
# TAB 3 – CLUSTERING & EVALUATION
# ======================
with tab3:
    import machine_learning
    machine_learning.clustering_models()

# ======================
# TAB 4 – ANALYSIS STEPS
# ======================
with tab4:
    import steps
    steps.analysis_steps()

# ======================
# TAB 5 – INTERPRETATION
# ======================
with tab5:
    import interpretasi
    interpretasi.interpretasi_hasil()

with tab6:
    import visualisasi
    import steps_kmeans

    visualisasi.chart()
    steps_kmeans.steps_kmeans()

# ======================
# TAB 7 – CONTACT ME
# ======================
with tab7:
    import kontak
    kontak.contact_me()
