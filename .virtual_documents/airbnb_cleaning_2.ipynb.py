import pandas as pd


listings = pd.read_csv('listings.csv')


listings.columns


listings.head()


listings = listings.drop(columns= ['listing_url', 'scrape_id', 'last_scraped', 'name', 'summary',
       'space', 'description', 'experiences_offered', 'neighborhood_overview',
       'notes', 'transit', 'thumbnail_url', 'medium_url', 'picture_url',
       'xl_picture_url', 'host_url','host_about', 'host_thumbnail_url', 'host_picture_url', 'host_listings_count', 'neighbourhood_cleansed',
       'neighbourhood_group_cleansed',  'market',
       'smart_location', 'calendar_updated', 'license', 'jurisdiction_names', 'requires_license'])


listings.drop([5832], inplace=True)
listings.reset_index(drop=True, inplace=True)


listings.info()


# creating a id column dataframe to concatinate to other tables
id = listings.iloc[:,:1]


host_cols = listings.columns[:14].tolist()
host = listings.loc[:, (host_cols)]

host.to_csv("host.csv", index=False)


host.head()


host.info()


# converting to datetime
host.host_since = pd.to_datetime(host.host_since)


host.host_response_rate = host.host_response_rate.str.split('get_ipython().run_line_magic("').str[0]", "")


# converting % into float
host.host_response_rate = host['host_response_rate'].astype(float)


host.host_response_rate = host.host_response_rate/100


# split str to grab numeric value
host.host_acceptance_rate = host.host_acceptance_rate.str.split('get_ipython().run_line_magic("').str[0]", "")


# converting datatype to float
host.host_acceptance_rate = host.host_acceptance_rate.astype(float)


# converting to percentage
host.host_acceptance_rate = host.host_acceptance_rate/100


# boolean datatype
host.host_is_superhost


i = {'t': True, 'f': False}


# converting datatype to boolean
host.host_is_superhost = host.host_is_superhost.map(i)

host.host_is_superhost = host.host_is_superhost.astype(bool)


host.host_has_profile_pic = host.host_has_profile_pic.map(i)
host.host_has_profile_pic = host.host_has_profile_pic.astype(bool)


host.host_identity_verified = host.host_identity_verified.map(i)
host.host_identity_verified = host.host_identity_verified.astype(bool)


host.head()


host.info()


host.to_csv("2_host.csv", index=False)


property_features = listings.iloc[:, 14:33]


property_features.info()


property_features.head()


property_features.is_location_exact = property_features.is_location_exact.map(i)
property_features.is_location_exact = property_features.is_location_exact.astype(bool)


property_features = pd.concat([id,property_features], axis=1)


property_features.to_csv("2_property_features.csv", index=False)


property_price = listings.iloc[:, 33:48]


property_price = pd.concat([id, property_price], axis=1)


property_price.head()


property_price.info()


# # split the $ symbol
# # replace any commas
# # convert into float
property_price.price = property_price.price.str.split('$').str[1]
property_price.price = property_price.price.replace(',', '', regex=True)
property_price.price = property_price.price.astype(float)


property_price.weekly_price = property_price.weekly_price.str.split('$').str[1]
property_price.weekly_price = property_price.weekly_price.replace(',', '', regex=True)
property_price.weekly_price = property_price.weekly_price.astype(float)


property_price.monthly_price = property_price.monthly_price.str.split('$').str[1]
property_price.monthly_price = property_price.monthly_price.replace(',', '', regex=True)
property_price.monthly_price = property_price.monthly_price.astype(float)


property_price.security_deposit = property_price.security_deposit.str.split('$').str[1]
property_price.security_deposit = property_price.security_deposit.replace(',', '', regex=True)
property_price.security_deposit = property_price.security_deposit.astype(float)


property_price.cleaning_fee = property_price.cleaning_fee.str.split('$').str[1]
property_price.cleaning_fee = property_price.cleaning_fee.replace(',', '', regex=True)
property_price.cleaning_fee = property_price.cleaning_fee.astype(float)


property_price.extra_people = property_price.extra_people.str.split('$').str[1]
property_price.extra_people = property_price.extra_people.astype(float)


# applying boolean datatype
property_price.has_availability = property_price.has_availability.map(i)
property_price.has_availability = property_price.has_availability.astype(bool)


# converting to datetime
property_price.calendar_last_scraped = pd.to_datetime(property_price.calendar_last_scraped)


property_price.info()


property_price.to_csv('2_property_price.csv', index=False)


property_reviews = listings.iloc[:, 48:]


property_reviews = pd.concat([id, property_reviews], axis=1)


property_reviews.head()


property_reviews.info()


property_reviews.first_review = pd.to_datetime(property_reviews.first_review)
property_reviews.last_review = pd.to_datetime(property_reviews.last_review)


property_reviews.instant_bookable = property_reviews.instant_bookable.map(i)
property_reviews.instant_bookable = property_reviews.instant_bookable.astype(bool)


property_reviews.require_guest_profile_picture = property_reviews.require_guest_profile_picture.map(i)
property_reviews.require_guest_profile_picture = property_reviews.require_guest_profile_picture.astype(bool)


property_reviews.require_guest_phone_verification = property_reviews.require_guest_phone_verification.map(i)
property_reviews.require_guest_phone_verification = property_reviews.require_guest_phone_verification.astype(bool)


property_reviews.head()


property_reviews.info()


property_reviews.to_csv('2_property_reviews.csv', index=False)



