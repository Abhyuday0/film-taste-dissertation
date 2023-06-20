from bs4 import BeautifulSoup
import requests

url = "https://api.themoviedb.org/3/discover/movie?api_key=240e5e05bbdeb94190adc4a29af81937&sort_by=release_date.asc&include_adult=false&include_video=false&primary_release_year=2012&vote_count.gte=1000&with_watch_monetization_types=flatrate"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

print(soup.prettify)


