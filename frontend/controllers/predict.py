import streamlit as st
from assets.styles.css import styles
from views.messages import AUTHORS, BAR, CYBORG, INTRO, PREDICT, SIDE_INFO, TITLE


def app():
    st.set_page_config(
        page_title="Hate Guardian - Advanced AI anti-hate",
        page_icon="🛡️",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.markdown(styles, unsafe_allow_html=True)

    st.image(CYBORG)

    st.title(TITLE)
    st.markdown(INTRO)
    st.sidebar.subheader(BAR)
    st.sidebar.info(SIDE_INFO)
    st.sidebar.markdown(PREDICT)

    st.header("Installation")
    # st.code("pip install streamlit-toggle", language="bash")
    # st.header("Quickstart")
    # st.code(QUICKSTART, language="python")
    st.markdown(AUTHORS, unsafe_allow_html=True)


if __name__ == "__main__":
    app()
