from data.preprocessing import *
from data.tools import *

data_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\PROC"
target_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS\\ALL"
likely_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS\\LIKELY"
unlikely_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS\\UNLIKELY"

meta_path = "C:\ANALIZA_SZEREGOW_CZASOWYCH\METADANE_FULL_notime_15052024.xls"
meta = pd.read_excel(meta_path, header=1)

ds = load_pickled(data_path)
unlikely_ids = set(meta[meta['psh_prob'] == 0]['ID'].astype(str).tolist())
print(f"all unlikely ({len(unlikely_ids)}): {unlikely_ids}")
unlikely_ds = {key: value for key, value in ds.items() if key in unlikely_ids}
print(f"unlikely ({len(unlikely_ds.keys())})")

likely_ids = set(meta[meta['psh_prob'] == 1]['ID'].astype(str).tolist())
print(f"all likely ({len(likely_ids)}): {likely_ids}")
likely_ds = {key: value for key, value in ds.items() if key in likely_ids}
print(f"likely ({len(likely_ds.keys())}): {likely_ds.keys()}")

DIM = 5
for sig1 in ['LF', 'HR']:
    for sig2 in ['ICP', 'PRX']:
        perform_cca(ds, sig1, sig2, target_path, DIM, True)
        perform_cca(unlikely_ds, sig1, sig2, unlikely_path, DIM, True)
        perform_cca(likely_ds, sig1, sig2, likely_path, DIM, True)
