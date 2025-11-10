import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import time

# ---
# 1. LOAD THE DATA
# ---

# These are the column names from the official NSL-KDD documentation.
col_names = ["duration", "protocol_type", "service", "flag", "src_bytes",
             "dst_bytes", "land", "wrong_fragment", "urgent", "hot", "num_failed_logins",
             "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
             "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
             "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
             "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
             "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
             "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
             "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
             "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "difficulty"]

print("--- [Step 1] Loading 'KDDTrain+.csv'... ---")
try:
    # Load the dataset from the .csv file
    df = pd.read_csv("KDDTrain+.csv", header=None, names=col_names)
except FileNotFoundError:
    print("---")
    print("Error: 'KDDTrain+.csv' not found.")
    print("Please make sure the file is in the same folder as the script.")
    print("---")
    exit()

print("Data loaded successfully.")
print("\n" + "="*50 + "\n")


# ---
# 2. PRE-PROCESS THE DATA (Convert Text to Numbers)
# ---
print("--- [Step 2] Pre-processing data (this is the fix)... ---")

# ----- Process the 'label' column -----
# We want a simple "Normal" (0) or "Attack" (1) model.
# If the label is 'normal', it becomes 0.
# If the label is anything else (like 'neptune', 'smurf', etc.), it becomes 1.
df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)
print("Processed 'label' column (0=normal, 1=attack).")

# ----- Process the feature columns (THE FIX) -----
# This is the part that removes 'tcp', 'http', etc.
# It converts 'protocol_type', 'service', and 'flag' into number columns.
df = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'])
print("Processed text columns ('protocol_type', 'service', 'flag') into numbers.")
print("Data is now 100% numerical.")
print("\n" + "="*50 + "\n")


# ---
# 3. PREPARE FOR TRAINING
# ---
print("--- [Step 3] Splitting data into Training and Testing sets... ---")

# X (the 'features') = all columns *except* the 'label'
X = df.drop('label', axis=1)

# y (the 'target') = *only* the 'label' column
y = df['label']

# Split the data: 80% for training, 20% for testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set has {len(X_train)} entries.")
print(f"Testing set has {len(X_test)} entries.")
print("\n" + "="*50 + "\n")


# ---
# 4. TRAIN THE AI MODEL
# ---
print("--- [Step 4] Training the AI model... ---")
print("(This may take a minute or two...)")

# We use a 'Random Forest', which is a powerful AI model for this task.
model = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)

# Start the timer
start_time = time.time()

# Train the model! This is where the error happened before.
model.fit(X_train, y_train)

# Stop the timer
end_time = time.time()
print(f"--- Model Training Complete! (Took {end_time - start_time:.2f} seconds) ---")
print("\n" + "="*50 + "\n")


# ---
# 5. TEST THE MODEL AND SHOW RESULTS
# ---
print("--- [Step 5] Evaluating model on the unseen test set... ---")

# Use the trained model to make predictions on the 'test' data
y_pred = model.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\n" + "="*50 + "\n")

# Print a detailed report
print("--- Classification Report ---")
print(classification_report(y_test, y_pred, target_names=['Normal (0)', 'Attack (1)']))

# This is the corrected line:
print("\n" + "="*50 + "\n")