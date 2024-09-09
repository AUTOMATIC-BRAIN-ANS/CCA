from data.preprocessing import *
from data.tools import *

data_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\PROC"
target_path_MEDIAN = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_MEDIAN\\ALL"
likely_path_MEDIAN = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_MEDIAN\\LIKELY"
unlikely_path_MEDIAN = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_MEDIAN\\UNLIKELY"

target_path_CLIP = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_CLIP\\ALL"
likely_path_CLIP = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_CLIP\\LIKELY"
unlikely_path_CLIP = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_CLIP\\UNLIKELY"


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
entropy = True
for sig1 in ['LF', 'HR']:
    for sig2 in ['ICP', 'PRX']:
        # perform_cca(ds, sig1, sig2, target_path_MEDIAN, DIM, 'median', entropy)
        # perform_cca(unlikely_ds, sig1, sig2, unlikely_path_MEDIAN, DIM, 'median', entropy)
        # perform_cca(likely_ds, sig1, sig2, likely_path_MEDIAN, DIM, 'median', entropy)

        perform_cca(ds, sig1, sig2, target_path_CLIP, DIM, 'clip', entropy, 'all')
        perform_cca(unlikely_ds, sig1, sig2, unlikely_path_CLIP, DIM, 'clip', entropy, 'unlikely')
        perform_cca(likely_ds, sig1, sig2, likely_path_CLIP, DIM, 'clip', entropy, 'likely')


