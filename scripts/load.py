from data.preprocessing import *
import os
import pandas as pd

load = "C:\\ANALIZA_SZEREGOW_CZASOWYCH\\CSV_with_results"
save = "C:\\Users\\48503\Desktop\PSH_patients_for_tests\PROC"
ds = load_files(load)
# missing_over_threshold(ds)
# print_nb_cols(ds)


nb_days = 1
for file in os.listdir(load):
    if file.endswith(".csv"):
        name = file[:-4]
        dataframe = pd.read_csv(os.path.join(load, file), sep=';', encoding='latin1',
                                decimal=',')

        if len(dataframe) >= nb_days * 24 * 60:
            dataframe = dataframe[:nb_days * 24 * 60]
        elif len(dataframe) < nb_days * 24 * 60:
            print(f"***Dataframe {name} is too short***")
            continue

        dataframe = drop_missing(dataframe)

        required_cols = ["Prx", "ICP", "HR", "ABP_HRVpsd_LF"]
        missing_cols = [col for col in required_cols if col not in dataframe.columns]

        if missing_cols:
            print(f"~~~Dataframe {name} misses columns: {missing_cols}~~~")
            continue
        else:
            dataframe = dataframe[required_cols]
            dataframe.rename(columns={"Prx": "PRX", "ABP_HRVpsd_LF": "LF"}, inplace=True)
            dataframe = fill_df_nans(dataframe)
            dataframe.to_pickle(save+f"\\{name}.pkl")
            print("!!!!!Saved", name)

