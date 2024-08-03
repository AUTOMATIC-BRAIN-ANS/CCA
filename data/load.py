from data.preprocessing import *
import os
import pandas as pd

load = "C:\\USK_Wieloparametrowe_onlyTBI_and_SAH_with_ICP_SONATA_HEATMAPS\\ANALIZA_SZEREGOW_CZASOWYCH\\CSV_with_results"
save = "D:\\MN\\preprocessed"

dataset = load_files(load)
print_nb_cols(dataset)


nb_days = 1
for file in os.listdir(load):
    if file.endswith(".csv"):
        name = file[:-4]
        dataframe = pd.read_csv(os.path.join(load, file), error_bad_lines=False, sep=';', encoding='latin1',
                                decimal=',')
        dataframe = drop_missing(dataframe)
        dataframe = fill_with_mean(dataframe)
        dataframe["Time"] = dataframe["DateTime"].apply(icmp_dateformat_to_datetime)

        if len(dataframe) > nb_days*24*60:
            dataframe = dataframe[:nb_days*24*60]
        elif len(dataframe) < nb_days*24*60:
            print(f"***Dataframe {name} is too short***")
            continue

        # dataframe.to_pickle(save+f"\\{name}.pkl")
