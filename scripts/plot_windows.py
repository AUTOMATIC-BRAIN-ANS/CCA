from data.preprocessing import *
from data.tools import *
import numpy as np
from scipy.signal import medfilt

data_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\PROC"
ds = load_pickled(data_path)


def plot_window(pac_nr, pac_df, signal_name, save_path, window_size=360, step_size=120):
    signal = pac_df[signal_name]
    for start in range(0, len(signal) - window_size + 1, step_size):
        x = np.arange(window_size)
        y = signal.iloc[start:start + window_size].values
        a, b, c = get_polyfit(x, y, True)
        plt.plot(x, y)
        plt.plot(x, medfilt(y, 25))
        plt.plot(x, np.clip(y, None, 600))

        plt.savefig(save_path + f"\\signal_{pac_nr}_{signal_name}_{start}.png")
        plt.title(f"a:{round(a, 3)}, b:{round(b, 3)}, c:{round(c, 3)}")
        plt.close()


def get_polyfit(x, y, free_term, deg=2):
    if not free_term:
        coefficients = np.polyfit(x, y, deg)[:-1]
    else:
        coefficients = np.polyfit(x, y, deg)
        if len(coefficients) < 3:
            coefficients = np.pad(coefficients, (0, 3 - len(coefficients)), 'constant')
    return coefficients
