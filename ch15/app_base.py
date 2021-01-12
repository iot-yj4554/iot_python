# 클래스가 많이 쓰이기 때문에 따로 모듈화함

import sys

class Configuration:
    def __init__(self):
        config = self.load() # 중요함
        self.fname = config['FNAME']
        self.encoding = config['ENCODING']

    def load(self):
        config = {}
        with open('config.ini', 'rt') as f:
            entries = f.readlines()
            for entry in entries:
                key, value = entry.split('=')
                config[key.strip()] = value.strip()
        return config

    def __str__(self):
        return f'<Configuration fname : {self.fname} / Encoding : {self.encoding}>'


class MenuItem:
    def __init__(self, title, func):
        self.title = title
        self.func = func
    
    def __str__(self):
        return f'<MenuItem : {self.title}>'

    def __repr__(self):
        return f'<MenuItem : {self.title}>'

        
class Menu:
    def __init__(self):
        self.menu_items = [] # MenuItem 객체를 담을 리스트

    def add(self, title, func): # 여러 menu_item을 리스트에 담음
        menu_item = MenuItem(title, func)
        self.menu_items.append(menu_item)

    def select_menu(self):
        print()
        for ix, menu_item in enumerate(self.menu_items):
            print(f'{ix}) {menu_item.title}', end='  ')
        print()
        menu = int(input('입력 : '))
        return menu

    def run(self, menu):
        if 0 <= menu < len(self.menu_items):
            menu_item = self.menu_items[menu]
            menu_item.func() # 괄호를 써야만 함 ---> 인스턴스의 메서드를 호출하겠다는 의미
        else:
            print('잘못된 메뉴입니다.')


# 템플릿 패턴
class Application:
    def __init__(self):
        self.config = Configuration()
        self.menu = Menu()
        self.create_menu(self.menu)

    def create_menu(self, menu):
        pass
    
    def run(self):
        while True:
            menu = self.menu.select_menu()
            self.menu.run(menu)
            
    def destroyed(self):
        pass

    def exit(self):
        if input('정말로 종료할까요? (y/n) ') == 'y':
            self.destroyed()
            sys.exit(0)