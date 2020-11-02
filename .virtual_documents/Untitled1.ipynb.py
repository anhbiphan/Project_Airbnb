


import pandas as pd





property_features.is_location_exact = property_features.is_location_exact.map(i)
property_features.is_location_exact = property_features.is_location_exact.astype(bool)


property_features = pd.concat([id,property_features], axis=1)

































