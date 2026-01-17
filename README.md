# Multi-Prompt Reasoning System (Free API Version)

This version uses Hugging Face Inference API instead of OpenAI.

## Steps to Run

1. Create Hugging Face account: https://huggingface.co
2. Get free token: https://huggingface.co/settings/tokens
3. Rename `.env.example` to `.env` and add token

HF_API_TOKEN=hf_xxxxxxxxx

4. Install dependencies:
pip install -r requirements.txt

5. Run app:
streamlit run app.py
