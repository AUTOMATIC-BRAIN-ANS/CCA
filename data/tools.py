import os
import pandas as pd
import numpy as np
from models.CCA import MyCCA
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import antropy as ent
from scipy.signal import medfilt


def fill_matrix(pac_dict, signal_name, offset, window_size, step_size, filter_type, if_entropy):
    filter_dict = {'PRX': 1, 'ICP': 200, 'LF': 600, 'HR': 200}
    variables = []
    for pac_nr, pac_df in pac_dict.items():
        signal = pac_df[signal_name]
        for start in range(offset, len(signal) - window_size + 1, step_size):
            x = np.arange(window_size)
            y = signal.iloc[start:start + window_size].values

            if filter_type == 'clip':
                y = np.clip(y, None, filter_dict[signal_name])
            elif filter_type == 'median':
                y = medfilt(y, 25)

            a, b, c = get_polyfit(x, y, True)
            freq, amp, phase = get_fft(y)

            if if_entropy:
                entropy_val = compute_spectral_entropy(y)
                variables.append([pac_nr, a, b, c, freq, amp, phase, entropy_val])
            else:
                variables.append([pac_nr, a, b, c, freq, amp, phase])

    if if_entropy:
        df = pd.DataFrame(variables, columns=['name', 'a', 'b', 'c', 'freq', 'amp', 'phase', 'entropy'])
    else:
        df = pd.DataFrame(variables, columns=['name', 'a', 'b', 'c', 'freq', 'amp', 'phase'])

    df.set_index('name', inplace=True)
    return df


def compute_spectral_entropy(signal, fs=1.0):
    spectral_entropy = ent.spectral_entropy(signal, sf=fs, method='welch')
    return spectral_entropy


def get_polyfit(x, y, free_term, deg=2):
    if not free_term:
        coefficients = np.polyfit(x, y, deg)[:-1]
    else:
        coefficients = np.polyfit(x, y, deg)
        if len(coefficients) < 3:
            coefficients = np.pad(coefficients, (0, 3 - len(coefficients)), 'constant')
    return coefficients


def get_fft(signal, fs=1.0):
    n = len(signal)
    fft = np.fft.rfft(signal)
    freq = np.fft.fftfreq(n, d=1 / fs)
    amp = np.abs(fft)
    phase = np.angle(fft)

    main_index = np.argmax(amp[1:])
    main_freq = freq[main_index]
    main_amp = amp[main_index]
    main_phase = phase[main_index]

    return main_freq, main_amp, main_phase


def plot_corr_matrix(corr, signal1, signal2, save_path):
    corr_values_df = pd.DataFrame(corr)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_values_df, annot=True, cmap='coolwarm')
    plt.title(f'')
    plt.savefig(save_path + f"\\corr_values_heatmap.pdf")
    plt.close()


def plot_scatter_components(components1, components2, signal1, signal2, save_path, dim, group_type):
    for i in range(dim):
        plt.figure()
        plt.scatter(components1[:, i], components2[:, i])
        plt.xlabel(f'{signal1}')
        plt.ylabel(f'{signal2}')
        # plt.title(f'')
        plt.tight_layout()
        plt.savefig(f'{save_path}/scatter_component_{i + 1}_{group_type}_{signal1}_{signal2}.pdf')
        plt.show()
        plt.close()


def calculate_stats(components1, components2, signal1, signal2, save_path, dim):
    stats = []
    for idx in range(dim):
        col1 = components1[:, idx]
        col2 = components2[:, idx]

        std_dev1 = np.std(col1)
        std_dev2 = np.std(col2)

        slope, intercept, r_value, p_value, std_err = linregress(col1, col2)

        stats.append({'component': idx + 1, 'std_dev1': std_dev1, 'std_dev2': std_dev2, 'slope': slope,
                      'intercept': intercept, 'r_value': r_value, 'p_value': p_value, 'std_err': std_err})

    pd.DataFrame(stats).to_csv(save_path + f"\\stats.csv")


def normalize(dataframe):
    return (dataframe - dataframe.min()) / (dataframe.max() - dataframe.min())


def perform_cca(dataset, signal1, signal2, save_path, dim, filter_type, entropy, group_type, offset=120, window_size=360, step_size=120):
    x = fill_matrix(dataset, signal1, offset, window_size, step_size, filter_type, entropy)
    y = fill_matrix(dataset, signal2, offset, window_size, step_size, filter_type, entropy)

    path = save_path + f"\\{signal1}_{signal2}"
    if not os.path.exists(path):
        os.makedirs(path)

    x.to_csv(path + f"\\{signal1}_matrix_unnormalized.csv")
    y.to_csv(path + f"\\{signal2}_matrix_unnormalized.csv")

    x = normalize(x)
    y = normalize(y)

    x.to_csv(path + f"\\{signal1}_matrix.csv")
    y.to_csv(path + f"\\{signal2}_matrix.csv")

    cca = MyCCA(dim)
    x_matrix, y_matrix = x.to_numpy(), y.to_numpy()
    cca.fit(x_matrix, y_matrix)
    components1, components2 = cca.transform(x_matrix, y_matrix)

    pd.DataFrame(cca.weights_x).to_csv(path + f"\\{signal1}_weights.csv")
    pd.DataFrame(cca.weights_y).to_csv(path + f"\\{signal2}_weights.csv")

    pd.DataFrame(components1).to_csv(path + f"\\{signal1}_components.csv")
    pd.DataFrame(components2).to_csv(path + f"\\{signal2}_components.csv")

    plot_corr_matrix(cca.corr_values, signal1, signal2, path)
    plot_scatter_components(components1, components2, signal1, signal2, path, dim, group_type)
    calculate_stats(components1, components2, signal1, signal2, path, dim)
