import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the dataset
df = pd.read_csv('mail_data.csv')

# 2. Preprocess the Data
# Handle any missing values by replacing them with empty strings
df = df.where((pd.notnull(df)), '')

# Map the categories to numerical values (spam = 1, ham = 0)
df['Category'] = df['Category'].map({'spam': 1, 'ham': 0})

# Separate features (X) and target labels (y)
X = df['Message']
y = df['Category']

# 3. Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Feature Extraction
# Convert text data to TF-IDF feature vectors
vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# 5. Model Training
# Initialize and train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_features, y_train)

# 6. Evaluation
# Predict on the test data
predictions = model.predict(X_test_features)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Test Accuracy: {accuracy:.4f}\n")
print("Classification Report:")
print(classification_report(y_test, predictions, target_names=['Ham (0)', 'Spam (1)']))