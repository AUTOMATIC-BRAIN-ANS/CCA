from data.preprocessing import *
from data.tools import *

data_path = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\PROC"

target_path_GR = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_GR\\ALL"
probably_path_GR = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_GR\\PROBABLY"
possibly_path_GR = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_GR\\POSSIBLY"
unlikely_path_GR = "C:\\Users\\48503\\Desktop\\PSH_patients_for_tests\\RESULTS_GR\\UNLIKELY"

meta_path = "C:\ANALIZA_SZEREGOW_CZASOWYCH\METADANE_FULL_notime_15052024.xls"
meta = pd.read_excel(meta_path, header=1)

ds = load_pickled(data_path)
unlikely_ids = set(meta[meta['psg_category'] == 'unlik']['ID'].astype(str).tolist())
print(f"all unlikely ({len(unlikely_ids)}): {unlikely_ids}")
unlikely_ds = {key: value for key, value in ds.items() if key in unlikely_ids}
print(f"unlikely ({len(unlikely_ds.keys())})")

probably_ids = set(meta[meta['psg_category'] == 'probab']['ID'].astype(str).tolist())
print(f"all likely ({len(probably_ids)}): {probably_ids}")
probably_ds = {key: value for key, value in ds.items() if key in probably_ids}
print(f"likely ({len(probably_ds.keys())}): {probably_ds.keys()}")

possibly_ids = set(meta[meta['psg_category'] == 'possibke']['ID'].astype(str).tolist())
print(f"all likely ({len(possibly_ids)}): {possibly_ids}")
possibly_ds = {key: value for key, value in ds.items() if key in possibly_ids}
print(f"likely ({len(possibly_ds.keys())}): {possibly_ds.keys()}")

DIM = 5
entropy = True
for sig1 in ['LF', 'HR']:
    for sig2 in ['ICP', 'PRX']:
        perform_cca(ds, sig1, sig2, target_path_GR, DIM, 'clip', entropy, 'all')
        perform_cca(unlikely_ds, sig1, sig2, unlikely_path_GR, DIM, 'clip', entropy, 'unlikely')
        perform_cca(possibly_ds, sig1, sig2, possibly_path_GR, DIM, 'clip', entropy, 'possibly')
        perform_cca(probably_ds, sig1, sig2, probably_path_GR, DIM, 'clip', entropy, 'probably')
