import pandas as pd

#  function to transform the dataframe by adding columns for Market Capitalization in GBP, EUR, and INR,
#  rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
def transform(df, csv_path):
    exchange_rate_df = pd.read_csv(csv_path, index_col='Currency')
    euro_rate = exchange_rate_df.loc['EUR','Rate']
    gbp_rate = exchange_rate_df.loc['GBP','Rate']
    inr_rate = exchange_rate_df.loc['BDT','Rate']
    dataframe_euro = (df[['MC_USD_Billion']] * euro_rate).rename(columns={'MC_USD_Billion':'MC_EURO_Billion'})
    dataframe_gbp = pd.DataFrame({'MC_GBP_Billion': df['MC_USD_Billion'] * gbp_rate})
    dataframe_inr = (df[['MC_USD_Billion']] * inr_rate).rename(columns={'MC_USD_Billion': 'MC_BDT_Billion'})
    
    dataframe2 = pd.concat([df, dataframe_euro, dataframe_gbp, dataframe_inr], axis=1).round(2)
    return dataframe2

