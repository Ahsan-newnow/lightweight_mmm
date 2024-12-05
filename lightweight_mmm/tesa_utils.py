import os
import pandas as pd
from functools import reduce

def get_exogenous_df(feature_store_origin):

    exogenous_csv_files = [i for i in os.listdir(os.path.join(feature_store_origin, 'exogenous')) if i.endswith('.csv')]
    dfs = []

    for _file in exogenous_csv_files:
        df = pd.read_csv(os.path.join(feature_store_origin, 'exogenous', _file))
        if _file in  ['competitor_rev.csv', 'competitor_market_share_pc.csv']:
            continue
        df = df[['year', 'week_number', _file.split('.')[0]]]
        dfs.append(df)

    
    merged_df = reduce(lambda left, right: pd.merge(left, right, on=['year', 'week_number'], how='outer'), dfs)

    return merged_df.iloc[:135]

def get_media_df(feature_store_origin, value='cost'):

    media_csv_files = [i for i in os.listdir(os.path.join(feature_store_origin, 'marketing')) if i.endswith('.csv')]
    dfs = []

    for _file in media_csv_files:
        if value == 'cost':
            df = pd.read_csv(os.path.join(feature_store_origin, 'marketing', _file))
            df = df[['year', 'week_number', _file.split('.')[0]]]
        else:
            df = pd.read_csv(os.path.join(feature_store_origin, 'marketing_impressions', _file))
            df = df[['year', 'week_number', 'impressions']]
        dfs.append(df)

    merged_df = reduce(lambda left, right: pd.merge(left, right, on=['year', 'week_number'], how='outer'), dfs)
    merged_df = merged_df[merged_df['year'].isin([2022, 2023, 2024])].iloc[:135]
    merged_df = merged_df.fillna(0)
    return merged_df

def get_revenue_df(feature_store_origin):

    media_csv_files = [i for i in os.listdir(os.path.join(feature_store_origin, 'revenue')) if i.endswith('.csv')]
    dfs = []

    for _file in media_csv_files:
        df = pd.read_csv(os.path.join(feature_store_origin, 'revenue', _file))
        df = df[['year', 'week_number', _file.split('.')[0]]]
        dfs.append(df)

    merged_df = reduce(lambda left, right: pd.merge(left, right, on=['year', 'week_number'], how='outer'), dfs)
    merged_df = merged_df[merged_df['year'].isin([2022, 2023, 2024])].iloc[:135]
    merged_df = merged_df.fillna(0)
    return merged_df
