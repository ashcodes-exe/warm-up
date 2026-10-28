# Warm-up

Short practice scripts for ML and Python basics. 

## What's here

- **logistic_regression.py**: Logistic Regression baseline (train/test split + accuracy)
- **xgboost_warmup.py**: XGBoost baseline
- **catboost_warmup.py**: CatBoost baseline
- **plotting_basics.py**: box plots, violin plots & histograms with matplotlib
- **multi_panel_plots.py**: histogram, scatter, error bar & box plot combined into one figure
- **pandas_titanic.py**: pandas exploration of the Titanic dataset: indexing, filtering, grouping, missing values
- **logistic_regression.py**: Logistic Regression baseline (linear boundary)
- **decision_tree.py**: Decision Tree baseline (single tree)
- **random_forest.py**: Random Forest baseline (bagged trees)
- **adaboost_warmup.py**: AdaBoost baseline (boosted stumps)
- **xgboost_warmup.py**: XGBoost baseline (external lib)
- **catboost_warmup.py**: CatBoost baseline (external lib)

## The point

These are small, self-contained scripts. The ML ones establish a baseline (train/test split + accuracy) for Logistic Regression, XGBoost & CatBoost on the same dataset so they can be compared side by side. The plotting and pandas files are coursework for data handling and visualization.

## Data

Scripts expect data files in the repo root (not included):

- `train_dataset.csv`: for the ML scripts
- Titanic CSV: for `pandas_titanic.py` (Titanic passenger dataset)

## Built with

Python, pandas, scikit-learn, XGBoost, CatBoost, Matplotlib

## Before running

pip install pandas scikit-learn xgboost catboost matplotlib
