import requests

url = 'https://book.douban.com/tag/%E9%98%BF%E5%8A%A0%E8%8E%8E%C2%B7%E5%85%8B%E9%87%8C%E6%96%AF%E8%92%82'
res = requests.get(url)
print(res.content.decode())





