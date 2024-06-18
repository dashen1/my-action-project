from bs4 import BeautifulSoup
import requests
import chardet

url = 'https://news.cctv.com/china/'
response = requests.get(url)

encoding_detected = chardet.detect(response.content)['encoding']

if response.status_code == 200:

    content = response.content.decode(encoding_detected, errors='replace')

    soup = BeautifulSoup(content, 'html.parser')
    
    a_tags = soup.find_all('a')

    with open('cctv.txt', 'w', encoding='utf-8') as f:
        for tag in a_tags:
            f.write(tag.text.strip() + '\n')
            
    print("爬取成功")
else:
    print(f"请求失败，状态码：{response.status_code}")