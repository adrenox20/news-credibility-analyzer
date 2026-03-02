# train.py

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def load_dataset():
    print("Loading datasets...")

    fake = pd.read_csv("Fake.csv")
    true = pd.read_csv("True.csv")

    fake["label"] = 0
    true["label"] = 1

    data = pd.concat([fake, true], axis=0)

    data = data.sample(frac=1, random_state=42)

    print("Dataset loaded successfully")

    return data


def preprocess_and_split(data):

    X = data["text"]
    y = data["label"]

    print("Splitting dataset...")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test


def vectorize_text(X_train, X_test):

    print("Creating TF-IDF features...")

    vectorizer = TfidfVectorizer(
        max_features=5000,
        stop_words='english'
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    return vectorizer, X_train_vec, X_test_vec


def train_model(X_train_vec, y_train):

    print("Training Logistic Regression model...")

    model = LogisticRegression(
        max_iter=1000,
        n_jobs=-1
    )

    model.fit(X_train_vec, y_train)

    print("Model training completed")

    return model


def evaluate_model(model, X_test_vec, y_test):

    print("Evaluating model...")

    predictions = model.predict(X_test_vec)

    accuracy = accuracy_score(y_test, predictions)

    print("\nAccuracy:", accuracy)

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))


def save_model(model, vectorizer):

    print("Saving model and vectorizer...")

    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

    print("Saved:")
    print("model.pkl")
    print("vectorizer.pkl")


def main():

    data = load_dataset()

    X_train, X_test, y_train, y_test = preprocess_and_split(data)

    vectorizer, X_train_vec, X_test_vec = vectorize_text(X_train, X_test)

    model = train_model(X_train_vec, y_train)

    evaluate_model(model, X_test_vec, y_test)

    save_model(model, vectorizer)


if __name__ == "__main__":
    main()