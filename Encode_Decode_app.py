import streamlit as st
import base64
import zlib

st.set_page_config(page_title="Secret Message Encoder/Decoder", layout="centered")

st.title("🔐 Secret Message Encoder & Decoder")
st.markdown("**Use this tool to encode/decode secret messages (text or emojis).**")

mode = st.radio("Select Mode:", ["🔏 Encode", "🔓 Decode"], horizontal=True)

def encode_message(message: str) -> str:
    compressed = zlib.compress(message.encode('utf-8'))
    encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')
    return encoded

def decode_message(secret_code: str) -> str:
    try:
        decoded_bytes = base64.urlsafe_b64decode(secret_code.encode('utf-8'))
        original = zlib.decompress(decoded_bytes).decode('utf-8')
        return original
    except Exception:
        return "❌ Invalid secret code! Please check your input."

if mode == "🔏 Encode":
    text_input = st.text_area("Enter your message (text, emoji, anything):", height=150)
    if st.button("Encode"):
        if text_input.strip():
            secret = encode_message(text_input.strip())
            st.success("✅ Here is your secret code:")
            st.code(secret, language='text')
        else:
            st.warning("Please enter a message to encode.")

elif mode == "🔓 Decode":
    code_input = st.text_area("Paste your secret code here:", height=150)
    if st.button("Decode"):
        if code_input.strip():
            original = decode_message(code_input.strip())
            st.success("✅ Decoded Message:")
            st.code(original, language='text')
        else:
            st.warning("Please enter a secret code to decode.")

st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        left: 10px;  /* Changed from right to left */
        color: #888888;
        font-size: 14px;
        text-align: left;
        opacity: 0.8;
        z-index: 100;
    }
    @media (max-width: 600px) {
        .footer {
            font-size: 12px;
        }
    }
    </style>
    <div class="footer">
        Created by <b>Debajit</b>
    </div>
""", unsafe_allow_html=True)