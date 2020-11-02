import pandas as pd


df = pd.read_csv('split_property_features.csv')


df.head()


df.info()


# t = 0 , f = 1
i = {'t':0, 'f':1}


# converting column into boolean
df.is_location_exact = df.is_location_exact.map(i)
df.is_location_exact = df.is_location_exact.astype(float)


# conversion worked
df.is_location_exact


df.to_csv('1_property_features_clean.csv', index=False)



