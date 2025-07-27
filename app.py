import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="E. coli GFP Simulator", layout="centered")

st.title("🧬 E. coli GFP Simulator")
st.write("Explore how DNA sequences control protein production!")

# Parameters
alpha = st.slider("Promoter Strength (α)", 0.0, 5.0, 1.0, step=0.1)
use_repressor = st.checkbox("Apply Repressor (stops transcription)", value=False)
delta = 0.5  # GFP degradation rate
dt = 0.1
t_max = 20

# Apply repressor
if use_repressor:
    alpha = 0

# Simulation
times = np.arange(0, t_max, dt)
gfp_levels = []
gfp = 0
for t in times:
    dgfp = alpha - delta * gfp
    gfp += dgfp * dt
    gfp_levels.app_
