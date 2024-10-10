import streamlit as st

st.title("🎈 My new app")
st.write(
    "Embedding Analyzer"

    "Projector"

    "Boost and Pruning"
)

#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import glob

#######################
# # Page configuration
# st.set_page_config(
#     page_title="Embeddings Analyzer",
#     layout="wide",
#     initial_sidebar_state="expanded")

# alt.themes.enable("dark")


#######################
# Load data
# df = pd.read_csv('data/nwu_inference_slim.csv')
# #df = df_reshaped

#######################
# Sidebar
with st.sidebar:
    
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)


