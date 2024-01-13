from bs4 import BeautifulSoup as bs
import requests

page = requests.get('https://math.hcmus.edu.vn/')
soup = bs(page.content, features='lxml') 

raw   = [_ for _ in soup.find_all(class_='mod-articles-category-title')]
news  = [_.text for _ in raw]
links = [_.attrs['href'] for _ in raw]
dates = [_.text.replace('\t', '').strip() 
         for _ in soup.find_all(class_='mod-articles-category-date')]

with open('README.md', 'w', encoding='utf-8') as f:
    for i, new in enumerate(news):
        f.write(f' - **{dates[i]}** - [{new}](https://math.hcmus.edu.vn{links[i]})\n')
