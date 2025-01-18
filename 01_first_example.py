html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story1">...</p>
"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
print(type(soup))

# gives all the items of the tag
soup.select('a')

# selecting element using class
soup.select('a.sister')

# selecting element using id
soup.select('a#link1')

# selecting the parent tag
parent_obj = soup.select_one('p.story')

for anchor in parent_obj.select('a'):
    # print(anchor)
    # print('text')
    # print(anchor.text)
    print(anchor.attrs['href'])


with open('index.html', 'r') as f:
    html_markup = f.read()

soup = BeautifulSoup(markup=html_markup, features='html.parser')
print(soup.prettify())

soup.select("section#section1")

soup.select("section.class1")

soup.find_all("section", attrs= {'class':'class1'})

soup.find_all("section", attrs= {'some_identifier':'custom_id1'})

soup.select('p')