# Autism Screening ML 🧩

A machine learning project that predicts the likelihood of Autism Spectrum Disorder (ASD) based on behavioral screening responses from the AQ-10 questionnaire.

## Status

🚧 Work in Progress

## Dataset

- **Source:** Kaggle - Autism Screening on Adults
- **Size:** 704 records, 21 features
- **Target:** Class/ASD (YES/NO)

## Tech Stack

- Python
- Pandas
- Scikit-learn
- XGBoost
- Streamlit

## AQ-10 Screening Questions

- **A1** — I often notice small sounds when others do not
- **A2** — I usually concentrate more on the whole picture, rather than small details
- **A3** — I find it easy to do more than one thing at once
- **A4** — If there is an interruption, I can switch back to what I was doing quickly
- **A5** — I find it easy to read between the lines when someone is talking to me
- **A6** — I know how to tell if someone listening to me is getting bored
- **A7** — When reading a story I find it difficult to work out characters' intentions
- **A8** — I like to collect information about categories of things
- **A9** — I find it easy to work out what someone is thinking just by looking at their face
- **A10** — I find it difficult to work out people's intentions

## Model Selection

I compared Random Forest and XGBoost:

| Model         | Accuracy | Recall (ASD) |
| ------------- | -------- | ------------ |
| Random Forest | 98.6%    | 0.97         |
| XGBoost       | 97.9%    | 1.00         |

I chose XGBoost because in a healthcare context, false negatives are more costly than false positives. XGBoost achieved 100% recall on the ASD class, meaning it never missed a real case.

## Data Cleaning

- Dropped `age_desc` (no useful information) and `result` (data leakage)
- Fixed age outlier (383 → median) and 2 missing age values
- Replaced `?` in ethnicity and relation with `Unknown`
- Label encoded binary columns (gender, jundice, etc.)
- One hot encoded categorical columns (ethnicity, relation)
- Dropped `contry_of_res` to reduce dimensionality (100 → 34 columns)
