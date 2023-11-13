import streamlit as st
import requests

def send_text(topic):

    if topic:
        payload = {
            "topic": topic
        }
        try:
            response = requests.post("http://localhost:8000/predict/message?text", json=payload)

            status = response.status_code
            if status == 200:
                result = response.json()
                st.success(f"La predicción del texto {topic}, es {result}")
            else:
                st.error(f"Error en la solicitud con codigo, {status} intentelo nuevamente")
        except Exception as e:
            st.error(f"Ha ocurrido un error, {e}")
    else:
        st.warning("Por favor ingresa una URL de YouTube valida")