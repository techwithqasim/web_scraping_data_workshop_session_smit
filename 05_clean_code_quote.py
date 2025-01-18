import pandas as pd
import requests
from bs4 import BeautifulSoup

base_url = 'https://quotes.toscrape.com/'

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

next_page_path = ''

complete_data_extracted = []

while True:
    url = base_url + next_page_path
    response = requests.get(url=url)
    markup = response.text
    soup = BeautifulSoup(markup, 'html.parser')
    
    # creating the object
    quotes_obj = soup.select('div.quote')
    quotes_data = extracting_all_elements(quotes_obj)
    
    complete_data_extracted.extend(quotes_data)
    print(len(complete_data_extracted))
    
    try:
        next_page_path = soup.select_one('li.next a').attrs['href']
        print(next_page_path)
    except:
        print('no next page breaking the loop')
        break;

pd.DataFrame(complete_data_extracted).to_csv('complete_data.csv', index=False)