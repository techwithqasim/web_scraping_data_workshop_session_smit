from bs4 import BeautifulSoup

markup = open('index.html', 'r').read()

soup = BeautifulSoup(markup=markup, features='html.parser')

print(soup.prettify())

parent_section = soup.select_one('section#section2')
parent_section.select_one('table')

# len(soup.select('section'))

soup.find_all('section', id='')