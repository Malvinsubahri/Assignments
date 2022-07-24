select b.ad_type,
b.advertiser_name,
b.date_range_start,
b.date_range_end,
b.num_of_days,
c.country_subdivision_primary,
c.spend_usd
from `bigquery-public-data.google_political_ads.advertiser_declared_stats` a
join `bigquery-public-data.google_political_ads.creative_stats` b on a.advertiser_id = b.advertiser_id
join `bigquery-public-data.google_political_ads.advertiser_geo_spend` c on b.advertiser_id = c.advertiser_id
where c.country_subdivision_primary is not null
and c.country = 'US'
order by date_range_start, num_of_days asc;