import pandas as pd
import requests
from bs4 import BeautifulSoup

base_url = 'https://quotes.toscrape.com/'

response = requests.get(url=base_url)

markup = response.text

soup = BeautifulSoup(markup, 'html.parser')

quotes_obj = soup.select('div.quote')
# print(len(quotes_obj))

quote_text = quotes_obj[0].select_one('span.text').text.strip()

quote_author = quotes_obj[0].select_one('span small.author').text

single_tag = quotes_obj[0].select('div.tags a')[0].text


# creating as a whole using for loop

# main_data_dict = {
#     "author_name":[],
#     "author_quote":[],
#     "tags": []
# }

def extracting_all_elements(quotes_obj):
    main_data_list = []

    for obj in quotes_obj:
        temp_dict = {}
    # text
        quote_text = obj.select_one('span.text').text.strip()
    # author
        quote_author = obj.select_one('span small.author').text
    # tags as string 
        tags_list = ', '.join([tags.text for tags in obj.select('div.tags a')])
    
    # appending all the data
        temp_dict['quote_text'] = quote_text
        temp_dict['quote_author'] = quote_author
        temp_dict['tags'] = tags_list
    
        main_data_list.append(temp_dict)
        # print(temp_dict)
    return main_data_list

extracting_all_elements(quotes_obj)

next_page_path = soup.select_one('li.next a').attrs['href']