import streamlit as st
import requests
from controllers import send_text
from controllers import send_mood

def send_info(topic, mood):
    try:
        send_text.send_text(topic)
        send_mood.send_mood(mood)

    except Exception as error:
        st.error(f"Ha ocurrido un error: {error}")