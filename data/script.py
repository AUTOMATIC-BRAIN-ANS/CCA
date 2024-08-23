from data.preprocessing import *
from tools import *

data_path = "D:\\MN\\PROC"
target_path = "D:\\MN\\RESULTS\\ALL"
likely_path = "D:\\MN\\RESULTS\\LIKELY"
unlikely_path = "D:\\MN\\RESULTS\\UNLIKELY"

meta_path = "D:\\MN\\METADANE_FULL_notime_15052024.xls"
meta = pd.read_excel(meta_path, header=1)

ds = load_pickled(data_path)
unlikely = meta[meta['Probable or Possible PSH'] == 0]
unlikely_ids = unlikely['ID'].astype(str).tolist()
unlikely_ds = {key: value for key, value in ds.items() if key in unlikely_ids}

likely = meta[meta['Probable or Possible PSH'] == 1]
likely_ids = likely['ID'].astype(str).tolist()
likely_ds = {key: value for key, value in ds.items() if key in likely_ids}


for sig1 in ['LF', 'HR']:
    for sig2 in ['ICP', 'PRX']:
        perform_cca(ds, sig1, sig2, target_path)
        perform_cca(unlikely_ds, sig1, sig2, unlikely_path)
        perform_cca(likely_ds, sig1, sig2, likely_path)

