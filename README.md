# Email Spam Classifier

This is an Email Spam Classifier web application that utilizes multiple machine learning models for classifying emails as either spam or not spam (ham). The project is built using Streamlit, a Python library for creating interactive web applications, and it is hosted at

## Website link https://email-spam-classifier-ua8t.onrender.com

## Overview

The goal of this project is to create a robust email spam classifier capable of accurately distinguishing between spam and legitimate (ham) emails. To achieve this, the following steps were taken:

1. **Data Preprocessing and Cleaning:** The email text data was subjected to extensive preprocessing and cleaning. This involved converting the text to lowercase, tokenization, removal of punctuation, and eliminating common stopwords. Additionally, the Porter Stemmer algorithm was used to reduce words to their base form, which helps in feature extraction.

2. **Model Selection:** Multiple machine learning models were considered for the task, including Multinomial Naive Bayes, Bernoulli Naive Bayes, and Random Forest. Each model was trained and evaluated using appropriate metrics.

3. **Performance Evaluation:** The performance of each model was assessed using metrics such as accuracy, precision, recall, and F1-score. The goal was to select a model that demonstrated the best overall performance on the test dataset.

4. **Random Forest Model:** After experimenting with different models, the Random Forest algorithm exhibited the highest accuracy and performed well on various evaluation metrics. Therefore, it was chosen as the final model for the email spam classifier.

## Getting Started

To try the Email Spam Classifier web application locally:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit app by executing the following command:

```bash
streamlit run app.py
```

4. Access the web application in your web browser by visiting [http://localhost:8501](http://localhost:8501).

## How to Use

1. Enter the email text you wish to classify in the provided text area.
2. Click on the "Predict" button.
3. The classifier will determine whether the email is "Spam" or "Not Spam" (ham) and display the result.

## Dataset

The dataset used for training and evaluating the models contains labeled examples of spam and ham emails. It was thoroughly preprocessed and cleaned to ensure high-quality training data.

## Note

1. The Random Forest model selected for the Email Spam Classifier has been chosen based on the specific dataset used and the performance metrics observed during evaluation. For different datasets, other models might perform better.
2. The accuracy and effectiveness of the classifier depend heavily on the quality and size of the training dataset. To achieve even better results, a larger and more diverse dataset may be used for training.
3. This project serves as an educational example of building an email spam classifier and demonstrating the effectiveness of different machine learning models.

## Acknowledgments

- Special thanks to the authors of the machine learning libraries and tools, including NLTK, Scikit-learn, and Streamlit, for enabling the development of this project.
- The email spam classification model and dataset used in this project are for demonstration purposes only.
