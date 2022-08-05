import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
# import base64
# import seaborn as sns
# import numpy as np

st.set_page_config(page_title="GEII", layout="wide")

st.title('[GEII](https://github.com/Leo-Poon-Lab/GEII)')

st.markdown("""
Host Gene Expression under Influenza virus infection or Interferon stimulation (GEII) database is a tool for studying host gene expression during influenza virus infection or interferon stimulation.
""")


st.sidebar.image("https://github.com/Leo-Poon-Lab/GEII/raw/main/logo.png", use_column_width=True)
st.sidebar.title('Input Features')
selected_gene_type = st.sidebar.radio('Gene Input Type', ["Entrez ID", "Gene Symbol"])
if selected_gene_type == "Entrez ID":
    selected_gene_id = st.sidebar.text_input('Gene Input', "672")
else:
    selected_gene_id = st.sidebar.text_input('Gene Input', "BRCA2")

selected_exp_type = st.sidebar.radio('Experiment Type', ["Infection", "Stimulation"])

# Web scraping of GEII results
@st.cache
def load_data(gene_type, gene_id, exp_type):
    if gene_type == "Entrez ID":
        if exp_type == "Infection":
            url = "https://raw.githubusercontent.com/Leo-Poon-Lab/GEII/main/data_entrez_id/hGEuIInf/" + str(gene_id) + ".csv"
        else:
            url = "https://raw.githubusercontent.com/Leo-Poon-Lab/GEII/main/data_entrez_id/hGEuISti/" + str(gene_id) + ".csv"
    else:
        if exp_type == "Infection":
            url = "https://raw.githubusercontent.com/Leo-Poon-Lab/GEII/main/data_gene_symbol/hGEuIInf/" + str(gene_id) + ".csv"
        else:
            url = "https://raw.githubusercontent.com/Leo-Poon-Lab/GEII/main/data_gene_symbol/hGEuISti/" + str(gene_id) + ".csv"

    try: 
        df = pd.read_csv(url, header = 0)
    except:
        df = pd.DataFrame()
    
    df = df.fillna(0)
    return df
datastats = load_data(selected_gene_type, selected_gene_id, selected_exp_type)

if(len(datastats)==0):
    st.header("No data available for this gene.")
else:
    st.sidebar.title('Filters')
    st.sidebar.markdown("[Glossary for filters](https://github.com/Leo-Poon-Lab/GEII#usage-and-glossary-information)")
    if selected_exp_type == "Infection":
        # Sidebar - H.P.I selection
        sorted_hpi = sorted(datastats['H.P.I'].unique())
        selected_hpi = st.sidebar.multiselect('H.P.I', sorted_hpi, sorted_hpi)

        # Sidebar - M.O.I selection
        sorted_moi = sorted(datastats['M.O.I'].unique())
        selected_moi = st.sidebar.multiselect('M.O.I', sorted_moi, sorted_moi)

        # Sidebar - Virus selection
        sorted_virus = sorted(datastats['virus_strain'].unique())
        selected_virus = st.sidebar.multiselect('Virus Strain', sorted_virus, sorted_virus)

        # Filtering data
        df_selected_data = datastats[(datastats['virus_strain'].isin(selected_virus)) & (datastats['H.P.I'].isin(selected_hpi)) & (datastats['M.O.I'].isin(selected_moi))]

    else:
        # Sidebar - H.P.S selection
        sorted_hps = sorted(datastats['H.P.S'].unique())
        selected_hps = st.sidebar.multiselect('H.P.S', sorted_hps, sorted_hps)

        # Sidebar - concentration selection
        sorted_concentration = sorted(datastats['concentration'].unique())
        selected_concentration = st.sidebar.multiselect('Concentration', sorted_concentration, sorted_concentration)

        # Sidebar - stimulator selection
        sorted_stimulator = sorted(datastats['stimulator'].unique())
        selected_stimulator = st.sidebar.multiselect('Stimulator', sorted_stimulator, sorted_stimulator)

        # Filtering data
        df_selected_data = datastats[(datastats['stimulator'].isin(selected_stimulator)) & (datastats['H.P.S'].isin(selected_hps)) & (datastats['concentration'].isin(selected_concentration))]

    st.subheader('Gene Expression Stats of Selected Features')
    st.write('Data Dimension: ' + str(df_selected_data.shape[0]) + ' rows and ' + str(df_selected_data.shape[1]) + ' columns.')
    st.dataframe(df_selected_data.astype(str))

st.markdown("""
---
**Made by**: *Yi Cao, [Haogao Gu](https://github.com/Koohoko), [Leo Poon](https://sph.hku.hk/en/Biography/Poon-Lit-Man-Leo)* from School of Public Health, The University of Hong Kong.

**Citation**: XXX
""")