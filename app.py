import streamlit as st # importing the streamlit library to build the application
import pickle # importing the pickle library to load the saved model and vectorizer
import numpy as np # importing the numpy library to work with the numericals

# Loading the model and vectorizer
model = pickle.load(open("random_forest_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf.pkl", "rb"))

# setting the title for the application
st.title("CSAT Prediction App")

# creating the text_area where the users can type their review
review = st.text_area("Enter your review")

# Creating a dropdown box for the sentiment 
sentiment = st.selectbox("Select sentiment", ["Negative", "Neutral", "Positive"])

# Encoding the sentiment with preferred numericals by mapping the numbers with text
sentiment_map = {"Negative": 0, "Neutral": 1, "Positive": 2}
sentiment_value = sentiment_map[sentiment]

# Creating the predict button
if st.button("Predict"):
    if review: # this block executes only if the user types the review
        # Applying the vectorizer to the review and converting the result into array
        text_features = vectorizer.transform([review]).toarray()

        # Combining the text_features and sentiment_value for the input
        X = np.hstack((text_features, [[sentiment_value]]))

        # Applying the predict feature of the model to the input (X)
        prediction = model.predict(X)[0]

        # This displays the CSAT Score, if the prediction is sucess
        st.success(f"Predicted CSAT: {prediction}")
        # This else will be executed if the prediction is not sucessful
    else:
        st.warning("Please enter a review")