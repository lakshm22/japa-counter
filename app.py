import streamlit as st
import json
import os

st.set_page_config(page_title="Japa Counter", layout="centered")

MALA_SIZE = 108
DATA_FILE = "japa_data.json"

# Load saved data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {"count": 0, "goal": 5, "dark": False}

if "count" not in st.session_state:
    st.session_state.count = data["count"]
if "goal" not in st.session_state:
    st.session_state.goal = data["goal"]
if "dark" not in st.session_state:
    st.session_state.dark = data["dark"]

malas = st.session_state.count // MALA_SIZE
current = st.session_state.count % MALA_SIZE

# Save function
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump({
            "count": st.session_state.count,
            "goal": st.session_state.goal,
            "dark": st.session_state.dark
        }, f)

bg = "#1e1e1e" if st.session_state.dark else "#f8f5f2"
fg = "#ffffff" if st.session_state.dark else "#000000"

st.markdown(f"""
<style>
body {{ background-color: {bg}; color: {fg}; }}
.card {{ background: {'#2b2b2b' if st.session_state.dark else 'white'}; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🕉️ Japa Counter</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div style='text-align:center; font-size:20px;'>
<b>Total Count:</b> {st.session_state.count}<br>
<b>Malas Completed:</b> {malas}<br>
<b>Current Mala:</b> {current}/108<br>
<b>Daily Goal:</b> {st.session_state.goal} malas
</div>
""", unsafe_allow_html=True)

progress = min(malas / st.session_state.goal, 1.0)
st.progress(progress)

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Count", use_container_width=True):
        st.session_state.count += 1
        if st.session_state.count % MALA_SIZE == 0:
            st.balloons()
        save_data()

with col2:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.count = 0
        save_data()

st.markdown("---")

st.session_state.goal = st.number_input("🎯 Set Daily Mala Goal", min_value=1, value=st.session_state.goal)
st.session_state.dark = st.checkbox("🌙 Dark Mode", value=st.session_state.dark)

save_data()

st.markdown("</div>", unsafe_allow_html=True)