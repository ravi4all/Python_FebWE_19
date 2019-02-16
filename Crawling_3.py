import bs4
import urllib.request as url

userInput = input("Enter movie/actor/tv series name : ")
web = url.urlopen('https://www.imdb.com/find?ref_=nv_sr_fn&q='+userInput)

page = bs4.BeautifulSoup(web, 'lxml')
td = page.find('td', class_='result_text')
a_tag = td.find('a')
href = a_tag['href']
# print(href)
newUrl = 'https://www.imdb.com'+href
web_2 = url.urlopen(newUrl)
page_2 = bs4.BeautifulSoup(web_2, 'lxml')

title = page_2.find('div', class_='title_wrapper')
# print(title.text.replace('  ',''))
title = title.text.replace('  ','')
title = title.replace('\n','')
print(title)

summary = page_2.find('div', class_='summary_text')
print(summary.text.strip())
