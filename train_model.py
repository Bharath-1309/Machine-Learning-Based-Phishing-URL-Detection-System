import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

df = pd.read_csv("dataset.csv")

X = df["url"]
y = df["label"]

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

dump(model, "phishing_model.pkl")
dump(vectorizer, "vectorizer.pkl")

print("Model trained successfully!")
