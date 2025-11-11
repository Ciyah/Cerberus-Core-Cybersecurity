# Cerberus-Core 🧠
> 🐍 An AI-powered Network Anomaly Detector built with Python, Pandas, and Scikit-learn.

---

## 💡 About This Project
Cerberus-Core is the intelligent engine for an autonomous security system. It's a Python script that uses a machine learning model to analyze network traffic and classify it as either **"Normal"** or **"Attack"**.

This project demonstrates the fundamentals of building a network intrusion detection system (IDS) by:
1.  **Loading & Pre-processing** a complex dataset.
2.  **Training** an AI classifier.
3.  **Evaluating** the model's performance on unseen data.

## ✨ Features
* **High-Accuracy AI Model:** Uses a `RandomForestClassifier` to detect anomalies with **99.69% accuracy** on the test set.
* **Intelligent Classification:** Classifies all network traffic into two simple categories: "Normal" (0) or "Attack" (1).
* **Automated Data Pre-processing:** Utilizes `pandas` to automatically clean and prepare the dataset, converting categorical features (like 'tcp', 'http') into a numerical format using one-hot encoding.
* **Built on Standard Libraries:** Leverages `scikit-learn` and `pandas` for a robust, industry-standard data science workflow.
* **Benchmark Trained:** The model is trained and validated on the trusted NSL-KDD dataset, a standard for intrusion detection research.

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

## 🔧 How to Run
1.  **Install dependencies:**
    ```bash
    pip install pandas scikit-learn numpy
    ```
2.  **Download the dataset:**
    Place the `KDDTrain+.csv` file in the same folder as the script (and rename it per the note above).

3.  **Navigate to the project folder:**
    Before running, you **must** change your terminal's directory to this project's folder.
    ```bash
    # Example for Windows
    cd "C:\Users\user\OneDrive\Desktop\Personal Projects\Project 2\"
    
    # Example for macOS/Linux
    cd /home/user/projects/Cerberus-Core/
    ```

4.  **Run the script:**
    ```bash
    # Once you are in the correct folder:
    python AnomalyDetector.py
    ```
---

## 📦 How to Create a Standalone Executable
You can bundle this script into a **single executable** for your operating system so you can run it without needing to install Python.

1.  **Install PyInstaller:**
    ```bash
    python -m pip install pyinstaller
    ```
2.  **Run the build command:**
    PyInstaller will create an executable for the OS you are currently on.

    * **On Windows (.exe):**
        ```bash
        pyinstaller --onefile -n CerberusCore.exe AnomalyDetector.py
        ```
    * **On macOS or Linux:**
        ```bash
        pyinstaller --onefile -n CerberusCore AnomalyDetector.py
        ```
3.  **Find your file:** Your new executable (`CerberusCore.exe` or `CerberusCore`) will be inside the new `dist` folder.

4.  **Run your new executable (from the terminal):**
    ```bash
    # On Windows
    .\dist\CerberusCore.exe

    # On macOS/Linux
    ./dist/CerberusCore
    ```
