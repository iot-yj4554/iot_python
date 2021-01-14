# 인터넷으로 파일 다운로드 받기
# requests 모듈
# ger(url)
# - 지정한 url을 요청하고 웹 서버로부터 받은 응답(response)을 리턴
# response
# - text : 웹 서버가 리턴한 텍스트 저장
# - content : 웹 서버가 리턴한 실제 데이터 저장

from threading import Thread
import requests
import time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), resp.text)

t1 = Thread(target=getHtml, args=('https://naver.com',)) 
# args는 인자가 하나여도 받드시 튜플로 전달해야 하기 때문에 마지막에 ,를 넣어주어야 함
t1.start()


# <만일 2개의 작업아 있을 때>
# getHtml('https://www.naver.com') # 1초
# getHtml('https://www.daum.net') # 2초

# 1) 스레드를 안 쓰는 경우
# -> 총 작업 시간 3초 걸림
# 2) 스레드를 쓰는 경우
# -> 총 작업 시간 2초 걸림

