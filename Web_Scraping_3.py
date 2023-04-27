from bs4 import BeautifulSoup
import lxml
import requests

year_requested = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD:")
url = "https://www.billboard.com/charts/hot-100/" + year_requested
response = requests.get(url)

soup = BeautifulSoup(response.text, lxml)

title = soup.find_all(name ="h3", class_ ="a-no-trucate")
top_100 = [i.getText().strip() for i in title]

print(top_100)


