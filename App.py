import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-image: linear-gradient(
            230deg,
            hsl(240deg 42% 11%) 0%,
            hsl(238deg 42% 13%) 11%,
            hsl(242deg 42% 15%) 22%,
            hsl(245deg 43% 18%) 33%,
            hsl(249deg 44% 20%) 44%,
            hsl(253deg 45% 22%) 56%,
            hsl(257deg 46% 24%) 67%,
            hsl(261deg 48% 26%) 78%,
            hsl(266deg 49% 27%) 89%,
            hsl(270deg 50% 29%) 100%
        );
        color: white;
    }
    p {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Hate Guard")

st.markdown(
    """
    <p style="text-align: justify;">
    Bienvenido a AntiHate, una herramienta impulsada por inteligencia artificial para detectar y combatir el discurso de odio en línea. Nuestra misión es fomentar un ambiente digital inclusivo y amigable para todos.
    </p>
    """,
    unsafe_allow_html=True,
)

st.button("¡Explora AntiHate!")
