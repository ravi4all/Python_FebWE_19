import bs4
import urllib.request as url

# Step - 1 - Request the Url of the page from where you want to fetch data
response = url.urlopen('https://www.imdb.com/title/tt2631186/?ref_=nv_sr_1')
# It will return httpresponse

# Step - 2 - Pass that httpresponse to bs4 and it will return the
# source code of that page
data = bs4.BeautifulSoup(response, 'lxml')
# Step 3 - Using bs4 methods like find, find_all, find_children we can fetch any data whatever we want
# If we use find() then it will return a string
# if we use findall() then it will return a list
title = data.find('div', class_='title_wrapper')
# print(title)
# we want text instead of html code
# print(title.text)
# we got text in unstructured format
# we need to format or struct the data
title = title.text
title = title.replace('\n','')
# print(title)
# title = title.replace('  ','')
# print(title)
title = title.split()
print(' '.join(title))