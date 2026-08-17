import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score


INPUT_FILE = r"data\processed\training_data.csv"
MODEL_DIR = r"models"

print("=" * 60)
print("AI CYBER THREAT DETECTION")
print("MODEL TRAINING")
print("=" * 60)

print("\nLoading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# --------------------------------------------------
# Remove classes with fewer than 2 samples
# --------------------------------------------------

print("\nOriginal label distribution:")
print(df["Label"].value_counts())

label_counts = df["Label"].value_counts()

valid_labels = label_counts[label_counts >= 2].index

removed_labels = label_counts[label_counts < 2].index

if len(removed_labels) > 0:
    print("\nRemoving classes with fewer than 2 samples:")

    for label in removed_labels:
        print(f"  {label}: {label_counts[label]} sample")

df = df[df["Label"].isin(valid_labels)].copy()

print(f"\nRows after removing extremely rare classes: {len(df)}")
print(f"Classes remaining: {df['Label'].nunique()}")

# --------------------------------------------------
# Separate features and labels
# --------------------------------------------------

X = df.drop("Label", axis=1)
y = df["Label"]

# Replace infinite values
X = X.replace([np.inf, -np.inf], np.nan)

# Convert features to numeric
X = X.apply(pd.to_numeric, errors="coerce")

# Fill missing values
X = X.fillna(X.median(numeric_only=True))
X = X.fillna(0)

# --------------------------------------------------
# Encode labels
# --------------------------------------------------

print("\nEncoding labels...")

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

print("Classes:")

for i, label in enumerate(label_encoder.classes_):
    print(f"{i}: {label}")

# --------------------------------------------------
# Train/test split
# --------------------------------------------------

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# --------------------------------------------------
# Train model
# --------------------------------------------------

print("\nTraining Random Forest model...")
print("Please wait...")

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    min_samples_leaf=2,
    class_weight="balanced",
    random_state=42,
    n_jobs=2
)

model.fit(X_train, y_train)

print("\nModel training completed!")


# --------------------------------------------------
# Predictions
# --------------------------------------------------

print("\nMaking predictions...")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL RESULTS")
print("=" * 60)

print(f"\nAccuracy: {accuracy:.4f}")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")

# Get only the classes actually present in the test set/predictions
report_labels = sorted(set(y_test) | set(y_pred))
report_names = label_encoder.inverse_transform(report_labels)

print(
    classification_report(
        y_test,
        y_pred,
        labels=report_labels,
        target_names=report_names,
        zero_division=0
    )
)

# --------------------------------------------------
# Save model
# --------------------------------------------------

os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(
    model,
    r"models\cyber_threat_model.pkl"
)

joblib.dump(
    label_encoder,
    r"models\label_encoder.pkl"
)

print("\nModels saved:")
print(r"models\cyber_threat_model.pkl")
print(r"models\label_encoder.pkl")

print("\n" + "=" * 60)
print("DONE!")
print("=" * 60)