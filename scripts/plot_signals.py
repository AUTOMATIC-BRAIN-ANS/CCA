import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


from data.preprocessing import *
from data.tools import *
import numpy as np
from scipy.signal import medfilt

data_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\PROC"
ds = load_pickled(data_path)
filter_dict = {'PRX': 1, 'ICP': 200, 'LF': 600, 'HR': 200}
path = "C:\\Users\\48503\Desktop\PSH_patients_for_tests\SignalPlots"

for name, value in ds.items():
    figure, axis = plt.subplots(4, 1)
    icp = np.clip(value['ICP'], None, filter_dict['ICP'])
    prx = np.clip(value['PRX'], None, filter_dict['PRX'])
    hr = np.clip(value['HR'], None, filter_dict['HR'])
    lf = np.clip(value['LF'], None, filter_dict['LF'])
    axis[0].plot(value['Hours'], icp)
    axis[0].set_ylabel('ICP [mmHg]')
    axis[1].plot(value['Hours'], prx)
    axis[1].set_ylabel('PRx')
    axis[2].plot(value['Hours'], hr)
    axis[2].set_ylabel('HR [bpm]')
    axis[3].plot(value['Hours'], lf)
    axis[3].set_ylabel('HRV LF [$ms^2$]')
    axis[3].set_xlabel('Time [h]')
    axis[0].set_title('')
    for ax in axis:
        ax.set_xlim([0, 24])
        ax.xaxis.set_major_locator(MultipleLocator(4))
    plt.tight_layout()
    plt.savefig(f"{path}\\{name}.png", dpi=900)
    plt.show()
    plt.close()
