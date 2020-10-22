import pandas as pd
import numpy as np


listing_summary = pd.read_csv('listings_summary.csv')


listing_summary.head()


listing.columns


calendar = pd.read_csv('calendar.csv')


calendar.head()


listings = pd.read_csv('listings.csv')


listings.columns


listings.host_verifications[0]


listings = listings.drop(columns= ['listing_url', 'scrape_id', 'last_scraped', 'name', 'summary',
       'space', 'description', 'experiences_offered', 'neighborhood_overview',
       'notes', 'transit', 'thumbnail_url', 'medium_url', 'picture_url',
       'xl_picture_url', 'host_url','host_about', 'host_thumbnail_url', 'host_picture_url', 'host_listings_count', 'neighbourhood_cleansed',
       'neighbourhood_group_cleansed',  'market',
       'smart_location', 'calendar_updated', 'license', 'jurisdiction_names'])


listings.to_csv("listings_cleaned.csv", index=False)


listings.fillna('n/a')


listings.host_since = pd.to_datetime(listings.host_since)


listings.host_since


listings.host_response_rate.astype(int)



