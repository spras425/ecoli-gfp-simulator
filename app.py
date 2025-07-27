import streamlit as st
import numpy as np

st.set_page_config(page_title="E. coli GFP Simulator (No Matplotlib)", layout="centered")

st.title("🧬 E. coli GFP Simulator (No Matplotlib)")
st.write("See how changing DNA controls glowing proteins!")

# Parameters
alpha = st.slider("Promoter Strength (α)", 0.0, 5.0, 1.0, step=0.1)
use_repressor = st.checkbox("Apply Repressor (stops transcription)", value=False)
delta = 0.5  # GFP degradation rate
dt = 0.1
t_max = 20

if use_repressor:
    alpha = 0

# Simulation
times = np.arange(0, t_max, dt)
gfp_levels = []
gfp = 0
for t in times:
    dgfp = alpha - delta * gfp
    gfp += dgfp * dt
    gfp_levels.append(gfp)

# Petri dish glow as colored block emoji with intensity
max_gfp = max(gfp_levels)
normalized_gfp = min(gfp_levels[-1] / 10, 1.0)  # normalize last GFP level

# Create glow intensity bar with green squares
glow_blocks = int(normalized_gfp * 10)
petri_display = "🟩" * glow_blocks + "⬜" * (10 - glow_blocks)

st.subheader("🧫 Petri Dish Glow Intensity")
st.markdown(f"<h2 style='color:green'>{petri_display}</h2>", unsafe_allow_html=True)
st.caption("More green blocks = stronger GFP glow")

# GFP Expression Graph using Streamlit line_chart
st.subheader("📈 GFP Protein Over Time")
st.line_chart(gfp_levels)

# Explanation
with st.expander("What’s Going On?"):
    st.markdown("""
- DNA in *E. coli* produces mRNA, which makes GFP protein.
- **Promoter strength (α)** controls how fast GFP is made.
- **Repressor** blocks the promoter — GFP stops being made.
- The green glow represents the amount of GFP in the cell.
- The math behind it:  
  `dGFP/dt = α - δ × GFP`
""")

