#!/usr/bin/env python
# coding: utf-8

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "data_mutations-all-cases.csv"

df = pd.read_csv(
    DATA_PATH,
    sep="\t",
    comment="#"
)

print("Dataset loaded successfully")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist()[:10])

egfr_df = df[df["Hugo_Symbol"] == "EGFR"].copy()

print("EGFR mutations:", egfr_df.shape[0])
print(egfr_df.head())

mutation_counts = egfr_df["HGVSp_Short"].value_counts()

print("\nTop EGFR mutations:")
print(mutation_counts.head(10))

top10 = mutation_counts.head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top10.values, y=top10.index)
plt.title("Top EGFR Mutations in Dataset")
plt.xlabel("Frequency")
plt.ylabel("Mutation")
plt.tight_layout()
plt.show()

if "Protein_position" in egfr_df.columns:
    positions = pd.to_numeric(egfr_df["Protein_position"], errors="coerce").dropna()

    plt.figure(figsize=(10, 6))
    plt.hist(positions, bins=50)
    plt.title("Distribution of EGFR mutation positions")
    plt.xlabel("Protein position")
    plt.ylabel("Mutation count")
    plt.tight_layout()
    plt.show()

if "Hotspot" in egfr_df.columns:
    print("\nHotspot counts:")
    print(egfr_df["Hotspot"].value_counts())