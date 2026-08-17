import pandas as pd
import numpy as np
import joblib

MODEL_FILE = r"models\cyber_threat_model.pkl"
ENCODER_FILE = r"models\label_encoder.pkl"
INPUT_FILE = r"data\processed\training_data.csv"

print("=" * 60)
print("AI CYBER THREAT DETECTION")
print("PREDICTION TEST")
print("=" * 60)

print("\nLoading model...")

model = joblib.load(MODEL_FILE)
label_encoder = joblib.load(ENCODER_FILE)

print("Model loaded successfully!")
print(f"Expected features: {model.n_features_in_}")

print("\nLoading test data...")

df = pd.read_csv(INPUT_FILE, nrows=10)

X = df.drop("Label", axis=1)

# Clean data in the same way as training
X = X.replace([np.inf, -np.inf], np.nan)
X = X.apply(pd.to_numeric, errors="coerce")
X = X.fillna(0)

print(f"Input shape: {X.shape}")

print("\nMaking predictions...")

predictions = model.predict(X)

predicted_labels = label_encoder.inverse_transform(predictions)

print("\n" + "=" * 60)
print("PREDICTIONS")
print("=" * 60)

for i, prediction in enumerate(predicted_labels):
    actual = df.iloc[i]["Label"]
    print(f"{i + 1}. Actual: {actual}")
    print(f"   Predicted: {prediction}")

print("\nPrediction test completed!")