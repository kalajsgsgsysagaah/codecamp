import pandas as pd
import re
import string
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset (replace with your actual dataset)
data = {
    "email": [
        "Congratulations! You've won a free lottery. Claim now.",
        "Hey, are we still on for the meeting tomorrow?",
        "Win a brand new car for free! Click the link below.",
        "Reminder: Your invoice for last month's subscription is due.",
        "You have been selected for a special discount, click here!"
    ],
    "label": [1, 0, 1, 0, 1]  # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

# Text preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(f"[{string.punctuation}]", "", text)  # Remove punctuation
    text = re.sub(r"\d+", "", text)  # Remove numbers
    return text

df["cleaned_email"] = df["email"].apply(preprocess_text)

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned_email"])
y = df["label"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Naïve Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save the trained model and vectorizer
joblib.dump(model, "spam_classifier.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

# Load the saved model and vectorizer
loaded_model = joblib.load("spam_classifier.pkl")
loaded_vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Test a new email
new_email = ["You have won a cash prize! Click here to claim."]
new_email_cleaned = [preprocess_text(email) for email in new_email]
new_email_vectorized = loaded_vectorizer.transform(new_email_cleaned)

# Predict whether the new email is spam or not
prediction = loaded_model.predict(new_email_vectorized)
print("Prediction (1 = Spam, 0 = Not Spam):", prediction[0])

# Evaluate model performance
y_pred = loaded_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
