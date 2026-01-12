import streamlit as st

# Page setup
st.set_page_config(page_title="Japa Counter", layout="centered")

# Initialize session state
if "count" not in st.session_state:
    st.session_state.count = 0

if "malas" not in st.session_state:
    st.session_state.malas = 0

# Title
st.markdown("## 🕉 Japa Counter")
st.markdown("📿 A simple digital mala (108 japa = 1 mala)")
st.markdown("hare krishna hare krishna krishna krishna hare hare hare rama hare rama rama rama hare hare")

st.divider()

# Display counts
st.markdown(
    f"<h1 style='text-align:center'>{st.session_state.count}</h1>",
    unsafe_allow_html=True
)
st.markdown(
    f"<p style='text-align:center; font-size:20px;'>Malas: {st.session_state.malas}</p>",
    unsafe_allow_html=True
)

st.divider()

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("＋ 1 Japa", use_container_width=True):
        st.session_state.count += 1
        if st.session_state.count == 108:
            st.session_state.malas += 1
            st.session_state.count = 0

with col2:
    if st.button("Reset", use_container_width=True):
        st.session_state.count = 0
        st.session_state.malas = 0

# Footer note
st.markdown(
    "<p style='text-align:center; color:gray; font-size:14px;'>"
    "Use with breath, mantra, or silence 🌿"
    "</p>",
    unsafe_allow_html=True
)
