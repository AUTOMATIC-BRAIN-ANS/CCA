import pandas as pd
import matplotlib.pyplot as plt


def plot_stacked_barplot(csv_file, save_path):
    df = pd.read_csv(csv_file, index_col=1)
    df = df.drop(df.columns[0], axis=1)
    df = df.abs().div(df.abs().sum(axis=0), axis=1)
    plt.figure(figsize=(10, 6))
    bottom = None
    for idx, row in df.iterrows():
        if bottom is None:
            bottom = row
            plt.bar(df.columns, row, label=f'component {idx}')
        else:
            plt.bar(df.columns, row, bottom=bottom, label=f'component {idx}')
            bottom += row

    plt.xlabel('variables')
    plt.ylabel('component')
    plt.title('')
    plt.legend()
    plt.savefig(save_path)
    plt.show()
    plt.close()


files = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_PRX\stats.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\LF_ICP\stats.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\HR_PRX\stats.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\\UNLIKELY\HR_ICP\stats.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\LIKELY\LF_PRX\stats.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\LIKELY\LF_ICP\stats.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\LIKELY\HR_PRX\stats.csv",
         "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS\LIKELY\HR_ICP\stats.csv"]

for file in files:
    plot_stacked_barplot(file, file[:-4]+".png")

