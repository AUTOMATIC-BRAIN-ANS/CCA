from data.preprocessing import *
from data.tools import *

data_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\PROC"
target_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS\\ALL"
likely_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS\\LIKELY"
unlikely_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS\\UNLIKELY"

target_path_sk = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_SK\\ALL"
likely_path_sk = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_SK\\LIKELY"
unlikely_path_sk = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_SK\\UNLIKELY"

meta_path = "C:\ANALIZA_SZEREGOW_CZASOWYCH\METADANE_FULL_notime_15052024.xls"
meta = pd.read_excel(meta_path, header=1)

ds = load_pickled(data_path)
unlikely = meta[meta['psh_prob'] == 0]
unlikely_ids = unlikely['ID'].astype(str).tolist()
print(f"unlikely {len(unlikely_ids)}: {unlikely_ids}")
unlikely_ds = {key: value for key, value in ds.items() if key in unlikely_ids}
print(f"unlikely {len(unlikely_ds.keys())}")

likely = meta[meta['psh_prob'] == 1]
likely_ids = likely['ID'].astype(str).tolist()
print(f"likely {len(likely_ids)}: {likely_ids}")
print(likely_ids)
likely_ds = {key: value for key, value in ds.items() if key in likely_ids}
print(f"likely {len(likely_ds.keys())}")
DIM = 7
for sig1 in ['LF', 'HR']:
    for sig2 in ['ICP', 'PRX']:
        perform_cca(ds, sig1, sig2, target_path, DIM)
        perform_cca(unlikely_ds, sig1, sig2, unlikely_path, DIM)
        perform_cca(likely_ds, sig1, sig2, likely_path, DIM)

        perform_cca(ds, sig1, sig2, target_path_sk, DIM)
        perform_cca(unlikely_ds, sig1, sig2, unlikely_path_sk, DIM)
        perform_cca(likely_ds, sig1, sig2, likely_path_sk, DIM)

