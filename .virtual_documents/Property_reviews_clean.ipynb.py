import pandas as pd


property_reviews = pd.read_csv('split_property_reviews.csv')


property_reviews.info()


property_reviews.head()


property_reviews.first_review = pd.to_datetime(property_reviews.first_review)
property_reviews.last_review = pd.to_datetime(property_reviews.last_review)


i = {'t':0,'f':1}


property_reviews.instant_bookable = property_reviews.instant_bookable.map(i)
property_reviews.instant_bookable = property_reviews.instant_bookable.astype(float)


property_reviews.require_guest_profile_picture = property_reviews.require_guest_profile_picture.map(i)
property_reviews.require_guest_profile_picture = property_reviews.require_guest_profile_picture.astype(float)


property_reviews.require_guest_phone_verification = property_reviews.require_guest_phone_verification.map(i)
property_reviews.require_guest_phone_verification = property_reviews.require_guest_phone_verification.astype(float)


property_reviews.head()


property_reviews.info()


property_reviews.to_csv('1_property_reviews_clean.csv', index=False)



