import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score


def prepare_data(signal1, signal2, label):
    nb_rows = 9  # every person has 9 rows
    nb_patients = len(signal1) // nb_rows
    customer_data = []
    labels = []

    for i in range(nb_patients):
        customer_signal1 = signal1.iloc[i * nb_rows:(i + 1) * nb_rows].values
        customer_signal2 = signal2.iloc[i * nb_rows:(i + 1) * nb_rows].values

        customer_flat1 = customer_signal1.flatten()
        customer_flat2 = customer_signal2.flatten()
        customer_combined = np.concatenate([customer_flat1, customer_flat2])

        customer_data.append(customer_combined)
        labels.append(label)
    return np.array(customer_data), np.array(labels)


scores = []

for sig1 in ["LF", "HR"]:
    for sig2 in ["ICP", "PRX"]:
        possibly_file1 = pd.read_csv(
            f"C:\\Users\\48503\Desktop\PSH_patients_for_tests\RESULTS_GR\POSSIBLY\{sig1}_{sig2}\{sig1}_components.csv")
        possibly_file2 = pd.read_csv(
            f"C:\\Users\\48503\Desktop\PSH_patients_for_tests\RESULTS_GR\POSSIBLY\{sig1}_{sig2}\{sig2}_components.csv")

        probably_file1 = pd.read_csv(
            f"C:\\Users\\48503\Desktop\PSH_patients_for_tests\RESULTS_GR\PROBABLY\{sig1}_{sig2}\{sig1}_components.csv")
        probably_file2 = pd.read_csv(
            f"C:\\Users\\48503\Desktop\PSH_patients_for_tests\RESULTS_GR\PROBABLY\{sig1}_{sig2}\{sig2}_components.csv")

        unlikely_file1 = pd.read_csv(
            f"C:\\Users\\48503\Desktop\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\{sig1}_{sig2}\{sig1}_components.csv")
        unlikely_file2 = pd.read_csv(
            f"C:\\Users\\48503\Desktop\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\{sig1}_{sig2}\{sig2}_components.csv")

        X_a, labels_a = prepare_data(possibly_file1, possibly_file2, 0)  # label is "0" for possibly
        X_b, labels_b = prepare_data(probably_file1, probably_file2, 1)  # label is "1" for probably
        X_c, labels_c = prepare_data(unlikely_file1, unlikely_file2, 2)  # label is "2" for unlikely

        X = np.vstack((X_a, X_b, X_c))
        Y = np.concatenate((labels_a, labels_b, labels_c))

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

        model = LogisticRegression(multi_class='ovr', max_iter=1000)
        model.fit(X_train, Y_train)
        Y_pred_train = model.predict(X_train)
        Y_pred_test = model.predict(X_test)
        test_accuracy = accuracy_score(Y_test, Y_pred_test)
        train_accuracy = accuracy_score(Y_train, Y_pred_train)
        test_precision = precision_score(Y_test, Y_pred_test, average='weighted')
        test_recall = recall_score(Y_test, Y_pred_test, average='weighted')
        roc_auc = roc_auc_score(Y_test, model.predict_proba(X_test), multi_class='ovr')
        scores.append({"signals": f"{sig1}_{sig2}", "train accuracy": f"{train_accuracy:.2f}", "test accuracy": f"{test_accuracy:.2f}",
                       "test precision": f"{test_precision:.2f}", "test recall": f"{test_recall:.2f}", "roc auc score": f"{roc_auc:.2f}"})

score_df = pd.DataFrame(scores)
score_df.to_csv("log_regression_scores.csv")
print(score_df)

