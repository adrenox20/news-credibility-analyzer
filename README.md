📰 Intelligent News Credibility Analyzer

A Machine Learning and Natural Language Processing (NLP) system that automatically analyzes news article text and predicts whether it is Credible (Real) or Fake.

This project demonstrates a complete end-to-end ML pipeline including data preprocessing, feature engineering, model training, evaluation, and deployment as an interactive web application.

🚀 Live Demo

Streamlit App:
https://adrenox20-news-credibility-analyzer.streamlit.app

GitHub Repository:
https://github.com/adrenox20/news-credibility-analyzer

📌 Project Overview

The rapid spread of misinformation across digital platforms has created a need for automated credibility verification systems. This project uses classical NLP and Machine Learning techniques to classify news articles based on textual patterns.

The system:

Accepts news article text input

Preprocesses and vectorizes the text using TF-IDF

Uses a trained Logistic Regression model for classification

Displays prediction results with confidence score

Provides feature importance and probability visualization

Runs as a deployed web application using Streamlit

🧠 System Architecture

User Input → Streamlit Interface → Text Preprocessing → TF-IDF Vectorization → Logistic Regression Model → Prediction → Result Display

🧾 Dataset

Dataset used: Fake and Real News Dataset (Kaggle)

Dataset contains:

~44,000 news articles

Fake news: ~23,000

Real news: ~21,000

Features:

Article title

Article text

Subject category

Publication date

Target:

0 = Fake News

1 = Real News

⚙️ Technology Stack

Programming Language:
Python

Machine Learning:
Scikit-learn
Logistic Regression

Natural Language Processing:
TF-IDF Vectorization

Data Processing:
Pandas
NumPy

Visualization:
Matplotlib

Deployment:
Streamlit
Streamlit Community Cloud

Version Control:
Git
GitHub

📊 Model Details

Feature Extraction:
TF-IDF Vectorizer
Max Features: 5000
Stopword removal enabled

Classifier:
Logistic Regression
max_iter = 1000

Train-Test Split:
80% Training
20% Testing

Performance:

Accuracy: 96–98%

Precision: ~0.97

Recall: ~0.97

F1 Score: ~0.97

🖥️ Application Features

Real-time news credibility prediction

Confidence score display

Feature importance visualization

Prediction probability chart

Professional interactive dashboard

Deployed and publicly accessible

📁 Project Structure
news-credibility-analyzer/
│
├── app.py
├── train.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
▶️ How to Run Locally
Step 1: Clone repository
git clone https://github.com/adrenox20/news-credibility-analyzer.git
cd news-credibility-analyzer
Step 2: Create virtual environment
python3 -m venv venv
source venv/bin/activate
Step 3: Install dependencies
pip install -r requirements.txt
Step 4: Run application
streamlit run app.py
🌐 Deployment

The application is deployed using Streamlit Community Cloud.

Deployment ensures:

Public accessibility

Real-time inference

No local setup required

📈 Future Improvements

Transformer models (BERT, RoBERTa)

Explainable AI (SHAP, LIME)

Multi-language support

Integration with live news APIs

Improved contextual understanding

👥 Team Members

Ram Bhardwaj
Mukund Mangla
Prajjwal Tripathi

B.Tech Artificial Intelligence & Machine Learning

📜 License

This project is developed for academic and educational purposes.

✅ Conclusion

This project demonstrates how classical NLP and Machine Learning techniques can effectively detect misinformation and provide scalable, deployable credibility analysis systems.