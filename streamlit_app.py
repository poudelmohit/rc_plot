import streamlit as st
from RamachanDraw import fetch, phi_psi, plot
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Ramachandran Plot Generator")

# PDB id to be downloaded
PDB_id = st.text_input("Enter the protein id(pdb id): ")

# Fetch the PDB file for the given ID
pdb_file = fetch(PDB_id)

# Generate the plot using Matplotlib
plt.figure()
plot(pdb_file)

# Display the plot in the Streamlit app using st.pyplot
st.pyplot()
