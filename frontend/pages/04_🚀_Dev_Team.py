import streamlit as st
from assets.styles.css import styles
from views.messages import AUTHORS

def dev_team():
    st.set_page_config(
        page_title='Deveolpers Team',
        page_icon='🚀'
    )
    
    st.markdown(styles, unsafe_allow_html=True)
    st.title("🚀 Developers Team")
    st.markdown(AUTHORS, unsafe_allow_html=True)
    
if __name__ == "__main__":
    dev_team()