# import streamlit as st
# import nltk
# import string
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.download("punkt_tab")

# #  FAQ dataset
# faq_pairs = {
#     "What are your business hours?": "We’re open Mon–Fri, 9 AM to 6 PM.",
#     "Where are you located?": "Our office is in Karachi, Pakistan.",
#     "How do I contact support?": "Email support@apexcify.com or call +92-300-1234567.",
#     "Do you give refunds?": "Yes, within 7 days as per our refund policy.",
#     "What services do you provide?": "We build AI solutions, custom software and offer IT consulting."
# }

# lemmatizer = WordNetLemmatizer()
# stop_words = set(stopwords.words("english"))

# def clean_text(text):
#     tokens = nltk.word_tokenize(text.lower())
#     tokens = [t for t in tokens if t not in string.punctuation]
#     tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
#     return " ".join(tokens)

# questions = list(faq_pairs.keys())
# answers = list(faq_pairs.values())
# processed_qs = [clean_text(q) for q in questions]

# vectorizer = TfidfVectorizer()
# question_vecs = vectorizer.fit_transform(processed_qs)

# def find_best_answer(user_text):
#     processed_input = clean_text(user_text)
#     input_vec = vectorizer.transform([processed_input])
#     scores = cosine_similarity(input_vec, question_vecs)
#     best_match = scores.argmax()
#     return answers[best_match]

# #           UI 
# st.title("ApexCify Chatbot")
# st.write("Ask me a question about our services!")

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# user_msg = st.text_input("You:")

# if user_msg:
#     reply = find_best_answer(user_msg)
#     st.session_state.chat_history.append(("You", user_msg))
#     st.session_state.chat_history.append(("Bot", reply))


# for sender, msg in st.session_state.chat_history:
#     if sender == "You":
#         st.markdown(f"🧑 {msg}")
#     else:
#         st.markdown(f"🤖 {msg}")

# chat_ui.py - Streamlit Chat UI for FAQ Bot
import streamlit as st
from task2 import find_best_answer

# ------------------- Streamlit UI -------------------
st.set_page_config(page_title="FAQ Chatbot", page_icon="💬")
st.title("💬 ApexCify FAQ Chatbot")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User input box
user_input = st.text_input("Type your question:")

if user_input:
    # Exit check BEFORE generating response
    if user_input.lower().strip() in {"quit", "exit", "bye"}:
        st.write("🤖 Bot: Goodbye! 👋 Have a great day.")
        st.stop()   # Stops execution immediately

    # Otherwise, get bot reply
    bot_reply = find_best_answer(user_input)

    # Save conversation
    st.session_state["messages"].append(("You", user_input))
    st.session_state["messages"].append(("Bot", bot_reply))

# Display chat history
for sender, msg in st.session_state["messages"]:
    if sender == "You":
        st.markdown(f"🧑 **{msg}**")
    else:
        st.markdown(f"🤖 {msg}")

# Optional: Clear chat button
if st.button("Clear Chat"):
    st.session_state["messages"] = []
    st.experimental_rerun()
