import QC
import pandas as pd
pd.options.display.max_rows = 10


def process_df(df, df_info):
    df_info = df_info.set_index('info')
    try:
        lat, lon = float(df_info.loc['Download Location (lat/long)', 'lat']), float(
            df_info.loc['Download Location (lat/long)', 'lon'])
    except:
        print('Location is not given')
        lat, lon = 0, 0
    df['datetime'] = pd.to_datetime(df.Date + ' ' + df.Time, format='%d/%m/%Y %H:%M:%S')
    df.rename(columns={'Temperature C': 'temperature', 'Depth Decibar': 'pressure', 'Depth M': 'pressure'},
              inplace=True)
    df['temperature'] = pd.to_numeric(df['temperature'])
    df['pressure'] = pd.to_numeric(df['pressure'])
    df['temperature'] = df.apply(lambda x: round(x['temperature'], 4), axis=1)
    df['pressure'] = df.apply(lambda x: round(x['pressure'], 3), axis=1)
    df = df[['datetime', 'temperature', 'pressure']]
    df.loc[:, 'latitude'] = lat
    df.loc[:, 'longitude'] = lon
    df.rename(columns={'datetime': 'DATETIME', 'temperature': 'TEMPERATURE', 'pressure': 'PRESSURE',
                       'latitude': 'LATITUDE', 'longitude': 'LONGITUDE'}, inplace=True)
    df = QC.QC(df).df
    df.rename(columns={'DATETIME': 'datetime', 'TEMPERATURE': 'temperature', 'PRESSURE': 'pressure',
                       'LATITUDE': 'latitude', 'LONGITUDE': 'longitude'}, inplace=True)
    return df
