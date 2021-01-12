# 일기장 app
# 주소록에서 부모 클래스로 쓰인 것들을 그대로 가져와서 사용함

from app_base import Application


# 일기장 app
class DiaryApp(Application):
    def __init__(self):
        super().__init__()

    def create_menu(self,menu):
        menu.add('쓰기', self.writeToday)
        menu.add('수정', self.update)
        menu.add('삭제', self.delete)
        menu.add('종료', self.exit)

    def writeToday(self):
        print('오늘의 일기 쓰기')

    def update(self):
        print('지난 일기 수정하기')

    def delete(self):
        print('지난 일기 삭제하기')


def main():
    app = DiaryApp()
    app.run()

main()