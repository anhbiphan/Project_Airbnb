import pandas as pd


listings = pd.read_csv('airbnb_dataset/listings.csv')


listings.columns


listings.head()


listings = listings.drop(columns= ['listing_url', 'scrape_id', 'last_scraped', 'name', 'summary',
       'space', 'description', 'experiences_offered', 'neighborhood_overview',
       'notes', 'transit', 'thumbnail_url', 'medium_url', 'picture_url',
       'xl_picture_url', 'host_url','host_about', 'host_thumbnail_url', 'host_picture_url', 'host_listings_count', 'neighbourhood_cleansed',
       'neighbourhood_group_cleansed',  'market',
       'smart_location', 'calendar_updated', 'license', 'jurisdiction_names', 'requires_license'])


listings.columns


listings.info()


# data error
# this proparty is in Spain, we need to remove this out of the data
listings.loc[listings['city'] == 'Cangas de Onís']


# remove data error
# index has a proparty outside of Austin,TX
listings.drop([5832], inplace=True)


# check if Spain property has been dropped
# it has been dropped
listings.loc[5831:].city


# now we need to reset the index
listings.reset_index(drop=True, inplace=True)


# our index is reset!
listings.loc[5831:].city


# creating a id column dataframe to concatenate to other tables
id = listings.iloc[:,:1]


host_cols = listings.columns[:14].tolist()
host = listings.loc[:, (host_cols)]

host.to_csv('split_host.csv', index=False)


property_features = listings.iloc[:, 14:33]


property_features = pd.concat([id,property_features], axis=1)


property_features.to_csv("split_property_features.csv", index=False)


property_price = listings.iloc[:, 33:48]


property_price = pd.concat([id, property_price], axis=1)


property_price.to_csv('split_property_price.csv', index=False)


property_reviews = listings.iloc[:, 48:]


property_reviews = pd.concat([id, property_reviews], axis=1)


property_reviews.to_csv('split_property_reviews.csv', index=False)
