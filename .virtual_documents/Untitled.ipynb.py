import pandas as pd


df = pd.read_csv('2_host.csv')


doop = df[df['host_id'].duplicated()]


doop.head()


doop.host_id.value_counts()


df.drop_duplicates(subset=['host_id'], inplace=True)


df.info()


df.to_csv('2_host_unique.csv', index= False)
