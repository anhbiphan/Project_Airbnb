import pandas as pd


host = pd.read_csv('split_host.csv')


host.head()


host.info()


# converting host_since to datetime
host.host_since = pd.to_datetime(host.host_since)

# str split host_reponse_time, grabbing only numeric value
host.host_response_rate = host.host_response_rate.str.split('get_ipython().run_line_magic("').str[0]", "")

# converting numeric value into float
host.host_response_rate = host['host_response_rate'].astype(float)
# converting float to percent
host.host_response_rate = host.host_response_rate/100


# split str to grab numeric value
host.host_acceptance_rate = host.host_acceptance_rate.str.split('get_ipython().run_line_magic("').str[0]", "")

# converting datatype to float
host.host_acceptance_rate = host.host_acceptance_rate.astype(float)

# converting to percentage
host.host_acceptance_rate = host.host_acceptance_rate/100


# boolean datatype
host.host_is_superhost


i = {'t': 0, 'f': 1}


# converting datatype to boolean
host.host_is_superhost = host.host_is_superhost.map(i)

host.host_has_profile_pic = host.host_has_profile_pic.map(i)

host.host_identity_verified = host.host_identity_verified.map(i)


host.host_is_superhost


# checking datatype
host.info()


# There are duplicates for sure
host['host_id'].duplicated()


# Confirmation that some host have mulitple connections to properties
# host_id 4641823 has 127 properties on Airbnb listings
host.host_id.value_counts()


host.drop_duplicates(subset=['host_id'], inplace=True)


# drop_duplicates has removed all duplicates, keeping only unique host_ids (aka the host)
host.host_id.value_counts()


# reset the index
host.reset_index(drop=True, inplace=True)


# count 4632 unique host_ids, AWESOME!
host.info()


host.to_csv("1_host_unique.csv", index=False)



