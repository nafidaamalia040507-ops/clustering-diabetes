import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import (
    KMeans,
    AgglomerativeClustering,
    MeanShift,
    SpectralClustering
)
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score


def clustering_models():
    st.header("Clustering Models & Evaluation")

    # =====================
    # LOAD DATA
    # =====================
    df = pd.read_csv("diabetes_aggregated.csv")

    features = df[[
        "diabetes_mean",
        "diabetes_min",
        "diabetes_max"
    ]]

    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    results = []

    # =====================
    # K-MEANS
    # =====================
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels_km = kmeans.fit_predict(X)
    sil_km = silhouette_score(X, labels_km)

    results.append(["K-Means", len(set(labels_km)), sil_km])

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=labels_km)
    ax.set_title("K-Means Clustering")
    st.pyplot(fig)

    # =====================
    # GMM
    # =====================
    gmm = GaussianMixture(n_components=3, random_state=42)
    labels_gmm = gmm.fit_predict(X)
    sil_gmm = silhouette_score(X, labels_gmm)

    results.append(["GMM", len(set(labels_gmm)), sil_gmm])

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=labels_gmm)
    ax.set_title("Gaussian Mixture Model")
    st.pyplot(fig)

    # =====================
    # HIERARCHICAL
    # =====================
    hier = AgglomerativeClustering(n_clusters=3)
    labels_hc = hier.fit_predict(X)
    sil_hc = silhouette_score(X, labels_hc)

    results.append(["Hierarchical", len(set(labels_hc)), sil_hc])

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=labels_hc)
    ax.set_title("Hierarchical Clustering")
    st.pyplot(fig)

    # =====================
    # MEAN SHIFT
    # =====================
    ms = MeanShift()
    labels_ms = ms.fit_predict(X)

    if len(set(labels_ms)) > 1:
        sil_ms = silhouette_score(X, labels_ms)
    else:
        sil_ms = None

    results.append(["MeanShift", len(set(labels_ms)), sil_ms])

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=labels_ms)
    ax.set_title("MeanShift Clustering")
    st.pyplot(fig)

    # =====================
    # SPECTRAL
    # =====================
    spectral = SpectralClustering(
        n_clusters=3,
        affinity="nearest_neighbors",
        random_state=42
    )
    labels_sc = spectral.fit_predict(X)
    sil_sc = silhouette_score(X, labels_sc)

    results.append(["Spectral", len(set(labels_sc)), sil_sc])

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=labels_sc)
    ax.set_title("Spectral Clustering")
    st.pyplot(fig)

    # =====================
    # SILHOUETTE TABLE
    # =====================
    st.subheader("Silhouette Score Evaluation")

    eval_df = pd.DataFrame(
        results,
        columns=["Method", "Number of Clusters", "Silhouette Score"]
    )

    st.dataframe(eval_df)
