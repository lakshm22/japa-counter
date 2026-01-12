import streamlit as st

# Page setup
st.set_page_config(page_title="🕉 Japa Counter", page_icon="📿", layout="centered")

# Session state
if "count" not in st.session_state:
    st.session_state.count = 0
if "malas" not in st.session_state:
    st.session_state.malas = 0

# CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
        color: #fef3c7;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    .count {
        font-size: 72px;
        font-weight: bold;
        margin: 20px;
        color: #facc15;
        text-shadow: 2px 2px 5px #000000;
    }
    .mala {
        font-size: 24px;
        color: #a78bfa;
        margin-bottom: 30px;
    }
    .btn {
        font-size: 20px;
        padding: 15px 0;
        margin: 10px 0;
        border-radius: 15px;
        border: none;
        width: 100%;
    }
    .add { background-color: #6366f1; color: white; }
    .reset { background-color: #1e293b; color: #fef3c7; border: 1px solid #fef3c7; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown(f'<div class="count">{st.session_state.count}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="mala">Malas completed: {st.session_state.malas} 📿</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    if st.button("＋ 1 Japa", key="add", help="Tap for each mantra"):
        st.session_state.count += 1
        if st.session_state.count == 108:
            st.session_state.malas += 1
            st.session_state.count = 0
with col2:
    if st.button("Reset", key="reset", help="Reset count & malas"):
        st.session_state.count = 0
        st.session_state.malas = 0

st.markdown("<p style='text-align:center; color:#cbd5e1; font-size:16px;'>Keep your mind calm, chant with love 🌿</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
