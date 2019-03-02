import bs4
import urllib.request as url

movie_name = input("Enter movie name : ")
response = url.urlopen('https://www.imdb.com/find?ref_=nv_sr_fn&q='+movie_name)
data = bs4.BeautifulSoup(response, 'lxml')
td = data.find('td', class_='result_text')
href = td.find('a')['href']
# print(href)
newResponse = url.urlopen('https://www.imdb.com'+href)
newPage = bs4.BeautifulSoup(newResponse, 'lxml')
title = newPage.find('div', class_='title_wrapper')
title = title.text
title = title.replace('\n','')
title = title.split()
print(' '.join(title))

summary = newPage.find('div', class_='summary_text')
summary = summary.text.strip()
print(summary)