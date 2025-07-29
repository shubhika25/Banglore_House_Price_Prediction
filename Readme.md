
# Bangalore House Price Prediction

Predict real estate prices in Bangalore using features like location, square footage, number of bathrooms, and bedrooms. This is a full-stack machine learning project with an interactive frontend, Flask API backend, and deployment on Render.
URL : https://banglore-house-price-prediction-icum.onrender.com

<img width="1824" height="955" alt="image" src="https://github.com/user-attachments/assets/3ad624db-30d1-4277-a88c-0470d7de0ec5" />

---

## 📌 Overview

The goal of this project is to build a regression model that can estimate the price of a home in Bangalore based on user inputs. The application includes:

- Cleaned and preprocessed real-world data
- Exploratory data analysis (EDA) and feature engineering
- A trained linear regression model
- REST API using Flask
- Frontend interface for predictions
- Deployment using Render



##  Tech Stack

- **Python**, **Pandas**, **NumPy**
- **Scikit-learn** for machine learning
- **Flask** for backend API
- **HTML/CSS + JS** for frontend
- **Render** for deployment
- **Jupyter Notebook** for EDA and model development

## Model Evaluation and Selection
Approach
Cross-Validation:
Applied ShuffleSplit cross-validation with 5 splits and 20% test size to reliably estimate model performance and reduce overfitting risks.

Algorithms Tested:

Linear Regression

Lasso Regression (with tuning for alpha and selection)

Decision Tree Regressor (with default parameters)

Hyperparameter Tuning:
Used GridSearchCV to optimize model parameters and identify the best configurations.

| Model             | Best (R^2) Score | Best Hyperparameters                        |
| ----------------- | ---------------- | ------------------------------------------- |
| Linear Regression | 0.83             | Default parameters                          |
| Lasso Regression  | 0.68             | alpha=1, selection='cyclic'                 |
| Decision Tree     | 0.74             | criterion='squared\_error', splitter='best' |

