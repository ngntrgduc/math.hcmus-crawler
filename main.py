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

data = {}

with open('README.md', 'r', encoding='utf-8') as f:
    old_data = f.read()
    old_date = [line[5:15] for line in old_data.splitlines()]
    old_link = re.findall(r'http.*\)', old_data)
    old_link = [link[:-1] for link in old_link]
    
    for link, date in zip(old_link, old_date):
        data[link] = date

with open('README.md', 'w', encoding='utf-8') as f:
    for i, title in enumerate(news):
        link = f'https://math.hcmus.edu.vn{links[i]}'
        if link not in old_link:
            if dates[i] != data[link]:
                f.write(f' - **{dates[i]}** - [***{title}***]({link})\n')
            else:
                f.write(f' - **{dates[i]}** - [{title}]({link})\n')   
        else:
            f.write(f' - **{dates[i]}** - [{title}]({link})\n')
