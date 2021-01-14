# 인터넷으로 파일 다운로드 받기 
# 이미지 파일 저장하기

from threading import Thread
import requests

def getHtml(url):
    resp = requests.get(url)
    with open('./image.jpeg', 'wb') as f:
        f.write(resp.content)
    print('Done')

url = 'https://www.memphisveterinaryspecialists.com/files/best-breeds-of-house-cats-memphis-vet-1-1.jpeg'

t1 = Thread(target=getHtml, args=(url,))
t1.start()