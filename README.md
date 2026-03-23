## 🤖 CSAT Predictor – Customer Satisfaction Score Prediction from Reviews

- CSAT Predictor is an end-to-end Machine Learning system designed to predict
- Customer Satisfaction (CSAT) scores based on customer reviews and sentiment.
- The project analyzes textual feedback and sentiment signals to estimate customer satisfaction levels (1–5).
- By leveraging Natural Language Processing (NLP) and Machine Learning models, the system helps businesses
- understand customer feedback, detect dissatisfaction early, and improve service quality.

---


## 🎯 Project Goal:-

The goal of this project is to build a predictive model that can estimate CSAT scores using customer reviews.

- Predicting customer satisfaction helps businesses:
- Identify unhappy customers early- Improve service quality
- Automate feedback analysis
- Enhance customer experience

---


## 🧠 Problem Definition:-

- Type: Supervised Learning
  
- Approach: Classification (Multi-class: 1–5)

- 🔹 Input: Review (text data), Sentiment (categorical)

- 🔹 Output: CSAT Score (1–5)

👉 The problem is treated as a multi-class classification task for better performance and interpretability.

---

## 🧠 Project Highlights:-

- Text-based CSAT prediction using NLP

- TF-IDF feature engineering

- Multiple ML models (Logistic Regression, Random Forest, XGBoost)

- Hyperparameter tuning using GridSearchCV

- Model evaluation using accuracy & confusion matrix

- End-to-end pipeline from preprocessing → prediction

- Streamlit web application for real-time predictions

---

## 🛠 Tech Stack:-

- Python
- Pandas
- NumPy
- scikit-learn
- XGBoost
- NLTK
- Matplotlib
- Streamlit

---


## ⚙️ How It Works:-

## 1️⃣ Text Preprocessing:-

- Lowercasing
- Removing punctuation
- Stopword removal
- Cleaning noisy text

  
## 2️⃣ Feature Engineering:-

- Convert text → numerical features using TF-IDF
- Limit features using max_features to avoid overfitting
- Combine: Text features (TF-IDF), Sentiment feature


## 3️⃣ Model Training:-

Models used:

- Logistic Regression (Baseline)
- Random Forest (Ensemble Model)
- XGBoost (Boosting Model)


## 4️⃣ Model Evaluation:-

Models are evaluated using:

- Accuracy Score
- Confusion Matrix

Results:-

Logistic Regression → 70%
Random Forest → 76%
XGBoost → 56%

---
## 📊 Dataset Overview:-

The dataset consists of customer reviews along with sentiment and CSAT scores.

Key Columns:
- Review → Customer feedback (text)
- Sentiment → Positive / Neutral / Negative
- CSAT Score → Target variable (1–5)

---
## 🔄 Data Preprocessing:-

Steps performed:

- Handling missing values
- Text cleaning using NLP
- Stopword removal (with care for negations like "not")
- Encoding sentiment column

---
## 🤖 Machine Learning Models:-

## 1️⃣ Logistic Regression:-
- Baseline model
- Simple and interpretable
- Fast training

## 2️⃣ Random Forest:-
- Ensemble of decision trees
- Handles non-linear patterns
- Reduced overfitting

## 3️⃣ XGBoost:-
- Gradient boosting model
- High performance on structured data
- Tuned for optimal results

---

## ⚙️ Hyperparameter Tuning

Performed using:
- GridSearchCV
- RandomizedSearchCV

Improved model performance by tuning:
- Number of estimators
- Tree depth
- Learning rate
- Regularization parameters

---

## 🌐 Streamlit Application

An interactive web app built using Streamlit

Features:
- Input customer review
- Select sentiment
- Predict CSAT score instantly

Example:
- Input: "I am unhappy with the service"
- Output: Predicted CSAT: 2

---

## ▶️ How to Run:-

## 1️⃣ Install dependencies
pip install -r requirements.txt

## 2️⃣ Run the app
streamlit run app.py
---


## 📈 Business Use Cases
- 🧑‍💼 Customer Experience
- Predict dissatisfaction before surveys
- Improve service quality
---

## 📊 Feedback Analysis
- Automate review analysis
- Detect negative trends early
---

## 📌 Important Notes
Same TF-IDF vectorizer must be used during training and prediction
Input features must match training features (text + sentiment)
Large datasets are not included due to size limits
---

streamlit app link :- https://customerassistant-hsxhnvtzg4b68zjqmxddvv.streamlit.app/
---

👨‍💻 Author
Akash Jalapati
