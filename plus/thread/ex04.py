# Thread 클래스 상속 방법
# run() 메서드 구현

import threading, requests, time

class HtmlGetter(threading.Thread):
    def __init__(self, url):
        # threading.Thread.__init__(self) # 다중 상속일 때는 이렇게 넣어주어야 함
        super().__init__()
        self.url = url

    def run(self): # 오버라이드
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), resp.text)

t = HtmlGetter('https://google.com')
t.start()

print('### End ###')