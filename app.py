import streamlit as st
from agent import run_agent_workflow

# 1. Page Configuration
st.set_page_config(
    page_title="MemeCircuit | AI Meme Agent",
    page_icon="⚡",
    layout="wide",
)

# 2. CSS for Black Typing Text
st.markdown(
    """
    <style>
    input[type="text"], textarea, div[data-baseweb="input"] input, div[data-baseweb="base-input"] input {
        color: #000000 !important;
    }
    ::placeholder {
        color: #6b7280 !important;
        opacity: 1 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. App Header
st.title("⚡ MemeCircuit - Autonomous Meme Agent")
st.caption("Spot trends, trigger LangGraph reasoning, generate visual memes with Pillow, and publish live.")

st.markdown("---")

# 4. Split Layout Dashboard
col_left, col_right = st.columns([1, 1.5], gap="large")

with col_left:
    st.subheader("🔥 Trending Right Now")
    st.metric(label="Work Culture", value="The Spreadsheet Apocalypse", delta="Score: 96")
    st.metric(label="Social Mood", value="NPC Energy", delta="Score: 89")
    st.metric(label="Daily Life", value="Side Quest Mode", delta="Score: 84")
    st.metric(label="Online Humor", value="Main Character Buffering", delta="Score: 78")

with col_right:
    st.subheader("🤖 Culture Co-Pilot Console")
    
    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Quick action buttons
    st.write("**Quick Prompts:**")
    btn_col1, btn_col2 = st.columns(2)
    
    triggered_prompt = None
    with btn_col1:
        if st.button("Explain NPC Energy", use_container_width=True):
            triggered_prompt = "Explain NPC Energy"
    with btn_col2:
        if st.button("Why is Side Quest trending?", use_container_width=True):
            triggered_prompt = "Why is Side Quest trending?"

    # Chat Input
    user_input = st.chat_input("Ask about a trend or generate a meme...")
    if user_input:
        triggered_prompt = user_input

    # Execute workflow if any prompt was triggered via button or chat input
    if triggered_prompt:
        # 1. Append user prompt to history
        st.session_state.messages.append({"role": "user", "content": triggered_prompt})
        
        # 2. Run LangGraph Workflow
        with st.spinner("🤖 LangGraph agent running workflow..."):
            agent_output = run_agent_workflow(triggered_prompt)
            
        # 3. Append assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": agent_output})
        
        # 4. Rerun to instantly render the response
        st.rerun()