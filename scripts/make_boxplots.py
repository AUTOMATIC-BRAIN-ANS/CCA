import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_boxplots(csv_file, labels, save_path, group_type):
    df = pd.read_csv(csv_file, index_col=0)
    data = [df.abs().iloc[idx] for idx in range(len(df))]
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=labels, showfliers=False)
    plt.xlabel('variables')
    plt.ylabel('weights')
    plt.tight_layout()
    folder_name = os.path.basename(os.path.dirname(csv_file))
    plt.savefig(f"{save_path}_{folder_name}_{group_type}.pdf")
    plt.show()
    plt.close()


unlikely_files = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\LF_PRX\LF_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\LF_PRX\PRX_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\LF_ICP\ICP_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\LF_ICP\LF_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\HR_PRX\HR_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\HR_PRX\PRX_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\HR_ICP\ICP_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\HR_ICP\HR_weights.csv",

                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\LF_PRX\LF_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\\RESULTS_GR\\UNLIKELY\LF_PRX\PRX_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\LF_ICP\ICP_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\LF_ICP\LF_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\HR_PRX\HR_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\HR_PRX\PRX_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\HR_ICP\ICP_weights.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\UNLIKELY\HR_ICP\HR_weights.csv"
                  ]

likely_files = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\LIKELY\LF_PRX\LF_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\LIKELY\LF_PRX\PRX_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\LIKELY\LF_ICP\ICP_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\LIKELY\LF_ICP\LF_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\LIKELY\HR_PRX\HR_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\LIKELY\HR_PRX\PRX_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\LIKELY\HR_ICP\ICP_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\LIKELY\HR_ICP\HR_weights.csv"]

possibly_files = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\POSSIBLY\LF_PRX\LF_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\POSSIBLY\LF_PRX\PRX_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\POSSIBLY\LF_ICP\ICP_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\POSSIBLY\LF_ICP\LF_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\POSSIBLY\HR_PRX\HR_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\POSSIBLY\HR_PRX\PRX_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\POSSIBLY\HR_ICP\ICP_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\POSSIBLY\HR_ICP\HR_weights.csv"]

probably_files = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\PROBABLY\LF_PRX\LF_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\PROBABLY\LF_PRX\PRX_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\PROBABLY\LF_ICP\ICP_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\PROBABLY\LF_ICP\LF_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\PROBABLY\HR_PRX\HR_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\PROBABLY\HR_PRX\PRX_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\PROBABLY\HR_ICP\ICP_weights.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_GR\\PROBABLY\HR_ICP\HR_weights.csv"]

label_list = ['a', 'b', 'c', 'frequency', 'amplitude', 'phase', 'entropy']

for file in unlikely_files:
    plot_boxplots(file, label_list, file[:-4], "unlikely")

for file in likely_files:
    plot_boxplots(file, label_list, file[:-4], "likely")

for file in probably_files:
    plot_boxplots(file, label_list, file[:-4], "probably")

for file in possibly_files:
    plot_boxplots(file, label_list, file[:-4], "possibly")

