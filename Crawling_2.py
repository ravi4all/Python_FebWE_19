import bs4
import urllib.request as url

web = url.urlopen('https://www.amazon.in/LAYASA-Running-Sports-Shoes-Black/dp/B07MGLJWSK/ref=sr_1_1?s=amazon-devices&ie=UTF8&qid=1550292258&sr=8-1&keywords=shoes')

page = bs4.BeautifulSoup(web, 'lxml')
data = page.find('span', id='productTitle')
print(data.text.strip())

price = page.find('span', id='priceblock_ourprice')
print(price.text.strip())

details = page.find('div', id='feature-bullets')
# print(details.text.strip())
text = details.text.strip()
text = text.replace("  ", '')
text = text.replace('\n','')
text = text.replace('\t','')
print(text)