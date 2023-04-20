from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests

page = requests.get('https://math.hcmus.edu.vn/')
soup = bs(page.content, features='lxml') 

raw = [_ for _ in soup.find_all(class_='mod-articles-category-title')]
news = [_.text for _ in raw]
links = [_.attrs['href'] for _ in raw]
dates = [_.text.replace('\t', '').strip() 
         for _ in soup.find_all(class_='mod-articles-category-date')]
descriptions = [_.text.replace('\r', '').replace('\t', '').replace('\n', '')
                for _ in soup.find_all(class_='mod-articles-category-introtext')]

file = Path('README.md').rename(Path('README.md').with_suffix('.txt'))
with open(file, 'w', encoding='utf-8') as f:
    for i, new in enumerate(news):
        f.write(f' - [{new}](https://math.hcmus.edu.vn/{links[i]})(**{dates[i]}**): {descriptions[i]}\n')
    
f.close()

readme = Path('README.txt')
readme.rename(readme.with_suffix('.md'))
