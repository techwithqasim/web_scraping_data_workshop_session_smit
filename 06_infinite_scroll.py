import pandas as pd
import requests

cookies = {
    'MicrosoftApplicationsTelemetryDeviceId': 'd5a14ea3-df87-4270-a765-3f4b04d7ac55',
    'MicrosoftApplicationsTelemetryFirstLaunchTime': '2025-01-11T16:08:33.755Z',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-SA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'MicrosoftApplicationsTelemetryDeviceId=d5a14ea3-df87-4270-a765-3f4b04d7ac55; MicrosoftApplicationsTelemetryFirstLaunchTime=2025-01-11T16:08:33.755Z',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://quotes.toscrape.com/scroll',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


page=1

complete_data = []

while True:
    params = {
        'page': page,
    }
    response = requests.get('https://quotes.toscrape.com/api/quotes', params=params, cookies=cookies, headers=headers)

    data_dict = response.json()
    quotes_data = data_dict['quotes']
    complete_data.extend(quotes_data)
    if not quotes_data:
        print('no data quotes found')
        break
    print(f'scraping page: {page}')
    page += 1

pd.DataFrame(complete_data).to_csv('api_data.csv')