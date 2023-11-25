import pandas as pd

full_df = pd.read_pickle("./data/transactions_usa.pkl")

# Split the data into both categories
df_yes = full_df.loc[full_df['Is Fraud?'] == "Yes"]  # ~     40_000 records
df_no = full_df.loc[full_df['Is Fraud?'] == "No"]    # ~ 20_000_000 records

# Take a random sample of non-fraudulent transactions
df_no = df_no.sample(60_000)

# Create a smaller dataset with a more even distribution of fraud vs non-fraud
df_final = pd.concat((df_yes, df_no))

df_final.to_csv('./data/sample_usa.csv')
