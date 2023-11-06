import streamlit as st
from assets.styles.css import styles
from views.messages import AUTHORS

def analisis():
    st.set_page_config(
        page_title='Analisis',
        page_icon='📈'
    )
    
    st.markdown(styles, unsafe_allow_html=True)
    st.title("📈 Analisis")
    st.markdown(AUTHORS, unsafe_allow_html=True)
    
if __name__ == "__main__":
    analisis()