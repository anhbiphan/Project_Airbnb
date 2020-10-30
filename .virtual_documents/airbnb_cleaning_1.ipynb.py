import pandas as pd
import numpy as np


listing_summary = pd.read_csv('airbnb_dataset/listings_summary.csv')


listing_summary.head()


listing_summary.columns


listing_summary = listing_summary.drop(columns=['neighbourhood_group'])


listing_summary.drop([5832], inplace=True)
listing_summary.reset_index(drop=True, inplace=True)


listing_summary.info()


# converting to datetime
listing_summary.last_review = pd.to_datetime(listing_summary.last_review)


listing_summary.last_review


listing_summary.info()


# save cleaned dataframe
# listing_summary.to_csv("1_listings_sum_clean.csv", index=False)


calendar = pd.read_csv('airbnb_dataset/calendar.csv')


calendar.head()


calendar.info()


# converting date to datetime datatype
calendar.date = pd.to_datetime(calendar.date)


# converting t/f to boolean datatype
calendar.available


i = {'t': True, 'f': False}


calendar.available = calendar.available.map(i)


calendar.available.head()


len(listing_summary.host_id.unique().tolist())


# save cleaned calendar dataframe
# calendar.to_csv("1_calendar_clean.csv", index=False)



