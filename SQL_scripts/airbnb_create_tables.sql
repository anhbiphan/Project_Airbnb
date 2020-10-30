CREATE TABLE `property_features` (
  `id` INT,
  `street` VARCHAR(50),
  `neighbourhood` VARCHAR(50),
  `city`VARCHAR(50),
  `state` VARCHAR(50),
  `zipcode` FLOAT,
  `country_code` VARCHAR(50),
  `country` VARCHAR(50),
  `latitude` FLOAT,
  `longitude` FLOAT,
  `is_location_exact` BOOL,
  `property_type` VARCHAR(50),
  `room_type` VARCHAR(50),
  `accommodates` INT,
  `bathroom` FLOAT,
  `bedrooms` FLOAT,
  `beds` FLOAT,
  `bed_type` VARCHAR(50),
  `amenities` VARCHAR(50),
  `square_feet` FLOAT
);

CREATE TABLE `listing_summary` (
  `id` INT,
  `name` VARCHAR(50),
  `host_id` INT,
  `host_name` VARCHAR(50),
  `neighbourhood` INT,
  `latitude` FLOAT,
  `longitude` FLOAT,
  `room_type` VARCHAR(50),
  `price` SMALLINT,
  `minimum_nights` TINYINT,
  `number_of_reviews` INT,
  `last_review` DATE,
  `reviews_per_month` FLOAT,
  `calculated_host_listings_count` INT,
  `availability_365` SMALLINT,
  PRIMARY KEY (`id`)
);

CREATE TABLE `host` (
  `host_id` INT,
  `host_name` VARCHAR(50),
  `host_since` DATE,
  `host_location` VARCHAR(50),
  `host_response_time` VARCHAR(50),
  `host_response_rate` FLOAT,
  `host_acceptance_rate` FLOAT,
  `host_is_superhost` BOOL,
  `host_neighbourhood` VARCHAR(50),
  `host_total_listings_count` SMALLINT,
  `host_verifications` VARCHAR(50),
  `host_has_profile_pic` BOOL,
  `host_identity_verified` BOOL,
  PRIMARY KEY (`host_id`)
);

CREATE TABLE `property_prices` (
  `id` INT,
  `price` INT,
  `weekly_price` INT,
  `monthly_price` INT,
  `security_deposit` INT,
  `cleaning_fee` INT,
  `guests_included` TINYINT,
  `extra_people` TINYINT,
  `minimum_nights` TINYINT,
  `maximum_nights` SMALLINT,
  `has_availability` BOOL,
  `availability_30` SMALLINT,
  `availability_60` SMALLINT,
  `availability_90` SMALLINT,
  `availability_365` SMALLINT,
  `calendar_last_scraped` DATE
  );

CREATE TABLE `property_reviews` (
  `id` INT,
  `number_of_reviews` INT,
  `first_review` DATE,
  `last_review` DATE,
  `review_scores_rating` FLOAT,
  `review_scores_accuracy` FLOAT,
  `review_scores_cleanliness` FLOAT,
  `review_scores_checkin` FLOAT,
  `review_scores_communication` FLOAT,
  `review_scores_location` FLOAT,
  `review_scores_value` FLOAT,
  `instant_bookable` BOOL,
  `cancellation_policy` VARCHAR(50),
  `require_guest_profile_picture` BOOL,
  `require_guest_phone_verification` BOOL,
  `calculated_host_listings_count` INT,
  `reviews_per_month` FLOAT
);

