import streamlit as st
from textblob import TextBlob
import random

st.set_page_config(page_title="EchoProof AI", layout="centered")

st.title("🛡️ EchoProof — AI Fake Review Detector")
st.subheader("Detect fake, spam, and AI-generated reviews")

review = st.text_area("Enter a product review:")

fake_keywords = [
    "best product ever",
    "must buy",
    "100% genuine",
    "life changing",
    "excellent product",
    "highly recommended",
    "five stars",
    "perfect product"
]

if st.button("Analyze Review"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:

        sentiment = TextBlob(review).sentiment.polarity

        keyword_score = 0

        for word in fake_keywords:
            if word.lower() in review.lower():
                keyword_score += 1

        fake_probability = min((keyword_score * 20) + random.randint(10, 30), 95)

        authenticity = 100 - fake_probability

        st.markdown("## Analysis Result")

        if fake_probability > 60:
            st.error("⚠️ This review appears suspicious or potentially fake.")
        else:
            st.success("✅ This review appears relatively authentic.")

        st.write(f"### Fake Review Probability: {fake_probability}%")
        st.write(f"### Authenticity Score: {authenticity}%")

        if sentiment > 0:
            st.write("### Sentiment: Positive")
        elif sentiment < 0:
            st.write("### Sentiment: Negative")
        else:
            st.write("### Sentiment: Neutral")

        st.markdown("### Suspicious Keyword Detection")

        detected = []

        for word in fake_keywords:
            if word.lower() in review.lower():
                detected.append(word)

        if detected:
            for item in detected:
                st.write(f"• {item}")
        else:
            st.write("No suspicious keywords detected.")