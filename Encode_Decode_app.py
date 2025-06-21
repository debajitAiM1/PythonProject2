import streamlit as st
import base64
import zlib
import streamlit.components.v1 as components

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
            st.success("✅ Message Encoded")
            st.text_area("Encoded Key:", secret, height=150, key="decoded_text")
            components.html(f"""
            <div class="button-wrapper">
              <textarea id="toCopy" style="position: absolute; left: -9999px;">{secret}</textarea>
              <button class="normal-button" onclick="copyText()">📋 Copy</button>
            </div>

            <style>
              .button-wrapper {{
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 30px;
              }}

              .normal-button {{
                padding: 12px 30px;
                font-size: 16px;
                font-weight: 600;
                color: white;
                background-color: #6f42c1;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                transition: transform 0.2s ease-in-out;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
              }}

              .normal-button:hover {{
                transform: translateY(-6px) scale(1.05);
              }}
            </style>

            <script>
              function copyText() {{
                var textArea = document.getElementById("toCopy");
                textArea.select();
                document.execCommand("copy");
                alert("✅ Copied to clipboard!");
              }}
            </script>
            """, height=180)
        else:
            st.warning("Please enter a message to encode.")

elif mode == "🔓 Decode":
    code_input = st.text_area("Paste your secret code here:", height=150)
    if st.button("Decode"):
        if code_input.strip():
            original = decode_message(code_input.strip())
            st.success("✅ Message Decoded")
            st.text_area("Decoded Text:", original, height=150, key="decoded_text")
            components.html(f"""
            <div class="button-wrapper">
              <textarea id="toCopy" style="position: absolute; left: -9999px;">{original}</textarea>
              <button class="normal-button" onclick="copyText()">📋 Copy</button>
            </div>

            <style>
              .button-wrapper {{
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 30px;
              }}

              .normal-button {{
                padding: 12px 30px;
                font-size: 16px;
                font-weight: 600;
                color: white;
                background-color: #6f42c1;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                transition: transform 0.2s ease-in-out;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
              }}

              .normal-button:hover {{
                transform: translateY(-6px) scale(1.05);
              }}
            </style>

            <script>
              function copyText() {{
                var textArea = document.getElementById("toCopy");
                textArea.select();
                document.execCommand("copy");
                alert("✅ Copied to clipboard!");
              }}
            </script>
            """, height=180)
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