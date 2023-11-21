import streamlit as st
from assets.styles.css import styles
from views.messages import AUTHORS

#def analisis():
st.set_page_config(
    page_title='Analisis',
    page_icon='📈'
    )
    
st.markdown(styles, unsafe_allow_html=True)
st.title("📈 Analisis")
st.markdown(AUTHORS, unsafe_allow_html=True)
    
codigo_insercion_powerbi ="""
    <iframe title="analisis_nlp1" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=3fe38db6-3acd-4192-a441-c3e504a40376&ctid=7d979bda-6909-4e84-9f48-1674dc104477" frameborder="0" allowFullScreen="true"></iframe>
"""
st.markdown(codigo_insercion_powerbi, unsafe_allow_html=True)

__name__ == "__main__"
    #analisis()