"document" id="41852"}
# Recovery Prediction Using Metabolomics

## Project Overview

This project aims to predict patient recovery outcomes using metabolomics biomarkers and machine learning techniques.

The workflow includes:

- Data preprocessing
- PCA analysis
- Biomarker ranking
- Volcano plot analysis
- Recovery clustering
- Machine learning prediction
- Feature selection
- SHAP interpretation
- Hyperparameter optimization

---

## Dataset

Source:

- MetaboLights MTBLS242

Patients:

- 47 patients

Classes:

- Fast Recovery
- Poor Recovery

---

## Workflow

### 1. Data Preprocessing

- Clean metabolomics dataset
- Normalize metabolite values
- Generate machine learning dataset

### 2. Exploratory Data Analysis

- PCA
- Correlation Heatmap
- Recovery Trajectory

### 3. Biomarker Discovery

- Volcano Plot
- Biomarker Ranking
- SHAP Analysis

### 4. Machine Learning

Models tested:

- Random Forest
- Extra Trees
- XGBoost
- SVM

### 5. Feature Selection

Top biomarkers:

- L-tyrosine_3m
- lipoproteins_preop
- L-allo-Isoleucine_preop

---

## Results

| Model | Accuracy |
|---------|---------|
| Random Forest | 0.791 |
| Top 3 Features | 0.811 |
| Ratio Features | 0.811 |
| Random Forest + Grid Search | 0.833 |
| Extra Trees | 0.744 |
| XGBoost | 0.724 |
| SVM | 0.771 |

### Best Model

Random Forest + Grid Search

Accuracy:

83.33%

---

## Project Structure

text data/ raw_data/ results/ scripts/  README.md requirements.txt .gitignore 

---

## How to Run

Install packages:

bash pip install -r requirements.txt 

Run scripts:

bash python scripts/step22_train_model.py python scripts/step25_feature_search.py python scripts/step28_grid_search.py 

---