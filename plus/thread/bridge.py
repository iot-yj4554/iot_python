from threading import Lock

class Bridge:
    def __init__(self):
        self.counter = 0
        self.name = '아무개'
        self.address = '모름'
        self.lock = Lock()

    def across(self, name, address):
        self.lock.acquire() # Critical Section (임계 영역 / cs)
        self.counter += 1
        self.name = name
        self.address = address
        self.check()
        self.lock.release() # Critical Section (임계 영역 /cs)

    def toString(self):
        self.lock.acquire() # Critical Section (임계 영역 / cs)
        return f'이름 : {self.name}, 출신 : {self.address}, 도전 횟수 : {self.counter}'
        self.lock.release() # Critical Section (임계 영역 /cs)

    def check(self):
        if self.name[0] != self.address[0]:
            print('문제 발생 !!!' + self.toString())