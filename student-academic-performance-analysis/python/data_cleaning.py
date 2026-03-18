import pandas as pd

# Load dataset
df = pd.read_excel("student_academic_performance.xlsx")

# -----------------------------
# Handle Missing Values
# -----------------------------

# Fill missing study time with median
df["Study Time per Week"] = df["Study Time per Week"].fillna(
    df["Study Time per Week"].median()
)

# Fill missing categorical values
df["Parental Education"] = df["Parental Education"].fillna("Unknown")
df["Lunch Type"] = df["Lunch Type"].fillna(df["Lunch Type"].mode()[0])
df["Internet Access"] = df["Internet Access"].fillna(df["Internet Access"].mode()[0])

# -----------------------------
# Fix Data Types
# -----------------------------

categorical_columns = [
    "Student ID",
    "Gender",
    "Race/Ethnicity",
    "Parental Education",
    "Lunch Type",
    "Test Preparation",
    "School Type",
    "Internet Access"
]

df[categorical_columns] = df[categorical_columns].astype("string")

# -----------------------------
# Clean Sleep Duration
# -----------------------------

df.loc[
    (df["Daily Sleep Duration"] < 3) | 
    (df["Daily Sleep Duration"] > 12),
    "Daily Sleep Duration"
] = None

df["Daily Sleep Duration"] = df["Daily Sleep Duration"].fillna(
    df["Daily Sleep Duration"].median()
)

# -----------------------------
# Clean Score Columns
# -----------------------------

score_columns = ["Math Score", "Reading Score", "Writing Score"]

df[score_columns] = df[score_columns].apply(pd.to_numeric, errors="coerce")

for col in score_columns:
    df.loc[(df[col] < 0) | (df[col] > 100), col] = None
    df[col] = df[col].fillna(df[col].mean())

df[score_columns] = df[score_columns].round(0)

# -----------------------------
# Create Average Score
# -----------------------------

df["Average Score"] = df[score_columns].mean(axis=1).round(2)

# -----------------------------
# Internet Access Text Column
# -----------------------------

df["Internet Access"] = df["Internet Access"].astype(float).astype(int)

df["Internet Access Text"] = df["Internet Access"].map({
    1: "Yes",
    0: "No"
})

# -----------------------------
# Save Clean Dataset
# -----------------------------

df.to_excel("student_academic_performance_cleaned.xlsx", index=False)