import streamlit as st
import string
import random

st.set_page_config(page_title="🔐 Şifre Üretici", layout="centered")
st.markdown("<h1 style='text-align:center; color:#d96b00; font-size:26px;'>🔐 Şifre Üretici</h1>",unsafe_allow_html=True)
if "password" not in st.session_state:
    st.session_state.password = ""
if "strength" not in st.session_state:
    st.session_state.strength = ""

st.markdown("<h3 style='text-align:left; color:#444; font-size:16px;'>Lütfen şifre uzunluğunu ayarlayınız</h3>",unsafe_allow_html=True)
a = st.slider("", min_value=4, max_value=30, value=10)

st.markdown("<h3 style='text-align:left; color:#444; font-size:16px;'>Karakter Seçenekleri:</h3>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    use_digits = st.checkbox("Rakamlar", value=True)
with col2:
    use_letters = st.checkbox("Harfler", value=True)
with col3:
    use_symbols = st.checkbox("Semboller", value=False)
with col4:
    generate = st.button("🔄 Şifre Oluştur")

all_chars = []
if use_letters:
    all_chars.extend(list(string.ascii_letters))
if use_symbols:
    all_chars.extend(list(string.punctuation))
if use_digits:
    all_chars.extend(list("0123456789"))

if generate:
    if not all_chars:
        st.error("Lütfen en az bir karakter türü seçin!")
    else:
        st.session_state.password = ''.join(random.choice(all_chars) for _ in range(a))

        if a < 8:
            st.session_state.strength = "🔴 Şifre çok zayıf"
        elif a < 12:
            st.session_state.strength = "🟡 Şifre güvenli"
        elif a < 16:
            st.session_state.strength = "🟢 Şifre güçlü"
        else:
            st.session_state.strength = "💪 Şifre çok güçlü!"
if st.session_state.password:
    st.markdown(
        f"<h4 style='text-align:left; font-size:18px; color:#222;'>🔑 Şifreniz: "
        f"<code style='font-size:18px; color:#d96b00;'>{st.session_state.password}</code></h4>",
        unsafe_allow_html=True
    )
    st.info(st.session_state.strength)
    if st.button("📋 Şifreyi Kopyala"):
        st.markdown(
            f"""
            <script>
            navigator.clipboard.writeText("{st.session_state.password}");
            </script>
            """,
            unsafe_allow_html=True
        )
        st.success("✅ Şifre panoya kopyalandı!")
st.markdown(
    "<p style='text-align:center; color:gray; font-size:12px; margin-top:40px;'>by <b>Beyza Yıldırım</b></p>",
    unsafe_allow_html=True
)
