import bs4
import urllib.request as url

web = url.urlopen('https://www.indeed.co.in/jobs?q=java&l=New+Delhi%2C+Delhi')
# print(web)
# lxml - library xml
page = bs4.BeautifulSoup(web, 'lxml')
# links = page.find_all('a', class_='jobtitle')
# print(link)
# for link in links:
#     print(link.text)

# link = page.find('a', id='sja1')
# print(link)

jobs = page.find_all('div', class_='jobsearch-SerpJobCard')
for job in jobs:
    print(job.text)