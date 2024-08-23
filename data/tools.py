import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from models.CCA import MyCCA
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress


def fill_matrix(pac_dict, signal_name, window_size, step_size):
    variables = []
    for pac_nr, pac_df in pac_dict.items():
        signal = pac_df[signal_name]
        for start in range(0, len(signal) - window_size + 1, step_size):
            x = np.arange(window_size)
            y = signal.iloc[start:start + window_size].values
            a, b, c = get_polyfit(x, y)
            freq, amp, phase = get_fft(y)
            variables.append([pac_nr, a, b, c, freq, amp, phase])
    df = pd.DataFrame(variables, columns=['name', 'a', 'b', 'c', 'freq', 'amp', 'phase'])
    df.set_index('name', inplace=True)
    return df


def get_polyfit(x, y, deg=2):
    p = Polynomial.fit(x, y, deg)
    return p.convert().coef


def get_fft(signal, fs=1.0):
    n = len(signal)
    fft = np.fft.fft(signal)
    freq = np.fft.fftfreq(n, d=1/fs)
    amp = np.abs(fft)
    phase = np.angle(fft)

    main_index = np.argmax(amp[:n//2]) + 1
    main_freq = freq[main_index]
    main_amp = amp[main_index]
    main_phase = phase[main_index]

    return main_freq, main_amp, main_phase


def plot_corr_matrix(corr, signal1, signal2, save_path):
    corr_values_df = pd.DataFrame(corr)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_values_df, annot=True, cmap='coolwarm')
    plt.title(f'')
    plt.savefig(save_path + f"\\{signal1}_{signal2}\\corr_values_heatmap.png")
    plt.close()


def plot_scatter_components(components1, components2, signal1, signal2, save_path):
    for i in range(5):
        plt.figure()
        plt.scatter(components1[:, i], components2[:, i])
        plt.xlabel(f'{signal1} (column {i + 1})')
        plt.ylabel(f'{signal2} (column {i + 1})')
        plt.title(f'')
        if save_path:
            plt.savefig(f'{save_path}/scatter_component_{i + 1}.png')
        else:
            plt.show()
        plt.close()


def calculate_stats(components1, components2, signal1, signal2, save_path):
    stats = []
    for idx in range(5):
        col1 = components1[:, idx]
        col2 = components2[:, idx]

        std_dev1 = np.std(col1)
        std_dev2 = np.std(col2)

        slope, intercept, r_value, p_value, std_err = linregress(col1, col2)

        stats.append({'component': idx + 1, 'std_dev1': std_dev1, 'std_dev2': std_dev2, 'slope': slope,
                      'intercept': intercept, 'r_value': r_value, 'p_value': p_value, 'std_err': std_err})

    pd.DataFrame(stats).to_csv(save_path + f"\\{signal1}_{signal2}\\stats.csv")


def perform_cca(dataset, signal1, signal2, save_path, window_size=360, step_size=120, dim=6):
    x = fill_matrix(dataset, signal1, window_size, step_size)
    y = fill_matrix(dataset, signal2, window_size, step_size)

    x.to_csv(save_path + f"\\{signal1}_{signal2}\\{signal1}_matrix.csv")
    y.to_csv(save_path + f"\\{signal1}_{signal2}\\{signal2}_matrix.csv")

    cca = MyCCA(dim)
    x_matrix, y_matrix = x.to_numpy(), y.to_numpy()
    cca.fit(x_matrix, y_matrix)
    components1, components2 = cca.transform(x_matrix, y_matrix)

    pd.DataFrame(cca.weights_x).to_csv(save_path + f"\\{signal1}_{signal2}\\{signal1}_weights.csv")
    pd.DataFrame(cca.weights_y).to_csv(save_path + f"\\{signal1}_{signal2}\\{signal2}_weights.csv")

    plot_corr_matrix(cca.corr_values, signal1, signal2, save_path)
    plot_scatter_components(components1, components2, signal1, signal2, save_path + f"\\{signal1}_{signal2}")
    calculate_stats(components1, components2, signal1, signal2, save_path)