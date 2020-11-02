import pandas as pd


calendar = pd.read_csv('airbnb_dataset/calendar.csv')


calendar.head()


calendar.info()


# converting date to datetime datatype
calendar.date = pd.to_datetime(calendar.date)


calendar.available


i = {'t': True, 'f': False}


calendar.available = calendar.available.map(i)


calendar.available.head()





# save cleaned calendar dataframe
# calendar.to_csv("1_calendar_clean.csv", index=False)
