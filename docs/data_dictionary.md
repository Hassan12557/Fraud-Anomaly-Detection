

\# Dataset Metadata and Data Dictionary



\## 1. Dataset Identity



\- Name: Credit Card Fraud Detection

\- Publisher: Machine Learning Group, ULB

\- Distribution source: Kaggle

\- Dataset identifier: mlg-ulb/creditcardfraud

\- Expected filename: creditcard.csv

\- Original collection period: September 2013

\- Geographic context: European cardholders

\- Coverage: Two days of transactions

\- Format: CSV



\## 2. Dataset Dimensions



\- Expected records: 284,807

\- Expected columns: 31

\- Fraud records: 492

\- Legitimate records: 284,315

\- Fraud proportion: Approximately 0.173%



\## 3. Data Dictionary



| Column | Description | Role |

|---|---|---|

| Time | Seconds since first transaction | Feature |

| V1–V28 | Anonymized PCA components | Features |

| Amount | Transaction amount | Feature |

| Class | 1 = fraud, 0 = legitimate | Evaluation label |



\## 4. Intended Use



This dataset will be used to develop and evaluate

unsupervised anomaly-detection methods.



The Class column will be excluded from model training

and retained only for evaluation.



\## 5. Known Limitations



\- Data is from 2013.

\- Only two days of transactions are represented.

\- V1–V28 are anonymized.

\- Merchant, customer, device, and location details

&#x20; are not available.

\- The dataset may not represent current fraud patterns.



\## 6. Source



https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud



\## 7. Data Handling



\- Raw data is stored locally in data/raw/.

\- Raw data is not committed to GitHub.

\- Cleaning decisions must be documented.

\- Original records must be preserved.



