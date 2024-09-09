import numpy as np
from scipy.interpolate import interp1d
import pandas as pd
import os
import xlrd
import datetime


def load_files(folder: str):
    ds = {}
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            ds[file[:-4]] = pd.read_csv(os.path.join(folder, file), error_bad_lines=False, sep=';', encoding='latin1',
                                        decimal=',')
    return ds


def load_pickled(folder: str):
    ds = {}
    for file in os.listdir(folder):
        if file.endswith(".pkl"):
            ds[file[:-4]] = pd.read_pickle(os.path.join(folder, file))
    return ds


def get_missing_col(dataframe: pd.DataFrame):
    missing = dataframe.isnull().sum()
    everything = dataframe.shape[0]
    percent = 100 * missing / everything
    return percent


def get_missing_all(dataframe: pd.DataFrame):
    missing = dataframe.isnull().sum().sum()
    everything = dataframe.size
    percent = 100 * missing / everything
    return percent


def print_missing_table(dataset: dict):
    missing = []
    for name, df in dataset.items():
        missing.append({'name': name, 'percent': get_missing_all(df)})
    nan_df = pd.DataFrame(missing)
    with pd.option_context('display.max_rows', None):
        print(nan_df)


def missing_over_threshold(dataset: dict, threshold: float = 10.0):
    cols = []
    for name, df in dataset.items():
        percent = get_missing_col(df)
        colnames = percent[percent > threshold]
        cols.append({'name': name, 'colnames': colnames.index.tolist()})
    col_df = pd.DataFrame(cols)
    with pd.option_context('display.max_rows', None):
        print(col_df)


def drop_missing(dataframe, threshold=80.0):
    missing = get_missing_col(dataframe)
    to_drop = missing[missing > threshold].index
    result = dataframe.drop(columns=to_drop)
    return result


def fill_with_mean(dataframe):
    for col in dataframe.columns[dataframe.isnull().any(axis=0)]:
        dataframe[col].fillna(dataframe[col].mean, inplace=True)
    return dataframe


def icmp_dateformat_to_datetime(icmp_time_mark):
    datetime_date = xlrd.xldate_as_datetime(icmp_time_mark, 0)
    datetime_date = datetime_date + datetime.timedelta(hours=1)
    return datetime_date


def print_nb_cols(dataset):
    for name, dataframe in dataset.items():
        print(f"{name} has {len(dataframe.columns)} columns: {dataframe.columns}")


def get_n_days(dataframe, n=1):
    return dataframe.iloc[:n*24*60]


def fill_nans(signal, kind='linear'):
    idx = np.arange(signal.shape[0])
    not_nan, = np.where(np.isfinite(signal))
    f = interp1d(not_nan, signal[not_nan], bounds_error=False, copy=False, fill_value="extrapolate", kind=kind)
    return f(idx)


def fill_df_nans(dataframe, kind='linear'):
    for col in dataframe.columns:
        if dataframe[col].isnull().any():
            dataframe[col] = fill_nans(dataframe[col].values, kind=kind)
    return dataframe

