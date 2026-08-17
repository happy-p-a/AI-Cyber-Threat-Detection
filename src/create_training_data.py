import pandas as pd
import os

INPUT_FILE = r"data\processed\cyber_threats.csv"
OUTPUT_FILE = r"data\processed\training_data.csv"

TARGET_ROWS = 300_000
CHUNK_SIZE = 50_000

print("=" * 50)
print("AI CYBER THREAT DETECTION")
print("Creating Training Dataset")
print("=" * 50)

print("\nCounting labels...")

label_counts = {}

for chunk in pd.read_csv(INPUT_FILE, chunksize=CHUNK_SIZE):
    counts = chunk["Label"].value_counts()

    for label, count in counts.items():
        label_counts[label] = label_counts.get(label, 0) + count

print("\nOriginal label distribution:")

for label, count in sorted(label_counts.items(), key=lambda x: -x[1]):
    print(f"{label}: {count}")

total_rows = sum(label_counts.values())

targets = {}

for label, count in label_counts.items():
    targets[label] = max(
        1,
        int(TARGET_ROWS * count / total_rows)
    )

print("\nTarget samples:")

for label, count in sorted(targets.items(), key=lambda x: -x[1]):
    print(f"{label}: {count}")

print("\nCreating sample...")

samples = []
collected = {label: 0 for label in label_counts}

for chunk in pd.read_csv(INPUT_FILE, chunksize=CHUNK_SIZE):

    for label in chunk["Label"].unique():

        remaining = targets[label] - collected[label]

        if remaining <= 0:
            continue

        label_rows = chunk[chunk["Label"] == label]

        take = min(len(label_rows), remaining)

        if take > 0:
            selected = label_rows.sample(
                n=take,
                random_state=42
            )

            samples.append(selected)
            collected[label] += take

    print(
        f"Processed chunk | "
        f"Collected: {sum(collected.values())}/{sum(targets.values())}"
    )

training_data = pd.concat(
    samples,
    ignore_index=True
)

training_data = training_data.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

os.makedirs(
    os.path.dirname(OUTPUT_FILE),
    exist_ok=True
)

training_data.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n" + "=" * 50)
print("DONE")
print("=" * 50)

print(f"\nTraining rows: {len(training_data)}")
print(f"Features: {len(training_data.columns) - 1}")

print("\nFinal label distribution:")
print(training_data["Label"].value_counts())

print("\nSaved to:")
print(OUTPUT_FILE)
