import streamlit as st
from assets.styles.css import styles
from views.messages import AUTHORS
from controllers.send_info import send_info

def prediction():
    st.set_page_config(
        page_title='Predicción Hate',
        page_icon='🤖'
    )

    st.markdown(styles, unsafe_allow_html=True)
    st.title("🤖 Predicción Hate")
    
    st.markdown(
    "Escribe a continuación el ID del comentario que deseas predecir"
)

    topic = st.text_input(label="Comentario de YouTube", placeholder="ID")
    mood = st.text_area(
        label="Comentario de texto",
        placeholder="Escribe aquí",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.feeling_lucky = not st.button(
            label="Predecir",
            type="primary",
            on_click=send_info,
            args=(topic, mood),
        )
    
    st.markdown(AUTHORS, unsafe_allow_html=True)
    
if __name__ == "__main__":
    prediction()