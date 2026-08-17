import pandas as pd
import glob
import os

RAW_DIR = r"data\raw\MachineLearningCVE"
OUTPUT_FILE = r"data\processed\cyber_threats.csv"


def load_dataset():
    files = glob.glob(os.path.join(RAW_DIR, "*.csv"))

    print(f"Found {len(files)} CSV files.")

    dataframes = []

    for file in files:
        print(f"Reading: {os.path.basename(file)}")

        df = pd.read_csv(file)

        df.columns = df.columns.str.strip()

        dataframes.append(df)

    combined = pd.concat(dataframes, ignore_index=True)

    return combined


def clean_dataset(df):
    df = df.dropna(how="all")

    df.columns = df.columns.str.strip()

    df["Label"] = (
        df["Label"]
        .astype(str)
        .str.strip()
        .str.replace("�", "-", regex=False)
    )

    df = df.replace([float("inf"), float("-inf")], pd.NA)

    df = df.dropna()

    return df


def main():
    print("=" * 50)
    print("AI CYBER THREAT DETECTION")
    print("Dataset Preprocessing")
    print("=" * 50)

    df = load_dataset()

    print(f"\nCombined rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    df = clean_dataset(df)

    print(f"\nRows after cleaning: {len(df):,}")

    print("\nLabel distribution:")
    print(df["Label"].value_counts())

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nProcessed dataset saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()