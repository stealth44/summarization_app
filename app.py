import streamlit as st
import requests

# Must be the very first Streamlit command
st.set_page_config(page_title="AI Summarizer", page_icon="📝")

# Hugging Face API setup
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

def summarize_via_api(text, hf_token):
    headers = {"Authorization": f"Bearer {hf_token}"}
    payload = {
        "inputs": text[:3000],
        "parameters": {
            "max_length": 130,
            "min_length": 30,
            "do_sample": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['summary_text']
    elif response.status_code == 503:
        return "⚠️ Model is loading on Hugging Face servers, please wait 20 seconds and try again."
    elif response.status_code == 401:
        return "❌ Invalid API token. Please check your Hugging Face token."
    else:
        return f"❌ Error {response.status_code}: {response.text}"

#  UI
st.title("My Text Summarizer App")
st.markdown("Enter long text below to get a structured summary.")

# Sidebar for API token input
with st.sidebar:
    st.header("⚙️ Settings")
    hf_token = st.text_input(
        "Hugging Face API Token",
        type="password",
        placeholder="hf_xxxxxxxxxxxxxxxx",
        help="Enter your Hugging Face token from huggingface.co/settings/tokens"
    )

text_input = st.text_area("Input Text", placeholder="Paste your article here...", height=250)

if st.button("Generate Summary"):
    if not hf_token:
        st.error("Please enter your Hugging Face API token in the sidebar.")
    elif not text_input:
        st.error("Please enter some text first.")
    elif len(text_input.split()) < 30:
        st.error("Text is too short. Please enter at least 30 words.")
    else:
        with st.spinner("Summarizing text...."):
            result = summarize_via_api(text_input, hf_token)
            if result.startswith("❌") or result.startswith("⚠️"):
                st.warning(result)
            else:
                st.subheader("Summary Result:")
                st.success(result)