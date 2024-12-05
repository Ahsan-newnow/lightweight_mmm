feature_store_origin = "/Users/ahasan/Library/CloudStorage/OneDrive-SharedLibraries-NewNowGroupGmbH/Tesa Projects - Documents/03_Data/00 Data Storage/14_feature_storage/max_aggregation"

revenue_column = 'full_rev' # options: 'ecom_rev', 'full_rev', 'full_rev'

# pass a valid list to filter out the media columns

# all columns: ['year', 'week_number', 'owned_social_cost', 'paid_social_cost',
#       'programmatic_video_cost', 'paid_search_cost',
#       'programmatic_display_cost', 'tv_cost_lag8']

media_columns = [] 

# pass a valid list to filter out the exogenous columns

# all columns: ['distribution', 'economic_activity',
#       'precipitation', 'market_size', 'sunshine', 'smoothed_price_change',
#       'visibility', 'temperature', 'competitor_ad_spending', 'holiday_flag']
exogenous_columns = ['distribution', 'economic_activity', 'temperature', 'holiday_flag', 'smoothed_price_change']