# README.md

## 🧠 Project Overview
This project addresses the challenge of **entity resolution** — identifying and grouping records that refer to the same company, despite having variations in name, descriptions, or other attributes. The solution uses **semantic similarity** powered by transformer-based language models to group similar records together.

---

## 🎯 Goal
To detect duplicate company records and assign a `canonical_id` to all similar entries, so that each group of duplicates shares a unique identifier.

---

## 📂 Dataset
The input data (`data/companies.csv`) contains records of companies, each described by several fields. For this project, we focus on the following:
- `company_name`
- `short_description`
- `long_description`
- `product_type`
- `main_industry`
- `main_business_category`
- `main_sector`

These fields are extracted and embedded **individually** to preserve their meaning and allow field-specific comparison.

---

## 🔍 How It Works

1. **Extract Fields**
   - Extract and normalize relevant fields from each row (see `build_fields.py`).

2. **Generate Embeddings**
   - Use `SentenceTransformer` to convert each field's text into dense vector representations (see `generate_embeddings.py`).

3. **Compute Similarity**
   - Calculate cosine similarity separately for each field.
   - Combine these similarities using weighted averages based on field importance (e.g. `name` = 0.4, `short_description` = 0.2, etc.).

4. **Construct Similarity Graph**
   - Create a graph where nodes are company records and edges connect highly similar records.

5. **Extract Groups**
   - Use NetworkX to extract connected components (i.e. groups of similar companies).

6. **Assign Canonical IDs**
   - Assign a unique ID (`canonical_id`) to each group.
   - Rows with the same `canonical_id` are considered duplicates.

7. **Output**
   - Sort rows by `canonical_id`.
   - Place `canonical_id` as the first column.
   - Save results to `data/resolved_companies.csv`.

---

## 🧰 Tech Stack
- Python 3.10+
- `pandas`
- `sentence-transformers`
- `scikit-learn`
- `networkx`

---

## 📦 Setup & Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Place your input data in `data/companies.csv`

3. Run the resolution script:
```bash
python src/resolve_entities.py
```

Output will be saved to:
```
data/resolved_companies.csv
```

---

## 📌 Output Format
The output CSV contains all original data plus:
- `canonical_id`: groups similar companies

You can sort or group by this field in Excel to inspect clusters.

---

## 📊 Example (Simplified)
| canonical_id | company_name       | short_description        |
|--------------|--------------------|---------------------------|
| 101          | Apple Inc          | Consumer electronics     |
| 101          | Apple Corporation  | Electronics & software   |
| 202          | Microsoft          | Software and cloud       |

---

## 💡 Improvements for Future Work
- Tune weights dynamically with validation labels
- Use Approximate Nearest Neighbors for scale (e.g. FAISS)
- Improve canonical record selection (e.g. pick most complete)
