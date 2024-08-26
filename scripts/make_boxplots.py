import pandas as pd
import matplotlib.pyplot as plt


def plot_boxplots(csv_file, matrix, labels, save_path):
    df = pd.read_csv(csv_file, index_col=0)
    mx = pd.read_csv(matrix, index_col=0)
    print(df)
    std_devs = mx.std(axis=0)

    data = [df.iloc[i] / std_devs[i] for i in range(len(df))]
    print(data)

    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=labels, showfliers=True)
    plt.xlabel('variables')
    plt.ylabel('weights')
    plt.title('')
    plt.savefig(save_path)
    plt.show()
    plt.close()


files = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_PRX\LF_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_PRX\PRX_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_PRX\LF_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_PRX\PRX_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_ICP\ICP_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_ICP\LF_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_ICP\ICP_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_ICP\LF_weights.csv"]

matrices = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_PRX\LF_matrix.csv",
            "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_PRX\PRX_matrix.csv",
            "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_PRX\LF_matrix.csv",
            "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_PRX\PRX_matrix.csv",
            "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_ICP\ICP_matrix.csv",
            "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_ICP\LF_matrix.csv",
            "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_ICP\ICP_matrix.csv",
            "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_ICP\LF_matrix.csv"]
label_list = ['a', 'b', 'freq', 'amp', 'phase']
# label_list = ['a', 'b', "c",'freq', 'amp', 'phase']

for idx in range(len(files)):
    plot_boxplots(files[idx], matrices[idx], label_list, files[idx][:-4] + ".png")
