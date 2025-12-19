import streamlit as st
from stt.whisper_stt import transcribe
from utils.mic_recorder import mic_recorder
from utils.audio_utils import save_uploaded_audio
from nlp.ollama_sales_engine import analyze_customer

st.set_page_config("AI Sales Assistant", layout="wide")

st.markdown("""
<style>
.card{background:#161b22;padding:15px;border-radius:12px;margin:10px 0}
.customer{background:#1f2937;padding:12px;border-radius:10px}
.ai{background:#052e2b;padding:12px;border-radius:10px}
.badge{background:#2563eb;color:white;padding:4px 10px;border-radius:20px}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Sales Assistant")
st.caption("Customer Voice → AI Sales Intelligence")

if "chat" not in st.session_state:
    st.session_state.chat = []

audio_path = None

col1, col2 = st.columns(2)
with col1:
    uploaded = st.file_uploader("Upload customer audio", type=["wav", "mp3"])
    if uploaded:
        audio_path = save_uploaded_audio(uploaded)
        st.audio(audio_path)

with col2:
    if st.button("🎙️ Record Customer (5 sec)"):
        audio_path = mic_recorder()
        st.audio(audio_path)

if audio_path:
    transcript = transcribe(audio_path)

    st.session_state.chat.append({"speaker": "customer", "text": transcript})
    analysis = analyze_customer(transcript)
    st.session_state.chat.append({"speaker": "ai", "text": analysis["ai_reply"]})

    st.subheader("📝 Transcript & NLP")
    st.markdown(f"<div class='card'>{transcript}</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card'>
    <span class='badge'>Sentiment</span> {analysis['sentiment']['label']}  
    <br><span class='badge'>Intent</span> {analysis['intent']}  
    <br><span class='badge'>Entities</span> {analysis['entities']}
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧠 AI Sales Suggestions")
    st.markdown(f"<div class='ai'><b>Auto Reply:</b><br>{analysis['ai_reply']}</div>", unsafe_allow_html=True)

    st.markdown("**Next Questions to Ask:**")
    for q in analysis["next_questions"]:
        st.write("•", q)

    st.markdown(f"<div class='card'><b>Objection Handling:</b><br>{analysis['objection_handling']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'><b>Product Recommendation:</b><br>{analysis['product_recommendation']}</div>", unsafe_allow_html=True)

st.subheader("💬 Conversation")
for msg in st.session_state.chat:
    if msg["speaker"] == "customer":
        st.markdown(f"<div class='customer'>🧑 {msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai'>🤖 {msg['text']}</div>", unsafe_allow_html=True)
