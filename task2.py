
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt_tab")

# ------------------- FAQ DATA -------------------
faq_pairs = {
    "What are your business hours?": "We’re open Mon–Fri, 9 AM to 6 PM.",
    "Where are you located?": "Our office is in Karachi, Pakistan.",
    "How do I contact support?": "Email support@apexcify.com or call +92-300-1234567.",
    "Do you give refunds?": "Yes, within 7 days as per our refund policy.",
    "What services do you provide?": "We build AI solutions, custom software and offer IT consulting."
}

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# ------------------- Text Cleaning -------------------
def clean_text(text: str) -> str:
    tokens = nltk.word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    return " ".join(tokens)

# Prepare vectors
questions = list(faq_pairs.keys())
answers = list(faq_pairs.values())
processed_qs = [clean_text(q) for q in questions]

vectorizer = TfidfVectorizer()
question_vecs = vectorizer.fit_transform(processed_qs)

# ------------------- Find Best Answer -------------------
def find_best_answer(user_text: str) -> str:
    processed_input = clean_text(user_text)
    input_vec = vectorizer.transform([processed_input])
    scores = cosine_similarity(input_vec, question_vecs)
    best_match = scores.argmax()
    return answers[best_match]

# ------------------- Console Chat -------------------
if __name__ == "__main__":
    print("💬 FAQ Chatbot (type 'quit', 'exit', or 'bye' to end)")
    while True:
        user_msg = input("You: ").strip()
        if user_msg.lower() in {"quit", "exit", "bye"}:
            print("🤖 Bot: Goodbye! 👋")
            break
        reply = find_best_answer(user_msg)
        print("🤖 Bot:", reply)
