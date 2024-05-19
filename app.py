import streamlit as st 
from src.chains import chain_for_eval, chain_for_qa

# Set the title of the Streamlit app with emojis
st.title("😎 Smart Q&A Evaluator 😎")

# Initialize session state for question and answer
if 'question_answer' not in st.session_state:
    st.session_state.question_answer = None

# Dropdown to select the topic with an emoji
option = st.selectbox(
    '📚 Select a topic:',
    ("🌍 Geography", "🏥 Health", "⚽ Sports"))

# Display the selected option with an emoji
st.write('📝 You selected:', option)

# If a topic is selected and it's different from the previous selection or no question is generated yet
if option and (st.session_state.question_answer is None or st.session_state.topic != option):
    st.session_state.topic = option
    st.session_state.question_answer = chain_for_qa.invoke({"topic": option.strip("🌍 🏥 ⚽")})

# Button to regenerate a question about the same topic
if st.button("🔄 Regenerate Question"):
    st.session_state.question_answer = chain_for_qa.invoke({"topic": option.strip("🌍 🏥 ⚽")})

# Display the question with an emoji
if st.session_state.question_answer:
    st.write('❓ Question:', st.session_state.question_answer["question"])

    # Input field for the user's answer with an emoji
    user_answer = st.text_input("💬 Your Answer:")

    # Button to submit the user's answer with an emoji
    if st.button("🚀 Submit Answer"):
        # Evaluate the user's answer against the actual answer
        evaluation = chain_for_eval.invoke({"qa": st.session_state.question_answer, "userAnswer": user_answer})
        
        # Display the actual answer with an emoji
        st.write("✔️ Actual Answer:", st.session_state.question_answer["answer"])
        
        # Display the evaluation result
        st.write(evaluation.content)
