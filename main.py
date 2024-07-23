import streamlit as st
import paginas.crea as crea
import paginas.confea as confea

st.sidebar.title("Sistema Nacional de Unificação dos CREAs")
selection1 = st.sidebar.selectbox('Menu',['Usuário CREA','Usuário CONFEA'])
if selection1 == 'Usuário CREA':
    crea.inicio()
if selection1 == 'Usuário CONFEA':
    confea.inicio()      

