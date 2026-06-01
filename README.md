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
| Random Forest | 79.11% |
| Top 3 Features | 81.11% |
| Ratio Features | 81.11% |
| XGBoost | 81.11% |
| Random Forest + Grid Search | 83.33% |
| Champion Model (Random Forest + Feature Selection) | 85.56% |

### Champion Model

Algorithm: Random Forest Classifier

Best Hyperparameters:

python RandomForestClassifier(     n_estimators=100,     max_depth=3,     min_samples_leaf=1,     min_samples_split=2,     random_state=42 ) 

Selected Features:

1. L-tyrosine_3m
2. lipoproteins_preop
3. L-allo-Isoleucine_preop
4. creatinine_preop
5. glycine_preop
6. lipoproteins_delta
7. L-glutamine_delta

Cross-Validation Results (5-Fold):

text Fold Scores: [0.60, 0.90, 0.89, 1.00, 0.89]  Mean Accuracy: 85.56% 

### Key Findings

- L-tyrosine_3m was one of the most predictive biomarkers for recovery outcome.
- Lipoprotein-related metabolites showed strong predictive value.
- Feature selection significantly improved model performance.
- The final Random Forest model achieved the highest accuracy of 85.56% using only 7 selected biomarkers.

### Conclusion

This study demonstrates that metabolomics biomarkers can be used to predict patient recovery outcomes with high accuracy. Using feature selection and Random Forest optimization, the final model achieved 85.56% cross-validated accuracy, indicating strong potential for recovery prediction based on metabolomic pr

## Project Structure

text data/ raw_data/ results/ scripts/  README.md requirements.txt .gitignore 

---

## How to Run

Install packages:

bash pip install -r requirements.txt 

Run scripts:

bash python scripts/step22_train_model.py python scripts/step25_feature_search.py python scripts/step28_grid_search.py 

---