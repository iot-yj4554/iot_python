
import sys

class Configuration:
    def __init__(self):
        config = self.load()
        self.fname = config['FNAME']
        self.encoding = config['ENCODING']

    def load(self):
        config = {}
        with open('./config.ini', 'rt') as f:
            lines = f.readlines()
            for line in lines:
                config[line.replace('\n','').split('=')[0]] = line.replace('\n','').split('=')[1]
        
        return config
    

class MenuItem:
    def __init__(self, title, func):
        self.title = title
        self.func = func


class Menu:
    def __init__(self):
        self.menu_items = []

    def add(self, title, func):
        menu_item = MenuItem(title, func)
        self.menu_items.append(menu_item)

    def select_menu(self):
        print()
        for ix, menu_item in enumerate(self.menu_items):
            print(f'{ix}) {menu_item.title}', end='  ')
        print()

        menu_num = int(input('입력 : '))
        return menu_num
    
    def run(self, menu_num):
        if 0 <= menu_num < len(self.menu_items):
            menu_item = self.menu_items[menu_num]
            menu_item.func()
        else:
            print('잘못된 메뉴입니다.')


class Application:
    def __init__(self):
        self.config = Configuration()
        self.menu = Menu()
        self.create_menu(self.menu)

    def create_menu(self,menu):
        pass
    
    def run(self):
        while True:
            menu = self.menu.select_menu()
            self.menu.run(menu)

    # def exit(self):
    #     if input('정말로 종료할까요? (y/n) ') == 'y':
    #         sys.exit(0)
            
    

    