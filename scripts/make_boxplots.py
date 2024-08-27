import pandas as pd
import matplotlib.pyplot as plt


def plot_boxplots(csv_file, labels, save_path):
    df = pd.read_csv(csv_file, index_col=0)
    data = [df.abs().iloc[i] for i in range(len(df))]
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=labels, showfliers=False)
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
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\LF_ICP\LF_weights.csv",


         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\HR_PRX\HR_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\HR_PRX\PRX_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\HR_PRX\HR_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\HR_PRX\PRX_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\HR_ICP\ICP_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\HR_ICP\HR_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\HR_ICP\ICP_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\LIKELY\HR_ICP\HR_weights.csv",


         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\ALL\LF_ICP\ICP_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\ALL\LF_ICP\LF_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\ALL\LF_PRX\PRX_weights.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\ALL\LF_PRX\LF_weights.csv"
         ]


label_list = ['a', 'b', 'c', 'freq', 'amp', 'phase',  'entropy']
# label_list = ['a', 'b', "c",'freq', 'amp', 'phase']

for idx in range(len(files)):
    plot_boxplots(files[idx], label_list, files[idx][:-4] + ".png")
