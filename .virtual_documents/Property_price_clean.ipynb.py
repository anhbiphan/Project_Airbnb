


import pandas as pd


df = pd.read_csv('split_property_price.csv')


df.head()


df.info()


# # split the $ symbol
# # replace any commas
# # convert into float
df.price = df.price.str.split('$').str[1]
df.price = df.price.replace(',', '', regex=True)
df.price = df.price.astype(float)


df.weekly_price = df.weekly_price.str.split('$').str[1]
df.weekly_price = df.weekly_price.replace(',', '', regex=True)
df.weekly_price = df.weekly_price.astype(float)


df.monthly_price = df.monthly_price.str.split('$').str[1]
df.monthly_price = df.monthly_price.replace(',', '', regex=True)
df.monthly_price = df.monthly_price.astype(float)


df.security_deposit = df.security_deposit.str.split('$').str[1]
df.security_deposit = df.security_deposit.replace(',', '', regex=True)
df.security_deposit = df.security_deposit.astype(float)


df.cleaning_fee = df.cleaning_fee.str.split('$').str[1]
df.cleaning_fee = df.cleaning_fee.replace(',', '', regex=True)
df.cleaning_fee = df.cleaning_fee.astype(float)


df.extra_people = df.extra_people.str.split('$').str[1]
df.extra_people = df.extra_people.astype(float)


i = {'t':0, 'f':1}


# applying boolean datatype
df.has_availability = df.has_availability.map(i)
df.has_availability = df.has_availability.astype(float)


# converting to datetime
df.calendar_last_scraped = pd.to_datetime(df.calendar_last_scraped)


df.info()


df.to_csv('1_property_price_clean.csv', index=False)



