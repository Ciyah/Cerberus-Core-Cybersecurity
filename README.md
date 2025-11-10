# Cerberus-Core 🧠
> 🐍 An AI-powered Network Anomaly Detector built with Python, Pandas, and Scikit-learn.

---

## 💡 About This Project
Cerberus-Core is the intelligent engine for an autonomous security system. It's a Python script that uses a machine learning model to analyze network traffic and classify it as either **"Normal"** or **"Attack"**.

This project demonstrates the fundamentals of building a network intrusion detection system (IDS) by:
1.  **Loading & Pre-processing** a complex dataset.
2.  **Training** an AI classifier.
3.  **Evaluating** the model's performance on unseen data.

### Tech Stack
* **Python**
* **Pandas:** For loading, cleaning, and pre-processing the data.
* **Scikit-learn:** For splitting the data and building the `RandomForestClassifier` model.

### Topics
`python` `cybersecurity` `machine-learning` `ai` `intrusion-detection-system` `network-security` `data-science` `scikit-learn` `pandas`

---

## 📊 Dataset Used
This model was trained on the **NSL-KDD dataset**, a benchmark dataset for intrusion detection research. It's a cleaned-up version of the original KDD '99 dataset.

* **Download:** [NSL-KDD Dataset on Kaggle](https://www.kaggle.com/datasets/hassan-essam/nsl-kdd-dataset-for-network-intrusion-detection)
* **Training File:** `KDDTrain+.csv`
  > **Note:** The original file from the download may be a "Text Document" named `KDDTrain+` (with no extension). You must manually rename this file to `KDDTrain+.csv` for the script to work. (You may need to enable "File name extensions" in Windows Explorer to do this).

---

## 🚀 Results
The model was trained on 80% of the data and tested on the remaining 20%. The results were outstanding:

### Accuracy: 99.69%

### Classification Report
The model was able to identify both "Normal" and "Attack" traffic with near-perfect precision and recall.
