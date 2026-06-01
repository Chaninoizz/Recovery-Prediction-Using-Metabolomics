="55123"}
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
- Exhaustive feature search

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
- Ensemble Learning
- Stacking Classifier

### 5. Feature Selection

Final Selected Biomarkers:

- clinical_score
- L-allo-Isoleucine_preop
- creatinine_preop
- glycine_preop
- lipoproteins_ratio

---

## Results

| Model | Accuracy |
|---------|---------:|
| Random Forest Baseline | 79.11% |
| Top 3 Features | 81.11% |
| Ratio Features | 81.11% |
| XGBoost | 78.89% |
| Random Forest + Grid Search | 83.33% |
| Champion Model v1 (7 Features) | 85.56% |
| 🏆 Champion Model v2 (5 Features) | 89.33% |

---

## Final Champion Model

### Algorithm

Random Forest Classifier

### Cross-Validation Results (5-Fold)

Fold Scores:

text [0.80, 1.00, 0.78, 1.00, 0.89] 

Mean Accuracy:

text 89.33% 

Standard Deviation:

text 9.47% 

### Best Hyperparameters

python RandomForestClassifier(     n_estimators=100,     max_depth=3,     min_samples_leaf=1,     min_samples_split=2,     random_state=42 ) 

### Selected Biomarkers

1. clinical_score
2. L-allo-Isoleucine_preop
3. creatinine_preop
4. glycine_preop
5. lipoproteins_ratio

---

## Model Interpretation

SHAP analysis identified the following biomarkers as the most influential predictors of recovery outcome:

- clinical_score
- L-allo-Isoleucine_preop
- creatinine_preop
- glycine_preop
- lipoproteins_ratio

The use of engineered ratio features improved prediction performance while reducing the number of required biomarkers.

---

## Visualizations

### Confusion Matrix

Confusion Matrix

### SHAP Analysis

SHAP Analysis

---

## Key Findings

- Only five biomarkers were required to achieve the highest predictive performance.
- Feature engineering significantly improved model accuracy.
- Lipoprotein-related ratio features were more informative than raw lipoprotein measurements.
- Exhaustive feature search outperformed conventional feature selection methods.
- The final model achieved 89.33% cross-validated accuracy.
- L-allo-Isoleucine_preop consistently appeared as one of the strongest predictive biomarkers.
- Clinical information combined with metabolomics data substantially improved prediction performance.

---

## Conclusion

This study demonstrates that metabolomics biomarkers can be used to predict patient recovery outcomes with high accuracy.

After extensive experimentation involving:

- Feature Engineering
- Biomarker Ranking
- Boruta Feature Selection
- RFECV
- Random Forest Optimization
- XGBoost
- Ensemble Learning
- Stacking Classifiers
- Hyperparameter Optimization
- Exhaustive Feature Search
- SHAP Interpretation

the final Random Forest model achieved 89.33% cross-validated accuracy using only five biomarkers.

These results suggest that metabolomics-based recovery prediction has strong potential for future clinical decision support applications.

---

## Project Structure

Recovery-Prediction-Using-Metabolomics/

├── data/

│   ├── recovery_prediction_dataset.csv

│   ├── recovery_prediction_dataset_v2.csv

│   ├── recovery_prediction_dataset_v3.csv

│   └── model_comparison.csv

│

├── raw_data/

│   ├── Domain_2_NMR_results_MTBLS242.tsv

│   └── Domain_2_sample_table_MTBLS242.tsv

│

├── results/

│   ├── confusion_matrix.png

│   ├── confusion_matrix_v2.png

│   ├── champion_shap.png

│   └── champion_shap_v2.png

│

├── scripts/

│   ├── step22_train_model.py

│   ├── step25_feature_search.py

│   ├── step28_grid_search.py

│   ├── step33_champion_model.py

│   ├── step50_super_champion.py

│   ├── step51_confusion_matrix_v2.py

│   └── step52_shap_v2.py

│

├── README.md

├── requirements.txt

└── .gitignore
---

## How to Run

### Install Dependencies

bash pip install -r requirements.txt 

### Run Baseline Model

bash python scripts/step22_train_model.py 

### Run Feature Search

bash python scripts/step25_feature_search.py 

### Run Hyperparameter Optimization

bash python scripts/step28_grid_search.py 

### Run Final Champion Model

bash python scripts/step50_super_champion.py 

### Generate Confusion Matrix

bash python scripts/step51_confusion_matrix_v2.py 

### Generate SHAP Analysis

bash python scripts/step52_shap_v2.py 

---

## Author

-

School of Information Technology

King Mongkut's University of Technology Thonbur