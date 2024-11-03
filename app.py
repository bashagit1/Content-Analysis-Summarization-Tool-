import streamlit as st
import openai
import os
from SimplerLLM.language.llm import LLM, LLMProvider

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM instance
llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-3.5-turbo")

# Define function to summarize content
def summarize_content(content):
    """Generates a concise summary for the provided content."""
    return llm_instance.generate_response(messages=[{"role": "user", "content": f"Summarize the following content concisely: {content}"}])

# Define function to analyze content tone
def analyze_tone(content):
    """Analyzes the tone of the content."""
    return llm_instance.generate_response(messages=[{"role": "user", "content": f"Analyze the tone of this content: {content}"}])

# Define function to analyze content sentiment
def analyze_sentiment(content):
    """Performs sentiment analysis on the provided content."""
    return llm_instance.generate_response(messages=[{"role": "user", "content": f"Analyze the sentiment of this content: {content}"}])

# Define function to analyze content structure
def analyze_structure(content):
    """Analyzes the structure of the content (e.g., logical flow, clarity, etc.)."""
    return llm_instance.generate_response(messages=[{"role": "user", "content": f"Analyze the structure and clarity of this content: {content}"}])

# Streamlit UI with enhanced styling and characters
st.markdown("<h1 style='text-align: center; color: #4169E1;'>📊 Content Analysis & Summarization Tool 📝</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #696969;'>Analyze and summarize any content for quick insights.</p>", unsafe_allow_html=True)

# Sidebar for Analysis Options
with st.sidebar:
    st.markdown("<h2 style='color: #FF6347;'>🔍 Analysis Options</h2>", unsafe_allow_html=True)
    analysis_type = st.selectbox("Choose Analysis Type", ["Summarize", "Tone Analysis", "Sentiment Analysis", "Structure Analysis"])
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("👈 Select the type of analysis here!")

# Input for user content
user_content = st.text_area("Enter the content you want to analyze or summarize:", placeholder="Paste your text here...")

# Generate and display results based on user selection
if st.button("Run Analysis"):
    if user_content:
        # Choose function based on analysis type
        if analysis_type == "Summarize":
            result = summarize_content(user_content)
            st.markdown("<h3 style='color: #4B0082;'>📝 Summary:</h3>", unsafe_allow_html=True)
        elif analysis_type == "Tone Analysis":
            result = analyze_tone(user_content)
            st.markdown("<h3 style='color: #4B0082;'>🔍 Tone Analysis:</h3>", unsafe_allow_html=True)
        elif analysis_type == "Sentiment Analysis":
            result = analyze_sentiment(user_content)
            st.markdown("<h3 style='color: #4B0082;'>📈 Sentiment Analysis:</h3>", unsafe_allow_html=True)
        elif analysis_type == "Structure Analysis":
            result = analyze_structure(user_content)
            st.markdown("<h3 style='color: #4B0082;'>🔎 Structure Analysis:</h3>", unsafe_allow_html=True)
        
        # Display result
        st.write(result)
        
        # Option to download the result
        st.download_button(label="💾 Download Result", data=result, file_name="analysis_result.txt")
    else:
        st.warning("Please enter content to analyze or summarize!")
