import streamlit as st
from transformers import pipeline

# Set up the page
st.set_page_config(
  page_title="AI Text Generator",
  page_icon="🤖",
  layout="centered"
)

# Main App Header
st.markdown("<h1 style='text-align: center;'>🤖 AI Text <span style='color: #1F77B4;'>Generator</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: gray;'>✨ Enter a starting sentence, and let the AI complete it for you!</p>", unsafe_allow_html=True)
st.divider()

# Load Model
@st.cache_resource
def load_model():
    # Changed to a genuinely small, fast, and accurate model (1.5B parameters)
    return pipeline("text-generation", model="distilgpt2")

generator = load_model()

st.markdown("### ✍️ Enter your text below:")
prompt = st.text_area(
  "hidden_label", 
  label_visibility="collapsed",
  placeholder="Artificial Intelligence is transforming the way we...",
  height=150
)

generate_btn = st.button("✨ Generate Text")

if generate_btn:
    if prompt:
        with st.spinner("🤖 Generating your text..."):
            result = generator(
                prompt,
                max_new_tokens=50,
                num_return_sequences=1
            )
        generated_text = result[0]["generated_text"]
        st.success("✅ Generation Complete!")
        st.markdown("### 📝 Generated Result")
        st.info(generated_text)
    else:
        st.warning("⚠️ Please enter some text first!")