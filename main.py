from bs4 import BeautifulSoup as bs
import requests
import re

page = requests.get('https://math.hcmus.edu.vn/')
soup = bs(page.content, features='lxml') 

raw   = [_ for _ in soup.find_all(class_='mod-articles-category-title')]
news  = [_.text.strip() for _ in raw]
links = [_.attrs['href'] for _ in raw]
dates = [_.text.replace('\t', '').strip() 
         for _ in soup.find_all(class_='mod-articles-category-date')]

with open('README.md', 'r', encoding='utf-8') as f:
    old_data = f.read()
    old_link = re.findall(r'http.*\w', old_data)

with open('README.md', 'w', encoding='utf-8') as f:
    for i, title in enumerate(news):
        link = f'https://math.hcmus.edu.vn{links[i]}'
        if link not in old_link:
            f.write(f' - **{dates[i]}** - [***{title}***]({link})\n')
        else:
            f.write(f' - **{dates[i]}** - [{title}]({link})\n')
