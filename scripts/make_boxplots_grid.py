import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_boxplots(csv_files, labels, save_path, group, signal1, signal2, which_signal):
    all_data = [pd.DataFrame() for _ in range(len(labels))]
    for csv_file in csv_files:
        df = pd.read_csv(csv_file, index_col=0)
        for idx in range(len(df)):
            all_data[idx] = pd.concat([all_data[idx], df.abs().iloc[idx]], axis=0)
    print(all_data)

    data_to_plot = [all_data[i].values.flatten() for i in range(len(all_data))]

    plt.figure(figsize=(10, 6))
    plt.boxplot(data_to_plot, labels=labels, showfliers=False)
    plt.xlabel('variables')
    plt.ylabel('weights')
    plt.tight_layout()
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    plt.savefig(f"{save_path}\\{group}_{signal1}_{signal2}_{which_signal}.pdf")
    plt.show()
    plt.close()


offset_list = [30, 60, 90, 120]
step_size_list = [90, 120, 150, 180]
window_size_list = [240, 300, 360, 420]

label_list = ['a', 'b', 'c', 'frequency', 'amplitude', 'phase', 'entropy']

for group_type in ['UNLIKELY', 'POSSIBLY', 'PROBABLY']:
    for sig1 in ['LF', 'HR']:
        for sig2 in ['ICP', 'PRX']:
            same_sig1 = []
            same_sig2 = []
            for offset in offset_list:
                for step_size in step_size_list:
                    for window_size in window_size_list:
                        file_sig1 = f"D:\\GridSearch\\RESULTS_GR\\{group_type}\\O{offset}_S{step_size}_W{window_size}\\{sig1}_{sig2}\\{sig1}_weights.csv"
                        same_sig1.append(file_sig1)
                        file_sig2 = f"D:\\GridSearch\\RESULTS_GR\\{group_type}\\O{offset}_S{step_size}_W{window_size}\\{sig1}_{sig2}\\{sig2}_weights.csv"
                        same_sig2.append(file_sig2)
            plot_boxplots(same_sig1, label_list, "D:\\GridSearch\\Boxplots", group_type, sig1, sig2, 1)
            plot_boxplots(same_sig2, label_list, "D:\\GridSearch\\Boxplots", group_type, sig1, sig2, 2)
