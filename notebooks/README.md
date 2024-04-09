## EDA Analysis in Google Collab
I used Google Collab to perform the EDA analysis

# Some of the functions available in the notebooks
load_data(): Loads the data files into Pandas DataFrames.
merge_datasets(data, domains_location, traffic_data): Merges the three datasets based on common keys.
top_10_articles_count(merged_data): Identifies the top 10 websites with the largest count of news articles.
bottom_10_articles_count(merged_data): Identifies the bottom 10 websites with the largest count of news articles
countries_media_orgs(domains_location): Counts the number of news media organizations in each country.