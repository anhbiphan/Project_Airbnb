import pandas as pd


df = pd.read_csv('2_host.csv')


df.info()


doop = df[df['host_id'].duplicated()]


df.host_since = pd.to_datetime(df.host_since)


doop.host_has_profile_pic.value_counts()


doop.host_id.value_counts()


df.drop_duplicates(subset=['host_id'], inplace=True)


df.info()


df[['host_is_superhost', 'host_has_profile_pic', 'host_identity_verified']]


for i in df[]


df.to_csv('2_host_unique.csv', index= False)



