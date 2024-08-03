import numpy as np


def calculate_averages(dataset, n_hours=6):
    average_dict = {}
    window = n_hours * 60
    for name, dataframe in dataset.items():
        average_df = dataframe.rolling(window=window, win_type=None, step=0.6*window).mean().dropna()
        average_dict[name] = average_df
    return average_dict


def build_matrix(avg_dict, idx):
    rows = []
    for name, averages in avg_dict.items():
        that_row = averages.iloc[idx].to_numpy()
        rows.append(that_row)
    return np.vstack(rows)

