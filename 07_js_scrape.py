import pandas as pd
import requests
import json
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/js/page/2/"

soup = BeautifulSoup(requests.get(url).text, 'html.parser')

for script in soup.select('script'):
    if 'data' in script.text:
        data_script = script
        
        filtered_string = data_script.text.split('for (var')[0].split('data =')[1].replace(';','')
        data = json.loads(filtered_string)
        print(data)
        