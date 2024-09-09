import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_stacked_barplot(csv_file, save_path, group_type):
    df = pd.read_csv(csv_file, index_col=1)
    df = df.drop(df.columns[0], axis=1)
    df = df.abs().div(df.abs().sum(axis=0), axis=1)
    plt.figure(figsize=(10, 6))
    colors = plt.get_cmap('tab20').colors

    bottom = None
    for idx, row in df.iterrows():
        if bottom is None:
            bottom = row
            plt.bar(df.columns, row, label=f'component {idx}', color=colors[idx % len(colors)])
        else:
            plt.bar(df.columns, row, bottom=bottom, label=f'component {idx}', color=colors[idx % len(colors)])
            bottom += row

    plt.xlabel('variables')
    plt.ylabel('fraction')
    plt.tight_layout()
    plt.legend()
    folder_name = os.path.basename(os.path.dirname(csv_file))
    plt.savefig(f"{save_path}_{folder_name}_{group_type}.pdf")

    plt.show()
    plt.close()


unlikely_files = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\LF_PRX\stats.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\LF_ICP\stats.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\HR_PRX\stats.csv",
                  "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\\UNLIKELY\HR_ICP\stats.csv"]
likely_files = ["C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\LIKELY\LF_PRX\stats.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\LIKELY\LF_ICP\stats.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\LIKELY\HR_PRX\stats.csv",
                "C:\\Users\\48503\Desktop\\PSH_patients_for_tests\RESULTS_CLIP\LIKELY\HR_ICP\stats.csv"]

for file in unlikely_files:
    plot_stacked_barplot(file, file[:-4], 'unlikely')

for file in likely_files:
    plot_stacked_barplot(file, file[:-4], 'likely')
